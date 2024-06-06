# from obswebsocket import obsws, requests
import obswebsocket as ob
from time import sleep
# OBS WebSocket server address (default is localhost)
host = "192.168.56.1"
# OBS WebSocket server port (default is 4444)
port = 4455
# OBS WebSocket server password (if set)
password = "0vyx9MQIM1Erx7wt"

# Connect to OBS WebSocket server
try:
    # Connect to OBS WebSocket server
    ws = ob.obsws(host, port, password)
    ws.connect()
    print("Conexión exitosa con el servidor OBS.")
except Exception as e:
    print("Error al conectar con el servidor OBS:", e)




    # Switch to a specific scene
def switch_scene(scene_name):
    ws.call(requests.SetCurrentScene(scene_name))

# Toggle the visibility of a source in the current scene
def toggle_source(source_name):
    ws.call(requests.GetSceneList(), lambda resp: toggle_source_in_scene(resp, source_name))

def toggle_source_in_scene(response, source_name):
    for scene in response.getScenes():
        for item in scene.getItems():
            if item.getSourceName() == source_name:
                visible = not item.getVisible()
                ws.call(requests.SetSceneItemRender(scene.getName(), item.getSourceName(), visible))
                return

# Example usage
# switch_scene("Escena")
# toggle_source("Fuente1")
sleep(5)
response = ws.call(ob.requests.StartRecording())
i = 0
while not response.status:
    response = ws.call(ob.requests.StartRecording())
    i = i + 1
    if i>=200:
        raise Exception("Failed to start recording",response)
print(response.status)
ws.disconnect()
sleep(5)
print("Hello world!")