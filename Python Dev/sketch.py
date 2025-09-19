# Lista
nomes=["Daniel", "Dani", "José", "Sapôncio"]
nomes.append("Maria Clara") #Adiciona informações a uma lista
print(nomes)

primeiro_nome = nomes[0]
print(primeiro_nome)

# Dicionario Python
# role = Quem enviou a mensagem ="função"
#content = Qual o conteudo da Mensagem = "conteudo"


mensagem ={"quem": "Daniel", "texto": "coe galera"}

# Dicionario:{'key': <value>, 'key': <value>} 
# 1 Elemento: dicionario[key] -> Valor

msg_texto = mensagem["texto"]
msg_quem = mensagem["quem"]
print(msg_quem, msg_texto)

# Lista + Dicionario
lista_msgs = [
	{"role": "user", "content": "coe galera"},
	{"role": "assistant", "content": "Resposta da IA"},
	{"role": "Daniel", "content": "Tamo junto"}
    ]

lista_msgs.append(
	{"role": "assistant", "content": "I forgive you"}
	)

print(lista_msgs)