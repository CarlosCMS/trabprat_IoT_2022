# Our Simple IoT Gateway
# The data will arrive here, and we will send it to a an MQTT Server in the cloud

# IMU+GPS-Stream apps (install to mobile phone through Google PlayStore)
# - sends the measurements from your phone inertial sensors via UDP as CSV (Comma-Separated Values)
#   to a computer in your network.
# This turns your phone into a wireless inertial measurement unit (IMU).
# The following sensors are supported:
# - Accelerometer
# - Gyroscope
# - Magnetometer
# If your phone has not all these sensors, only the available sensor data is transmitted.
# Example UDP packet:
# 890.71558, 3, 0.076, 9.809, 0.565, 4, -0.559, 0.032, -0.134, 5, -21.660,-36.960,-28.140
# Timestamp [sec], sensorid, x, y, z, sensorid, x, y, z, sensorid, x, y, z
# Sensor id:
# 3 - Accelerometer (m/s^2)
# 4 - Gyroscope (rad/s)
# 5 - Magnetometer (micro-Tesla uT)

# in M10 the ID of the Gyroscope is 3
################################################################################################################
import time
import socket
import paho.mqtt.publish as publish

HOST = 'localhost'  # Standard loopback interface address (localhost)
PORT = 5555        # Port to listen on (non-privileged ports are > 1023)

# MQTT Variables
mqtt_broker = 'broker.mqttdashboard.com'
mqtt_port = 1883
mqtt_topic = "iot2021"
mqtt_client_id = 'clientId-B8U2PFx8OG'

def main():
    # Socket information (port needs to match port used in the app)
    host = ''
    port = 5555

    # Set up client
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.bind((host, port))
        print('Waiting to recieve data...')

        # Process the stream...
        while (1):
            message, address = s.recvfrom(8192)

            sensor_data = str(message).split(",")
            timestamp = sensor_data[0].replace("b'","")
            y_pos = sensor_data[3]
            ts = int(time.time())
            # collects data every 5 seconds
            if ts%5 == 0:
                msg = "t:{},y:{}".format(timestamp,y_pos)
                print(msg)
                publish.single(mqtt_topic, msg, hostname=mqtt_broker, port=mqtt_port)

if __name__ == "__main__":
    main()
