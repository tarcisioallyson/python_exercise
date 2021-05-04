import random
from datetime import datetime

#coleta os dados do usuário
nome_usuario = input("Digite seu nome: ")
idade_usuario = input("Digite sua idade: ")
data_aniversario = input("Digite sua data de aniversário: ")

#converte a data de aniversario e de registro para o formato dd/mm/aa
data_niver_conv = datetime.strptime(data_aniversario,'%d/%m/%Y').strftime('%d/%m/%Y')
data_registro = datetime.now().strftime("%d/%m/%Y")

#sortei um valor na lista
cartoes = ['R$50,00', 'R$250,00', 'R$120,00']
sorteio = random.choice(cartoes)

#exibe a mensagem na tela com as variáveis
print(f'Olá {nome_usuario}, seu registro foi concluído com sucesso no dia {data_registro}. '+
f'Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de {sorteio}.')