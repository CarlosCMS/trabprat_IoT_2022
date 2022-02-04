import socket
import time
import paho.mqtt.publish as publish

mqtt_broker = 'broker.mqttdashboard.com'
mqtt_port = 1883
mqtt_topic = "iot2022/estudante21"

HOST = ''
PORT = 5555

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        print('Aguardando dados ...')
        while (1):
            message, address = s.recvfrom(8192)
            ts = int(time.time())
            print(message)
            if ts%5 == 0:
                sensor_data = str(message).split(",")
                timestamp = sensor_data[0].replace("b'", "")
                x_pos = sensor_data[2]
                y_pos = sensor_data[3]
                z_pos = sensor_data[4]
                msg = '{},{},{},{}'.format(timestamp,x_pos, y_pos, z_pos)
                #msg = (timestamp,x_pos, y_pos,z_pos)
                #msg = y_pos
                publish.single(mqtt_topic, msg, hostname=mqtt_broker, port=mqtt_port)                

if __name__ == "__main__":
    main()