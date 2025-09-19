#Titulo 
#Input do Chat
#A cada mensagem enviada:
  # Mostrar a mensagem que o usuario enviou no chat
  # Enviar essa mensagem  para IA responder 
  # Aparace na tel a resposta da IA

# Streamlit - FrontEnd e BackEnd

import streamlit as st

st.write("## ChatBot com IA")

msg_usuario = st.chat_input("Escreva sua mensagem aqui")

if msg_usuario:
  print(msg_usuario)
  st.chat_message("user").write(msg_usuario)

  msg_ia = "Você quis dizer:" + msg_usuario +"?"

  st.chat_message("assistant").write(msg_ia)

  #User -> serhumano
  #assistant - > Inteligencia artificial