#Instruções para executar o projeto:

1 - Usamos o celular como dispositivo IoT.  Instalar o aplicativo sensor IMU+GPS-stream. Entrar com o IP da máquina. Usar a opção UDP Stream.
2 - Verificar se o computador e o celular estão na mesma rede wifi e verificar que não há bloqueio do firewall.
3 - Os dados enviados pelo IMU+GPS estão no formato string.  O código python (gateway simulado) separa os dados da hora e do acelerômetro.
4 - Usamos o broker HIVEMQ.  O Gateway envia os dados para o servidor MQTT. Código python main6.py simula o gateway.
5. Rodar o gateway - código python main6.py
6 - Para fazer o monitoramento via dashboard é necessária a instalação do freamework Fastapi e do servidor unvicorn.
7 - Dashboard - utilizar o código main.py da pasta dashboard.  Executar: uvicorn main:app --reload  (servidor tipo apache).
8 - As informações em formato JSON estarão disponíveis em http://127.0.0.1:8000/getdata
Abrir o socket HIVEMQ http://www.hivemq.com/demos/websocket-client/  
fazer o login com a conta iot2022/estudante21
9 - O grafana pode ser acessado em http://192.168.0.29:3000/login
10 - Irá observar que ao variar as posições do celular, os sensores enviarão novas informações. Alertas serão exibidos no dashboard.  Emails serão disparados aos gestores caso os dados de pressão e temperatura desviem muito de seus valores padrões.
