'''
Sockets UDP desenvolvidos para a disciplina de REDES de COMPUTADORES
Professor: Bruno
Alunos: Beatriz Duque (31906621) João Pedro (31954162)

Arquivo SERVIDOR: RECEBE
'''
import socket 
import time
import os

#configurando o servidor para receber os arquivos
ip_servidor="XXXXXXXXX"
porta_servidor=31954

#configurando SOCKET UDP 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((ip_servidor, porta_servidor))
sock.settimeout(40.0)
decisao = 2
while decisao != 1:
    print('Servidor Aberto e pronto para receber arquivos\nAguarde...')
    data=sock.recv(4)

    num_pacotes = int.from_bytes(data,"little")

    arquivo = str(input('Digite o nome que deseja dar ao arquivo recebido (nome + extensao):'))
    sock.settimeout(25.0) #se nao receber nenhum arquivo nesse tempo, sera fechado
    file=open(arquivo,"wb")
    kb = 512
    bts = kb*8
    print(f"Recebendo {num_pacotes} pacotes...")
    start=time.time()

    for i in range(num_pacotes):
        data=sock.recv(bts)
        file.write(data) #guardando o novo arquivo
        porcentagem=f"baixando...{round((100*(i+1))/num_pacotes,2)}%"
        print('/r'+porcentagem,end='')

    download=round(time.time()-start,2)
    print(f"\nO download foi completo em{download} sec")


    data, addr = sock.recvfrom(1024)
    #imprime endereço do cliente
    print("--------------------------------------")
    print("Mensagem recebida de : ",addr)
    #exibe texto enviado pelo cliente
    print ("Mensagem recebida:", data)
    decisao = input('\nDeseja fechar o servidor? 1. Sim 2. Nao:')    
file.close()
sock.close()
