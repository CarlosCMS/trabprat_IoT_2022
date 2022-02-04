import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def alerta(mensagem):    

    mail_content = 'Importante: Verifique o status operacional urgentemente'
    sender_address = 'petgraf100@gmail.com'
    sender_pass = 'grafan09'
    receiver_address = 'petgraf100@gmail.com'
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = mensagem  #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    #session.starttls() #enable security
    session.ehlo()
    session.starttls()
    session.ehlo()
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')
