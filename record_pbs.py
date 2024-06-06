from obswebsocket import obsws, requests
import time

# OBS WebSocket server address (default is localhost)
host = "192.168.56.1"
# OBS WebSocket server port (default is 4444)
port = 4455
# OBS WebSocket server password (if set)
password = "0vyx9MQIM1Erx7wt"

# Connect to OBS WebSocket server
ws = obsws(host, port, password)
ws.connect()

try:
    # Start recording
    response = ws.call(requests.StartRecording())
    # if not response.status:
    #     raise Exception("Failed to start recording")
    print(response)

    #print("Recording started...")

    # Wait for 10 seconds
    time.sleep(10)

    # Stop recording
    response = ws.call(requests.StopRecording())
    if not response.status:
        raise Exception("Failed to stop recording")

    print("Recording stopped.")

except Exception as e:
    print("Error:", e)

finally:
    # Disconnect from OBS WebSocket server
    ws.disconnect()
