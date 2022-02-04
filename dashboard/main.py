from fastapi import FastAPI
from paho import mqtt
from fastapi_mqtt import FastMQTT, MQTTConfig
import re
import mainemail

mqtt_broker = 'broker.mqttdashboard.com'
mqtt_port = 1883
mqtt_topic = "iot2022/estudante21"
FILE_NAME = "data.txt"

app = FastAPI()

fast_mqtt = FastMQTT(config=MQTTConfig(host = mqtt_broker, port= mqtt_port, keepalive = 60))

fast_mqtt.init_app(app)

# Mensagem de conecção
@fast_mqtt.on_connect()
def connect(client, flags, rc, properties):
    # fast_mqtt.client.subscribe("/mqtt") #subscribing mqtt topic 
    print("Connected: ", client, flags, rc, properties)

# Quando uma mensagem é postada no tópíco
@fast_mqtt.on_message()
async def message(client, topic, payload, qos, properties):
    print("Received message: ",topic, payload.decode(), qos, properties)
    return 0

# Mensagem de desconexão
@fast_mqtt.on_disconnect()
def disconnect(client, packet, exc=None):
    print("Disconnected")

# Mensagem de subscrição
@fast_mqtt.on_subscribe()
def subscribe(client, mid, qos, properties):
    print("subscribed", client, mid, qos, properties)

# Subscrição em um determinado tópíco
@fast_mqtt.subscribe(mqtt_topic)
async def get_topic_data(client, topic, payload, qos, properties):
    print("data: ", topic, payload.decode(), qos, properties)
    text_file = open(FILE_NAME, "w+")
    n = text_file.write(payload.decode())
    text_file.close()

    return 0

@app.get("/getdata")
async def get_data():
    mf = open(FILE_NAME, "r+")
    file_content = mf.readlines()
    pad = [-0.230,-0.019,9.768]
    rows = []
    
    for row in file_content:
        aux = row.replace("'","")
        aux = aux.split(",")
        xdesv = float(aux[1])-pad[0]
        ydesv = float(aux[2])-pad[1]
        zdesv = float(aux[3])-pad[2]
        if xdesv < -5:
            avisopress = "Redução da pressão: perfuração under-balanced"
            mainemail.alerta(avisopress)
        elif xdesv > 5:
            avisopress = "Aumento da pressão: perfuração over-balanced"
            mainemail.alerta(avisopress)
        else:
            avisopress = "Pressão Adequada"
        ydesv = float(aux[2])-pad[1]
        if -5 <=ydesv < 5:
            avisotemp = "Temperatura Adequada"            
        else:
            avisotemp = "Desvio de Temperatura"
            mainemail.alerta(avisotemp)
        zdesv = float(aux[3])-pad[2]
        if -5 <=zdesv < 5:
            avisocorr = "Tensão normal"
        else:
            avisocorr = "Avaliar Tensão"
        rows.append({
            #"teste": file_content,
            "tempo": float(aux[0]),
            "Pressão": float(aux[1]),
            "Temperatura": float(aux[2]),
            "Corrente": float(aux[3]),
            "Desvio Pressão": xdesv,
            "Desvio Temperatura": ydesv,
            "Desvio Corrente": zdesv,
            "Aviso Pressão": avisopress,
            "Aviso Temperatura": avisotemp,
            "Aviso Corrente": avisocorr
        })    
    
    return rows


@app.get('/teste')
async def teste():
    return "Teste"