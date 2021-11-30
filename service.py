import smtplib, ssl

port = 587
smtp_server = "smtp.seznam.cz"
sender_email = "@email.cz / @seznam.cz"
password = "Passwd seznam"
receiver_email = "@gmail.com"

nko= "\n" 

msg_from = "from:" + sender_email
msg_to = nko + "to:" + receiver_email
msg_subject = "Testovaci email" 
msg_subject_komplet = nko + "subject:" + msg_subject + nko + nko 
msg_msg = "Toto je obsah emailu"

message = msg_from + msg_to + msg_subject_komplet + msg_msg

def SendMailf():
    context = ssl._create_unverified_context() #Ignoruje certifikát
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        print("Email Zaslán:" + message) #Debug

SendMailf() 
