# server/websocket_manager.py

from fastapi import WebSocket


# List of currently connected clients
active_connections = []


async def connect_client(websocket: WebSocket):
    """
    Accept a new WebSocket connection
    and add it to the active connections.
    """

    await websocket.accept()

    active_connections.append(websocket)

    print(f"Client connected ({len(active_connections)} online)")


def disconnect_client(websocket: WebSocket):
    """
    Remove a disconnected client.
    """

    if websocket in active_connections:
        active_connections.remove(websocket)

    print(f"Client disconnected ({len(active_connections)} online)")


def get_connected_clients():
    """
    Return all connected clients.
    """

    return active_connections


def get_online_count():
    """
    Return number of connected clients.
    """

    return len(active_connections)
