"""
Desktop Chat Server

Main server entry point.

Responsibilities:
- Starts FastAPI server
- Creates WebSocket endpoint
- Receives client events
- Routes authentication requests
- Tracks connected users
- Maintains WebSocket heartbeat
"""


from fastapi import FastAPI
from fastapi import WebSocket
from fastapi import WebSocketDisconnect


import uvicorn



from server.config import SERVER_HOST
from server.config import SERVER_PORT
from server.config import WEBSOCKET_ENDPOINT



from server.database.create_tables import create_tables

from server.database.queries import update_user_status



from server.websocket_manager import connect_client
from server.websocket_manager import disconnect_client
from server.websocket_manager import register_user_connection
from server.websocket_manager import remove_user_connection



from server.auth.authentication import login
from server.auth.authentication import register



from shared.protocol import read_packet
from shared.protocol import create_packet



from shared.events import LOGIN
from shared.events import REGISTER
from shared.events import LOGOUT
from shared.events import LOGIN_SUCCESS
from shared.events import PING
from shared.events import PONG





app = FastAPI(

    title="Desktop Chat Server"

)







@app.on_event("startup")
async def startup_event():

    """
    Runs when server starts.
    """


    create_tables()



    print("=" * 50)

    print(
        "Desktop Chat Server Started..."
    )

    print(
        f"Listening on {SERVER_HOST}:{SERVER_PORT}"
    )

    print("=" * 50)









@app.get("/")
def home():

    """
    Server health check.
    """


    return {

        "status": "running",

        "server": "Desktop Chat Server"

    }









@app.websocket(WEBSOCKET_ENDPOINT)
async def websocket_endpoint(

        websocket: WebSocket

):

    """
    Main WebSocket endpoint.
    """


    await connect_client(

        websocket

    )



    try:


        while True:



            message = await websocket.receive_text()



            print(

                "Received:",

                message

            )



            packet = read_packet(

                message

            )



            event = packet.get(

                "event"

            )



            data = packet.get(

                "data",

                {}

            )



            response = None







            # ---------------------------------
            # Heartbeat
            # ---------------------------------

            if event == PING:


                pong_packet = create_packet(

                    PONG,

                    {}

                )



                await websocket.send_text(

                    pong_packet

                )



                continue







            # ---------------------------------
            # Register
            # ---------------------------------

            elif event == REGISTER:



                response = register(

                    data

                )









            # ---------------------------------
            # Login
            # ---------------------------------

            elif event == LOGIN:



                response = login(

                    data

                )



                if response is not None:



                    login_packet = read_packet(

                        response

                    )



                    if login_packet["event"] == LOGIN_SUCCESS:



                        user_id = login_packet["data"]["user_id"]



                        register_user_connection(

                            user_id,

                            websocket

                        )



                        update_user_status(

                            user_id,

                            "Online"

                        )



                        print(

                            f"User {user_id} logged in."

                        )









            # ---------------------------------
            # Logout
            # ---------------------------------

            elif event == LOGOUT:



                user_id = data.get(

                    "user_id"

                )



                if user_id is not None:



                    remove_user_connection(

                        user_id

                    )



                    print(

                        f"User {user_id} logged out."

                    )









            # ---------------------------------
            # Unknown Event
            # ---------------------------------

            else:



                print(

                    f"Unknown event: {event}"

                )









            # ---------------------------------
            # Send Response
            # ---------------------------------

            if response is not None:



                await websocket.send_text(

                    response

                )







    except WebSocketDisconnect:



        print(

            "Client disconnected."

        )



        disconnect_client(

            websocket

        )









if __name__ == "__main__":



    uvicorn.run(

        "server.main:app",

        host=SERVER_HOST,

        port=SERVER_PORT,

        reload=True

    )