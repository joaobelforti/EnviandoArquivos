'''
Sockets UDP desenvolvidos para a disciplina de REDES de COMPUTADORES
Professor: Bruno
Alunos: Beatriz Duque (31906621) João Pedro (31954162)

Arquivo CLIENTE: ENVIA
'''

import socket  #importa modulo socket
import os
import time


'''
Funcao utilizada para escrever o caminho de onde o
arquivo se encontra no computador
'''

def abrir_arquivo():
    entrada = ''
    caminho = ''
    print("Digite x para parar de digitar o caminho.")
    while entrada!='x':
        entrada = input("cd: ")
        if (entrada!='x'):
            caminho = caminho + '/' + entrada
            print(caminho)
        
    arquivo = input('Digite o nome do arquivo que deseja enviar:')
    arquivo = caminho + '/' +arquivo
    arquivo.encode()
    arquivo_aberto = open(arquivo, 'rb')
    
    return arquivo_aberto


#inicio do programa
#configurando o cliente
#dados de quem ira receber
IP_destino = "201.68.216.57"  #Endereço IP do servidor
PORTA_destino = 9090         #Numero de porta do servidor


endereco = (IP_destino, PORTA_destino)

#Criação de socket UDP
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#configurando o timeout
sock.connect(endereco)
sock.settimeout(10.0) # apos 10 segundos, configura uma perda de pacote 

print('Voce comecara a enviar arquivos. Digite "quit" quando desejar sair.')
count = 1 #contador de arquivos
MENSAGEM = ''
while MENSAGEM!= "quit" :
    if (MENSAGEM != "quit"):
        print('Enviando arquivos...')
        MENSAGEM = input("Digite sua mensagem ('quit' para sair):")
        print('ARQUIVO:',count)
        arquivo = abrir_arquivo() #chamando abertura do arquivo
        print("----------------------------------")
        #uma mensagem auxiliar chegará para o servidor
        print ("Endereço IP de destino:", IP_destino)
        print ("Porta UDP de destino:", PORTA_destino)
    

        #configurando o arquivo para ser enviado
        tamanho = os.path.getsize('teste.txt') #transforma em bits
        kb = 512 #kilobytes
        bts = kb * 8 #tamanho em bytes

        #definindo o numero de pacotes que serao enviados
        num_pacotes = (tamanho//bts)+ 1 #conversao
        sock.sendall(num_pacotes.to_bytes(4,'little'))

        delay = 0.004 
        tempo = num_pacotes*(delay*1.2)

        #enviando os pacotes
        for i in range (num_pacotes):
            packet = arquivo.read(bts)
            sock.sendall(packet)
            print('enviado')
            time.sleep(delay) 
        
    


        #Envia mensagem usando socket UDP
        sock.sendto(MENSAGEM.encode('UTF-8'), (IP_destino, PORTA_destino))
        count+=1

    else:
        print("\nSaindo....")
        
    
sock.close()
arquivo.close()

