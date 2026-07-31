# server/websocket_manager.py


"""
WebSocket connection manager.

Responsible for:

- accepting connections
- tracking logged-in users
- mapping users to sockets
"""


from server.database.queries import update_last_seen
from server.database.queries import update_user_status


connected_users = {}


async def connect_client(websocket):
    """
    Accept a new client.
    """

    await websocket.accept()

    print("Client connected")


def register_user_connection(
        user_id,
        websocket
):
    """
    Associates a logged-in user
    with a WebSocket connection.
    """

    connected_users[user_id] = websocket

    print(f"User {user_id} connected.")


def remove_user_connection(user_id):
    """
    Marks a user as logged out.

    Keeps the WebSocket connection alive.
    The connection is only removed when
    the socket actually disconnects.
    """

    update_user_status(
        user_id,
        "Offline"
    )

    update_last_seen(
        user_id
    )


def disconnect_client(websocket):
    """
    Handles unexpected WebSocket disconnect.
    """

    disconnected_user = None

    for user_id, socket in list(connected_users.items()):

        if socket == websocket:

            disconnected_user = user_id

            break


    if disconnected_user is not None:

        del connected_users[disconnected_user]

        update_user_status(
            disconnected_user,
            "Offline"
        )

        update_last_seen(
            disconnected_user
        )


    print(
        "Active users:",
        len(connected_users)
    )

def get_connected_clients():
    """
    Returns connected users.
    """

    return connected_users