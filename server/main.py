# server/main.py

from fastapi import FastAPI
from fastapi import WebSocket
from fastapi import WebSocketDisconnect
import uvicorn

from config import SERVER_HOST
from config import SERVER_PORT
from config import WEBSOCKET_ENDPOINT

from websocket_manager import connect_client
from websocket_manager import disconnect_client


app = FastAPI(
    title="Desktop Chat Server"
)


@app.on_event("startup")
async def startup_event():
    """
    Runs once when the server starts.
    """

    print("=" * 50)
    print("Desktop Chat Server Started...")
    print(f"Listening on {SERVER_HOST}:{SERVER_PORT}")
    print("=" * 50)


@app.get("/")
def home():
    """
    Simple health check endpoint.
    """

    return {
        "status": "running",
        "server": "Desktop Chat Server"
    }


@app.websocket(WEBSOCKET_ENDPOINT)
async def websocket_endpoint(websocket: WebSocket):
    """
    Temporary WebSocket endpoint.
    """

    await connect_client(websocket)

    try:

        while True:

            data = await websocket.receive_text()

            print(f"Received: {data}")

            # Temporary echo response
            await websocket.send_text(f"Server received: {data}")

    except WebSocketDisconnect:

        disconnect_client(websocket)


if __name__ == "__main__":

    uvicorn.run(
        "main:app",
        host=SERVER_HOST,
        port=SERVER_PORT,
        reload=True
    )
    