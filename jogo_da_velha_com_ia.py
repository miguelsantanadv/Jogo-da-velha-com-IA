import random
import time
import matplotlib.pyplot as plt
opcao = -5
conhecimento = []
conhecimento2 = []


def preencherVetor(vet):
   vet = [0, 0, 0,
          0, 0, 0,
          0, 0, 0]
   return vet


def instrucao():


   print("\n")
   print("1", "|", "2", "|", "3")
   print("_________")
   print("4", "|", "5", "|", "6")
   print("_________")
   print("7", "|", "8", "|", "9")
   print("\n")




def mostrarvetor(vet):


   # vetaux = vet.copy()
   #
   # for i in range(len(vetaux)):
   #     if vetaux[i] == 1:
   #             vetaux[i] = "X"
   #     elif vetaux[i] == -1:
   #             vetaux[i] = "O"
   #     elif vetaux[i] == 0:
   #             vetaux[i] = " "
   #
   # print("\n")
   # print(vetaux[0], "|", vetaux[1], "|", vetaux[2])
   # print("_________")
   # print(vetaux[3], "|", vetaux[4], "|", vetaux[5])
   # print("_________")
   # print(vetaux[6], "|", vetaux[7], "|", vetaux[8])
   # print("\n")
   pass




def limpar(base):
   p=0


   for linha in base:
       if(linha[10] < 0):
           base.remove(base[p])


       p+=1


def escrever_em_txt(matriz, nome_arquivo):
   with open(nome_arquivo, 'w') as arquivo:
       for linha in matriz:
           linha_texto = ' '.join(map(str, linha))
           arquivo.write(linha_texto + '\n')






def mostrargrafico(vitorias_jogador1, vitorias_jogador2, velhas, num_partidas):
   partidas = list(range(1, num_partidas + 1))


   plt.plot(partidas, vitorias_jogador1, label='Jogador 1', color='blue', marker='o')
   plt.plot(partidas, vitorias_jogador2, label='Jogador 2', color='red', marker='o')
   plt.plot(partidas, velhas, label='Velhas', color='gray', marker='o')


   plt.xlabel('Número de Partidas')
   plt.ylabel('Número de Vitórias/velhas')
   plt.title('Evolução das Vitórias')
   plt.legend()
   plt.grid(True)
   plt.show()


def jogando(vet,posicao, jogador, maquina):


   if vet[posicao] == 0:
       vet[posicao] = jogador
   else:
       while vet[posicao] != 0:
           print("posicao ja ocupada, tente novamente")
           posicao = int(input("Escolha novamente a posicao que deseja jogar:"))
           posicao = posicao - 1
   vet[posicao] = jogador


   if maquina == 1:
       mostrarvetor(vet)
       return posicao
   else:
       mostrarvetor(vet)




def maquina(vet, posicao, jogador, maquina):


   if vet[posicao] == 0:
       vet[posicao] = jogador
   else:
       while vet[posicao] != 0:
           posicao = random.randint(1, 9)
           posicao = posicao - 1
   vet[posicao] = jogador


   if maquina == 1:
       mostrarvetor(vet)
       return posicao
   else:
       mostrarvetor(vet)
       pass


def agente(vet, jogador, maquina, linhas, basededados):
   linharank = []
   rank = 0
   k= 0
   posicaoencontrada = 0
   ultimoinserido = 0




   for linha in basededados:
       if vet == linha[:9]:
           if(linha[10]>rank):
               linharank = linha
               rank = linha[10]
               posicaoencontrada = k


       k+=1




   if(linharank):
       posicao = linharank[9]
       vet[posicao] = jogador
       linhas.extend([posicaoencontrada])
   else:


       posicao = random.randint(1, 9)
       posicao = posicao - 1


       if vet[posicao] == 0:
           nova_linha = vet.copy()
           vet[posicao] = jogador
           nova_linha.extend([posicao, 0])
           basededados.append(nova_linha)
       else:
           while vet[posicao] != 0:
               posicao = random.randint(1, 9)
               posicao = posicao - 1


           nova_linha = vet.copy()
           vet[posicao] = jogador
           nova_linha.extend([posicao, 0])
           basededados.append(nova_linha)


       ultimoinserido = len(basededados) - 1
       linhas.extend([ultimoinserido])


       # j = 0
       # for linha in conhecimento:
       #     if (linha == nova_linha):
       #         linhasusadas.extend([j])
       #         break
       #     j = j + 1
       del nova_linha


   if (maquina == 1):
       mostrarvetor(vet)
       return posicao
   else:
       mostrarvetor(vet)




def possibilidade(vet, jogador):


   if(vet[0]+vet[1]+vet[2] == jogador * 2 ):
       if(vet[0] == 0):
           vet[0] = jogador
           pos = 0
       elif(vet[1] == 0):
           vet[1] = jogador
           pos = 1
       else:
           vet[2] = jogador
           pos = 2


   elif(vet[3]+vet[4]+vet[5] == jogador * 2 ):
       if (vet[3] == 0):
           vet[3] = jogador
           pos = 3
       elif (vet[4] == 0):
           vet[4] = jogador
           pos = 4
       else:
           vet[5] = jogador
           pos = 5


   elif (vet[6] + vet[7] + vet[8] == jogador * 2 ):
       if (vet[6] == 0):
           vet[6] = jogador
           pos = 6
       elif (vet[7] == 0):
           vet[7] = jogador
           pos = 7
       else:
           vet[8] = jogador
           pos = 8


   elif (vet[0] + vet[3] + vet[6] == jogador * 2 ):
       if (vet[0] == 0):
           vet[0] = jogador
           pos = 0
       elif (vet[3] == 0):
           vet[3] = jogador
           pos = 3
       else:
           vet[6] = jogador
           pos = 6


   elif (vet[1] + vet[4] + vet[7] == jogador * 2 ):
       if (vet[1] == 0):
           vet[1] = jogador
           pos = 1
       elif (vet[4] == 0):
           vet[4] = jogador
           pos = 4
       else:
           vet[7] = jogador
           pos = 7


   elif (vet[2] + vet[5] + vet[8] == jogador * 2 ):
       if (vet[2] == 0):
           vet[2] = jogador
           pos = 2
       elif (vet[5] == 0):
           vet[5] = jogador
           pos = 5
       else:
           vet[8] = jogador
           pos = 8


   elif (vet[0] + vet[4] + vet[8] == jogador * 2 ):
       if (vet[0] == 0):
           vet[0] = jogador
           pos = 0
       elif (vet[4] == 0):
           vet[4] = jogador
           pos = 4
       else:
           vet[8] = jogador
           pos = 8


   elif (vet[2] + vet[4] + vet[6] == jogador * 2):
       if (vet[2] == 0):
           vet[2] = jogador
           pos = 2
       elif (vet[4] == 0):
           vet[4] = jogador
           pos = 4
       else:
           vet[6] = jogador
           pos = 6




   elif(vet[0]+vet[1]+vet[2] == jogador * -2):
       if (vet[0] == 0):
           vet[0] = jogador
           pos = 0
       elif (vet[1] == 0):
           vet[1] = jogador
           pos = 1
       else:
           vet[2] = jogador
           pos = 2


   elif(vet[3]+vet[4]+vet[5] == jogador * -2 ):
       if (vet[3] == 0):
           vet[3] = jogador
           pos = 3
       elif (vet[4] == 0):
           vet[4] = jogador
           pos = 4
       else:
           vet[5] = jogador
           pos = 5


   elif(vet[6] + vet[7] + vet[8] == jogador * -2):
       if (vet[6] == 0):
           vet[6] = jogador
           pos = 6
       elif (vet[7] == 0):
           vet[7] = jogador
           pos = 7
       else:
           vet[8] = jogador
           pos = 8


   elif(vet[0] + vet[3] + vet[6] == jogador * -2):
       if (vet[0] == 0):
           vet[0] = jogador
           pos = 0
       elif (vet[3] == 0):
           vet[3] = jogador
           pos = 3
       else:
           vet[6] = jogador
           pos = 6


   elif(vet[1] + vet[4] + vet[7] == jogador * -2):
       if (vet[1] == 0):
           vet[1] = jogador
           pos = 1
       elif (vet[4] == 0):
           vet[4] = jogador
           pos = 4
       else:
           vet[7] = jogador
           pos = 7


   elif(vet[2] + vet[5] + vet[8] == jogador * -2):
       if (vet[2] == 0):
           vet[2] = jogador
           pos = 2
       elif (vet[5] == 0):
           vet[5] = jogador
           pos = 5
       else:
           vet[8] = jogador
           pos = 8


   elif(vet[0] + vet[4] + vet[8] == jogador * -2):
       if (vet[0] == 0):
           vet[0] = jogador
           pos = 0
       elif (vet[4] == 0):
           vet[4] = jogador
           pos = 4
       else:
           vet[8] = jogador
           pos = 8


   elif(vet[2] + vet[4] + vet[6] == jogador * -2):
       if (vet[2] == 0):
           vet[2] = jogador
           pos = 2
       elif (vet[4] == 0):
           vet[4] = jogador
           pos = 4
       else:
           vet[6] = jogador
           pos = 6






   elif (vet[0] + vet[1] + vet[2] == jogador and vet[0] == 0 or vet[0] + vet[1] + vet[2] == jogador and vet[1] == 0 or vet[0] + vet[1] + vet[2] == jogador and vet[2] == 0):
       if (vet[0] == 0):
           vet[0] = jogador
           pos = 0
       elif (vet[1] == 0):
           vet[1] = jogador
           pos = 1
       elif(vet[2]==0):
           vet[2] = jogador
           pos = 2


   elif (vet[3] + vet[4] + vet[5] == jogador and vet[3] == 0 or vet[3] + vet[4] + vet[5] == jogador and vet[4] == 0 or vet[3] + vet[4] + vet[5] == jogador and vet[5] == 0 ):
       if (vet[3] == 0):
           vet[3] = jogador
           pos = 3
       elif (vet[4] == 0):
           vet[4] = jogador
           pos = 4
       elif (vet[5] == 0):
           vet[5] = jogador
           pos = 5


   elif (vet[6] + vet[7] + vet[8] == jogador and vet[6] == 0 or vet[6] + vet[7] + vet[8] == jogador and vet[7] == 0 or vet[6] + vet[7] + vet[8] == jogador and vet[8] == 0):
       if (vet[6] == 0):
           vet[6] = jogador
           pos = 6
       elif (vet[7] == 0):
           vet[7] = jogador
           pos = 7
       elif (vet[8] == 0):
           vet[8] = jogador
           pos = 8


   elif (vet[0] + vet[3] + vet[6] == jogador and vet[0] == 0 or vet[0] + vet[3] + vet[6] == jogador and vet[3] == 0 or vet[0] + vet[3] + vet[6] == jogador and vet[6] == 0):
       if (vet[0] == 0):
           vet[0] = jogador
           pos = 0
       elif (vet[3] == 0):
           vet[3] = jogador
           pos = 3
       elif (vet[6] == 0):
           vet[6] = jogador
           pos = 6


   elif (vet[1] + vet[4] + vet[7] == jogador and vet[1] == 0 or vet[1] + vet[4] + vet[7] == jogador and vet[4] == 0 or vet[1] + vet[4] + vet[7] == jogador and vet[7] == 0):
       if (vet[1] == 0):
           vet[1] = jogador
           pos = 1
       elif (vet[4] == 0):
           vet[4] = jogador
           pos = 4
       elif (vet[7] == 0):
           vet[7] = jogador
           pos = 7


   elif (vet[2] + vet[5] + vet[8] == jogador and vet[2] == 0 or vet[2] + vet[5] + vet[8] == jogador and vet[5] == 0 or vet[2] + vet[5] + vet[8] == jogador and vet[8] == 0):
       if (vet[2] == 0):
           vet[2] = jogador
           pos = 2
       elif (vet[5] == 0):
           vet[5] = jogador
           pos = 5
       elif (vet[8] == 0):
           vet[8] = jogador
           pos = 8


   elif (vet[0] + vet[4] + vet[8] == jogador and vet[0] == 0  or vet[0] + vet[4] + vet[8] == jogador and vet[4] == 0 or vet[0] + vet[4] + vet[8] == jogador and vet[8] == 0):
       if (vet[0] == 0):
           vet[0] = jogador
           pos = 0
       elif (vet[4] == 0):
           vet[4] = jogador
           pos = 4
       elif (vet[8] == 0):
           vet[8] = jogador
           pos = 8


   elif (vet[2] + vet[4] + vet[6] == jogador and vet[2] == 0 or vet[2] + vet[4] + vet[6] == jogador and vet[4] == 0 or vet[2] + vet[4] + vet[6] == jogador and vet[6] == 0):
       if (vet[2] == 0):
           vet[2] = jogador
           pos = 2
       elif (vet[4] == 0):
           vet[4] = jogador
           pos = 4
       elif (vet[6] == 0):
           vet[6] = jogador
           pos = 6




   else:
       for i in range(len(vet)):
           if vet[i] == 0:
               vet[i] = jogador
               pos = i
               break


   return pos




def maquinaimpossivel(vet, jogador, cont, vetjogadas, retorno):


   if cont == 0:
       vet[0] = jogador
       pos = 0


   elif cont == 1:
       if (vetjogadas[0] == 4):
           vet[0] = jogador
           pos = 0
       else:
           vet[4] = jogador
           pos = 4


   elif cont == 2:
       if (vetjogadas[0] == 2 or vetjogadas[0] == 8):
           vet[6] = jogador
           pos = 6
       elif (vetjogadas[0] == 6):
           vet[2] = jogador
           pos = 2
       elif (vetjogadas[0] == 1 or vetjogadas[0] == 4):
           vet[3] = jogador
           pos = 3
       elif (vetjogadas[0] == 3):
           vet[1] = jogador
           pos = 1
       elif (vetjogadas[0] == 5 or vetjogadas[0] == 7):
           vet[4] = jogador
           pos = 4


   elif cont == 3:
       if(vetjogadas[0] == 4):
           if(vetjogadas[1] == 1):
               vet[7] = jogador
               pos = 7
           elif(vetjogadas[1] == 2):
               vet[6] = jogador
               pos = 6
           elif(vetjogadas[1] == 3):
               vet[5] = jogador
               pos = 5
           elif(vetjogadas[1] == 5):
               vet[3] = jogador
               pos = 3
           elif (vetjogadas[1] == 6):
               vet[2] = jogador
               pos = 2
           elif (vetjogadas[1] == 7):
               vet[1] = jogador
               pos = 1
           elif (vetjogadas[1] == 8):
               vet[6] = jogador
               pos = 6
       else:
           if (vetjogadas[0] == 0 and vetjogadas[1] == 2 or vetjogadas[0] == 2 and vetjogadas[1] == 0 or vetjogadas[0] == 3 and vetjogadas[1] == 5 or vetjogadas[0] == 5 and vetjogadas[1] == 3 or
                   vetjogadas[0] == 6 and vetjogadas[1] == 5 or vetjogadas[0] == 5 and vetjogadas[1] == 6 ):
               vet[1] = jogador
               pos = 1
           elif (vetjogadas[0] == 6 and vetjogadas[1] == 8 or vetjogadas[0] == 8 and vetjogadas[1] == 6):
               vet[7] = jogador
               pos = 7
           elif (vetjogadas[0] == 0 and vetjogadas[1] == 6 or vetjogadas[0] == 6 and vetjogadas[1] == 0 or vetjogadas[0] == 1 and vetjogadas[1] == 7 or vetjogadas[0] == 7 and vetjogadas[1] == 1
                 or vetjogadas[0] == 2 and vetjogadas[1] == 6 or vetjogadas[0] == 6 and vetjogadas[1] == 2):
               vet[3] = jogador
               pos = 3
           elif (vetjogadas[0] == 2 and vetjogadas[1] == 8 or vetjogadas[0] == 8 and vetjogadas[1] == 2 or vetjogadas[0] == 0 and vetjogadas[1] == 8 or vetjogadas[0] == 8 and vetjogadas[1] == 0):
               vet[5] = jogador
               pos = 5
           elif(vetjogadas[0] == 0 and vetjogadas[1] == 1 or vetjogadas[0] == 1 and vetjogadas[1] == 0 or vetjogadas[0] == 8 and vetjogadas[1] == 5 or vetjogadas[0] == 5 and vetjogadas[1] == 8
                or vetjogadas[0] == 5 and vetjogadas[1] == 7 or vetjogadas[0] == 7 and vetjogadas[1] == 5 or vetjogadas[0] == 1 and vetjogadas[1] == 8 or vetjogadas[0] == 8 and vetjogadas[1] == 1 or
                vetjogadas[0] == 0 and vetjogadas[1] == 5 or vetjogadas[0] == 5 and vetjogadas[1] == 0):
               vet[2] = jogador
               pos = 2
           elif (vetjogadas[0] == 1 and vetjogadas[1] == 2 or vetjogadas[0] == 2 and vetjogadas[1] == 1 or vetjogadas[0] == 3 and vetjogadas[1] == 6 or vetjogadas[0] == 6 and vetjogadas[1] == 3 or
                 vetjogadas[0] == 1 and vetjogadas[1] == 6 or vetjogadas[0] == 6 and vetjogadas[1] == 1 or vetjogadas[0] == 2 and vetjogadas[1] == 3 or vetjogadas[0] == 3 and vetjogadas[1] == 2 or
                 vetjogadas[0] == 3 and vetjogadas[1] == 7 or vetjogadas[0] == 7 and vetjogadas[1] == 3):
               vet[0] = jogador
               pos = 0
           elif (vetjogadas[0] == 0 and vetjogadas[1] == 3 or vetjogadas[0] == 3 and vetjogadas[1] == 0 or vetjogadas[0] == 1 and vetjogadas[1] == 3 or vetjogadas[0] == 3 and vetjogadas[1] == 1
                 or vetjogadas[0] == 7 and vetjogadas[1] == 8 or vetjogadas[0] == 8 and vetjogadas[1] == 7 or vetjogadas[0] == 0 and vetjogadas[1] == 7 or vetjogadas[0] == 7 and vetjogadas[1] == 0)\
                 or vetjogadas[0] == 3 and vetjogadas[1] == 8 or vetjogadas[0] == 8 and vetjogadas[1] == 3:
               vet[6] = jogador
               pos = 6
           elif (vetjogadas[0] == 2 and vetjogadas[1] == 5 or vetjogadas[0] == 5 and vetjogadas[1] == 2 or vetjogadas[0] == 6 and vetjogadas[1] == 7 or vetjogadas[0] == 7 and vetjogadas[1] == 6
                 or vetjogadas[0] == 2 and vetjogadas[1] == 7 or vetjogadas[0] == 7 and vetjogadas[1] == 2 or vetjogadas[0] == 1 and vetjogadas[1] == 5 or vetjogadas[0] == 5 and vetjogadas[1] == 1):
               vet[8] = jogador
               pos = 8


   elif cont == 4:
       if (vetjogadas[0] == 2 or vetjogadas[0] == 8):
           if(vetjogadas[1]!= 3):
               vet[3] = jogador
               pos = 3
           elif(vet[2] == 0):
               vet[2] = jogador
               pos = 2
           else:
               vet[8] = jogador
               pos = 8
       elif (vetjogadas[0] == 5 or vetjogadas[0] == 7):
           if(vetjogadas[1]!=8):
               vet[8] = jogador
               pos = 8
           elif(vet[5] == 0):
               vet[6] = jogador
               pos = 6
           else:
               vet[2] = jogador
               pos = 2
       elif (vetjogadas[0] == 1 or vetjogadas[0] == 4):
           if(vetjogadas[1]!=6):
               vet[6] = jogador
               pos = 6
           elif(vet[4] == 0):
               vet[4] = jogador
               pos = 4
           else:
               vet[2] = jogador
               pos = 2
       elif (vetjogadas[0] == 6):
           if (vetjogadas[1] != 1):
               vet[1] = jogador
               pos = 1
           else:
               vet[8] = jogador
               pos = 8
       elif (vetjogadas[0] == 3):
           if (vetjogadas[1] != 2):
               vet[2] = jogador
               pos = 2
           else:
               vet[4] = jogador
               pos = 4


   elif cont == 5:
       pos = possibilidade(vet, jogador)


   elif cont == 6:
       if (vetjogadas[0] == 2 or vetjogadas[0] == 8):
           if(vet[4]==0):
               vet[4] = jogador
               pos = 4
           elif(vet[2] == jogador):
               vet[1] = jogador
               pos = 1
           else:
               vet[7] = jogador
               pos = 7
       elif (vetjogadas[0] == 5 or vetjogadas[0] == 7):
           if (vet[2] == jogador ):
               if(vet[1]==0):
                   vet[1] = jogador
                   pos = 1
               else:
                   vet[6] = jogador
                   pos = 6
           else:
               if (vet[3] == 0):
                   vet[3] = jogador
                   pos = 3
               else:
                   vet[2] = jogador
                   pos = 2
       elif (vetjogadas[0] == 1 or vetjogadas[0] == 4):
           if(vet[4] == jogador):
               if(vet[8] == 0):
                   vet[8] = jogador
                   pos = 8
               else:
                   vet[5] = jogador
                   pos = 5
           else:
               if(vet[1] == 0):
                   vet[1] = jogador
                   pos = 1
               else:
                   vet[7] = jogador
                   pos = 7
       elif (vetjogadas[0] == 6):
           if (vet[4] == 0):
               vet[4] = jogador
               pos = 4
           else:
               vet[5] = jogador
               pos = 5
       elif (vetjogadas[0] == 3):
           if (vet[8] == 0):
               vet[8] = jogador
               pos = 8
           else:
               vet[7] = jogador
               pos = 7


   elif cont == 7:
      pos = possibilidade(vet, jogador)


   elif cont == 8:
       if(vet[8] == 0):
           vet[8] = jogador
           pos = 8
       else:
           vet[5] = jogador
           pos = 5


   else:
       for i in range(len(vet)):
           if vet[i] == 0:
               vet[i] = jogador
               pos = i
               break




   if(retorno == 1):
       mostrarvetor(vet)
       return pos
   else:
       mostrarvetor(vet)








def verificarganhador(vet):
   if (vet[0] + vet[1] + vet[2] == 3 or vet[3] + vet[4] + vet[5] == 3 or vet[6] + vet[7] + vet[8] == 3 or vet[0] +
       vet[ 4] + vet[8] == 3 or
       vet[0] + vet[3] + vet[6] == 3 or vet[1] + vet[4] + vet[7] == 3 or vet[2] + vet[5] + vet[8] == 3 or vet[2] +
       vet[4] + vet[6] == 3):
       #print("O JOGADOR NUMERO 1 GANHOU \n")
       return 1


   elif (vet[0] + vet[1] + vet[2] == -3 or vet[3] + vet[4] + vet[5] == -3 or vet[6] + vet[7] + vet[8] == -3 or vet[0] +
         vet[4] + vet[8] == -3 or
         vet[0] + vet[3] + vet[6] == -3 or vet[1] + vet[4] + vet[7] == -3 or vet[2] + vet[5] + vet[8] == -3 or vet[2] +
         vet[4] + vet[6] == -3):
       #print("O JOGADOR NUMERO 2 GANHOU \n")
       return 2


   else:
       for i in range(len(vet)):
           if vet[i] == 0:
               return 3


       #print("O JOGO DEU VELHA! \n")
       return 0




while opcao != 0:


   print("1 - Player vs Player")
   print("2 - Player vs Modo Facil")
   print("3 - Player vs Modo Impossivel")
   print("4 - Maquina Facil vs Maquina Facil")
   print("5 - Maquina Facil vs Maquina Impossivel")
   print("6 - Maquina Impossivel vs Maquina Impossivel")
   print("7 - Maquina Impossivel vs Agente inteligente")
   print("8 - Maquina Aleatorio vs Agente inteligente")
   print("9 - Agente inteligente vs Agente inteligente")


   print("0 - Sair do jogo")


   opcao = int(input("Escolha sua opcao:"))


   if opcao == 1:
       vet = []
       vet = preencherVetor(vet)
       cont = 0


       instrucao()


       while cont <= 4 or verificarganhador(vet) == 3:


           posicao1 = int(input("O jogador numero 1 escolhe a posicao que deseja jogar:"))
           posicao1 = posicao1 - 1
           jogando (vet, posicao1, 1, 0)
           cont += 1


           if verificarganhador(vet) != 3:
               break


           posicao2 = int(input("O jogador numero 2 escolhe a posicao que deseja jogar:"))
           posicao2 = posicao2 - 1
           jogando (vet, posicao2, -1, 0)
           cont += 1


   elif opcao == 2:
       vet = []
       vet = preencherVetor(vet)
       cont = 0


       inicia = int(input("Quem inicia o jogo: 1 - jogador ou 2 - maquina"))


       if inicia == 1:
           instrucao()


           while cont <= 4 or verificarganhador(vet) == 3:


               posicao1 = int(input("O jogador escolhe a posicao que deseja jogar:"))
               posicao1 = posicao1 - 1
               jogando(vet, posicao1, 1, 0)
               cont += 1


               if verificarganhador(vet) != 3:
                   break


               print("Vez da maquina:")
               time.sleep(1)
               posicao2 = random.randint(1, 9)
               posicao2 = posicao2 - 1
               maquina(vet, posicao2, -1, 0)
               cont += 1


       elif inicia == 2:
           instrucao()


           while cont <= 4 or verificarganhador(vet) == 3:


               print("Vez da maquina:")
               time.sleep(1)
               posicao2 = random.randint(1, 9)
               posicao2 = posicao2 - 1
               maquina(vet, posicao2, 1, 0)
               cont += 1


               if verificarganhador(vet) != 3:
                   break


               posicao1 = int(input("O jogador escolhe a posicao que deseja jogar:"))
               posicao1 = posicao1 - 1
               jogando(vet, posicao1, -1, 0)
               cont += 1


   elif opcao == 3:
       vet = []
       vetorjogadas = []
       vet = preencherVetor(vet)
       cont = 0
       j= 0


       inicia = int(input("Quem inicia o jogo: 1 - jogador ou 2 - maquina"))


       if inicia == 1:
           instrucao()


           while cont <= 4 or verificarganhador(vet) == 3:


               posicao1 = int(input("O jogador escolhe a posicao que deseja jogar:"))
               posicao1 = posicao1 - 1
               vetorjogadas.insert(j, jogando(vet, posicao1, 1, 1))
               j+=1
               cont += 1


               if verificarganhador(vet) != 3:
                   break


               print("Vez da maquina:")
               time.sleep(1)
               maquinaimpossivel(vet, -1, cont, vetorjogadas, 0)
               cont += 1


       elif inicia == 2:
           instrucao()


           while cont <= 4 or verificarganhador(vet) == 3:


               print("Vez da maquina:")
               time.sleep(1)
               maquinaimpossivel(vet, 1, cont, vetorjogadas, 0)
               cont += 1


               if verificarganhador(vet) != 3:
                   break


               posicao1 = int(input("O jogador escolhe a posicao que deseja jogar:"))
               posicao1 = posicao1 - 1
               vetorjogadas.insert(j, jogando(vet, posicao1, -1, 1))
               j += 1
               cont += 1




   elif opcao == 4:
       ganhador1total = 0
       ganhador2total = 0
       velhatotal = 0
       vitorias_jogador1 = []
       vitorias_jogador2 = []
       velhas = []


       vet = []
       vet = preencherVetor(vet)
       cont = 0


       instrucao()


       numeropartidas = int(input("Numero de partidas:"))
       acabou = numeropartidas


       while (acabou != 0):
           vet = []
           vetorjogadas = [8]
           vetorjogadas2 = [8]
           vet = preencherVetor(vet)
           cont = 0
           j = 0
           k = 0


           while True:




               print("Vez da maquina 1:")
               posicao1 = random.randint(1, 9)
               posicao1 = posicao1 - 1
               maquina(vet, posicao1, 1, 0)
               #time.sleep(1)
               cont += 1


               resultado = verificarganhador(vet)
               if (resultado == 1):
                   ganhador1total += 1
                   vitorias_jogador1.append(ganhador1total)
                   vitorias_jogador2.append(ganhador2total)
                   velhas.append(velhatotal)
                   break
               elif (resultado == 2):
                   ganhador2total += 1
                   vitorias_jogador1.append(ganhador1total)
                   vitorias_jogador2.append(ganhador2total)
                   velhas.append(velhatotal)
                   break
               elif (resultado == 0):
                   velhatotal += 1
                   vitorias_jogador1.append(ganhador1total)
                   vitorias_jogador2.append(ganhador2total)
                   velhas.append(velhatotal)
                   break




               print("Vez da maquina 2:")
               posicao2 = random.randint(1, 9)
               posicao2 = posicao2 - 1
               maquina(vet, posicao2, -1, 0)
               #time.sleep(1)
               cont += 1


               resultado = verificarganhador(vet)
               if (resultado == 1):
                   ganhador1total += 1
                   vitorias_jogador1.append(ganhador1total)
                   vitorias_jogador2.append(ganhador2total)
                   velhas.append(velhatotal)
                   break
               elif (resultado == 2):
                   ganhador2total += 1
                   vitorias_jogador1.append(ganhador1total)
                   vitorias_jogador2.append(ganhador2total)
                   velhas.append(velhatotal)
                   break
               elif (resultado == 0):
                   velhatotal += 1
                   vitorias_jogador1.append(ganhador1total)
                   vitorias_jogador2.append(ganhador2total)
                   velhas.append(velhatotal)
                   break


           acabou -= 1


       print("0 primeiro ganhou: ", ganhador1total)
       print("0 segundo ganhou: ", ganhador2total)
       print("Velha: ", velhatotal)
       print("\n")
       mostrargrafico(vitorias_jogador1, vitorias_jogador2, velhas, numeropartidas)


   elif opcao == 5:
       ganhador1total = 0
       ganhador2total = 0
       velhatotal = 0
       vitorias_jogador1 = []
       vitorias_jogador2 = []
       velhas =[]




       instrucao()
       inicia = int(input("Quem inicia o jogo: 1 - Maquina Facil ou 2 - Maquina Impossivel"))
       numeropartidas = int(input("Numero de partidas:"))
       acabou = numeropartidas


       if(inicia == 1):
           while (acabou != 0):
               vet = []
               vetorjogadas = []
               vet = preencherVetor(vet)
               cont = 0
               j = 0


               while True:


                   print("Vez da maquina 1:")
                   posicao2 = random.randint(1, 9)
                   posicao2 = posicao2 - 1
                   vetorjogadas.insert(j, maquina(vet, posicao2, 1, 1))
                   j += 1


                   cont += 1


                   resultado = verificarganhador(vet)
                   if (resultado == 1):
                       ganhador1total += 1
                       vitorias_jogador1.append(ganhador1total)
                       vitorias_jogador2.append(ganhador2total)
                       velhas.append(velhatotal)
                       break
                   elif (resultado == 2):
                       ganhador2total += 1
                       vitorias_jogador1.append(ganhador1total)
                       vitorias_jogador2.append(ganhador2total)
                       velhas.append(velhatotal)
                       break
                   elif (resultado == 0):
                       velhatotal += 1
                       vitorias_jogador1.append(ganhador1total)
                       vitorias_jogador2.append(ganhador2total)
                       velhas.append(velhatotal)
                       break


                   print("Vez da maquina 2:")
                   maquinaimpossivel(vet, -1, cont, vetorjogadas, 0)


                   cont += 1


                   resultado = verificarganhador(vet)
                   if (resultado == 1):
                       ganhador1total += 1
                       vitorias_jogador1.append(ganhador1total)
                       vitorias_jogador2.append(ganhador2total)
                       velhas.append(velhatotal)
                       break
                   elif (resultado == 2):
                       ganhador2total += 1
                       vitorias_jogador1.append(ganhador1total)
                       vitorias_jogador2.append(ganhador2total)
                       velhas.append(velhatotal)
                       break
                   elif (resultado == 0):
                       velhatotal += 1
                       vitorias_jogador1.append(ganhador1total)
                       vitorias_jogador2.append(ganhador2total)
                       velhas.append(velhatotal)
                       break


               acabou -= 1
       else:
           while (acabou != 0):
               vet = []
               vetorjogadas = []
               vet = preencherVetor(vet)
               cont = 0
               j = 0


               while True:


                   print("Vez da maquina 1:")
                   maquinaimpossivel(vet, 1, cont, vetorjogadas, 0)
                   cont += 1


                   resultado = verificarganhador(vet)
                   if (resultado == 1):
                       ganhador1total += 1
                       vitorias_jogador1.append(ganhador1total)
                       vitorias_jogador2.append(ganhador2total)
                       velhas.append(velhatotal)
                       break
                   elif (resultado == 2):
                       ganhador2total += 1
                       vitorias_jogador1.append(ganhador1total)
                       vitorias_jogador2.append(ganhador2total)
                       velhas.append(velhatotal)
                       break
                   elif (resultado == 0):
                       velhatotal += 1
                       vitorias_jogador1.append(ganhador1total)
                       vitorias_jogador2.append(ganhador2total)
                       velhas.append(velhatotal)
                       break


                   print("Vez da maquina 2:")
                   posicao2 = random.randint(1, 9)
                   posicao2 = posicao2 - 1
                   vetorjogadas.insert(j, maquina(vet, posicao2, -1, 1))
                   j += 1
                   cont += 1


                   resultado = verificarganhador(vet)
                   if (resultado == 1):
                       ganhador1total += 1
                       vitorias_jogador1.append(ganhador1total)
                       vitorias_jogador2.append(ganhador2total)
                       velhas.append(velhatotal)
                       break
                   elif (resultado == 2):
                       ganhador2total += 1
                       vitorias_jogador1.append(ganhador1total)
                       vitorias_jogador2.append(ganhador2total)
                       velhas.append(velhatotal)
                       break
                   elif (resultado == 0):
                       velhatotal += 1
                       vitorias_jogador1.append(ganhador1total)
                       vitorias_jogador2.append(ganhador2total)
                       velhas.append(velhatotal)
                       break


               acabou -= 1


       print("0 primeiro ganhou: ",ganhador1total)
       print("0 segundo ganhou: ", ganhador2total)
       print("Velha: ", velhatotal)
       print("\n")
       mostrargrafico(vitorias_jogador1, vitorias_jogador2, velhas, numeropartidas)


   elif(opcao == 6):
       ganhador1total = 0
       ganhador2total = 0
       velhatotal = 0
       vitorias_jogador1 = []
       vitorias_jogador2 = []
       velhas = []


       instrucao()
       numeropartidas = int(input("Numero de partidas:"))
       acabou = numeropartidas


       while (acabou != 0):
           vet = []
           vetorjogadas = [8]
           vetorjogadas2 = [8]
           vet = preencherVetor(vet)
           cont = 0
           j = 0
           k = 0


           while True:


               print("Vez da maquina 1:")
               vetorjogadas.insert(j, maquinaimpossivel(vet, 1, cont, vetorjogadas2, 1))
               j += 1


               cont += 1


               resultado = verificarganhador(vet)
               if (resultado == 1):
                   ganhador1total += 1
                   vitorias_jogador1.append(ganhador1total)
                   vitorias_jogador2.append(ganhador2total)
                   velhas.append(velhatotal)
                   break
               elif (resultado == 2):
                   ganhador2total += 1
                   vitorias_jogador1.append(ganhador1total)
                   vitorias_jogador2.append(ganhador2total)
                   velhas.append(velhatotal)
                   break
               elif (resultado == 0):
                   velhatotal += 1
                   vitorias_jogador1.append(ganhador1total)
                   vitorias_jogador2.append(ganhador2total)
                   velhas.append(velhatotal)
                   break


               print("Vez da maquina 2:")
               vetorjogadas2.insert(k, maquinaimpossivel(vet, -1, cont, vetorjogadas, 1))
               k += 1


               cont += 1


               resultado = verificarganhador(vet)
               if (resultado == 1):
                   ganhador1total += 1
                   vitorias_jogador1.append(ganhador1total)
                   vitorias_jogador2.append(ganhador2total)
                   velhas.append(velhatotal)
                   break
               elif (resultado == 2):
                   ganhador2total += 1
                   vitorias_jogador1.append(ganhador1total)
                   vitorias_jogador2.append(ganhador2total)
                   velhas.append(velhatotal)
                   break
               elif (resultado == 0):
                   velhatotal += 1
                   vitorias_jogador1.append(ganhador1total)
                   vitorias_jogador2.append(ganhador2total)
                   velhas.append(velhatotal)
                   break


           acabou -= 1


       print("0 primeiro ganhou: ", ganhador1total)
       print("0 segundo ganhou: ", ganhador2total)
       print("Velha: ", velhatotal)
       print("\n")
       mostrargrafico(vitorias_jogador1, vitorias_jogador2, velhas, numeropartidas)


   elif (opcao == 7):
       ganhador1total = 0
       ganhador2total = 0
       velhatotal = 0
       vitorias_jogador1 = []
       vitorias_jogador2 = []
       velhas = []


       instrucao()
       inicia = int(input("Quem inicia o jogo: 1 - Maquina Impossivel ou 2 - Agente inteligente "))
       numeropartidas = int(input("Numero de partidas:"))
       acabou = numeropartidas


       if (inicia == 1):
           while (acabou != 0):
               vet = []
               linhasusadas = []
               vetorjogadas = []
               vet = preencherVetor(vet)
               cont = 0
               j = 0


               while True:


                   #print("Vez da maquina 1:")


                   maquinaimpossivel(vet, 1, cont, vetorjogadas, 0)
                   cont += 1


                   resultado = verificarganhador(vet)
                   if (resultado == 1):
                       ganhador1total += 1
                       vitorias_jogador1.append(ganhador1total)
                       vitorias_jogador2.append(ganhador2total)
                       velhas.append(velhatotal)
                       ultimapartida = (numeropartidas - acabou) + 1


                       for k in range(len(linhasusadas)):
                           conhecimento[linhasusadas[k]][10] -= 10


                       limpar(conhecimento)
                       break
                   elif (resultado == 2):
                       ganhador2total += 1
                       vitorias_jogador1.append(ganhador1total)
                       vitorias_jogador2.append(ganhador2total)
                       velhas.append(velhatotal)


                       for k in range(len(linhasusadas)):
                           conhecimento[linhasusadas[k]][10] += 2
                       break
                   elif (resultado == 0):
                       velhatotal += 1
                       vitorias_jogador1.append(ganhador1total)
                       vitorias_jogador2.append(ganhador2total)
                       velhas.append(velhatotal)


                       for k in range(len(linhasusadas)):
                           conhecimento[linhasusadas[k]][10] += 1
                       break


                   #print("Vez da maquina 2:")
                   vetorjogadas.insert(j, agente(vet, -1, 1, linhasusadas, conhecimento))
                   j += 1


                   cont += 1


                   resultado = verificarganhador(vet)
                   if (resultado == 1):
                       ganhador1total += 1
                       vitorias_jogador1.append(ganhador1total)
                       vitorias_jogador2.append(ganhador2total)
                       velhas.append(velhatotal)
                       ultimapartida = (numeropartidas - acabou) + 1


                       for k in range(len(linhasusadas)):
                           conhecimento[linhasusadas[k]][10] -= 10


                       limpar(conhecimento)
                       break
                   elif (resultado == 2):
                       ganhador2total += 1
                       vitorias_jogador1.append(ganhador1total)
                       vitorias_jogador2.append(ganhador2total)
                       velhas.append(velhatotal)


                       for k in range(len(linhasusadas)):
                           conhecimento[linhasusadas[k]][10] += 2
                       break
                   elif (resultado == 0):
                       velhatotal += 1
                       vitorias_jogador1.append(ganhador1total)
                       vitorias_jogador2.append(ganhador2total)
                       velhas.append(velhatotal)


                       for k in range(len(linhasusadas)):
                           conhecimento[linhasusadas[k]][10] += 1
                       break


               acabou -= 1
       else:
           while (acabou != 0):
               vet = []
               linhasusadas = []
               vetorjogadas = []
               vet = preencherVetor(vet)
               cont = 0
               j = 0


               while True:


                   #print("Vez da maquina 1:")
                   vetorjogadas.insert(j, agente(vet, 1, 1, linhasusadas, conhecimento))
                   j+=1
                   cont += 1


                   resultado = verificarganhador(vet)
                   if (resultado == 1):
                       ganhador1total += 1
                       vitorias_jogador1.append(ganhador1total)
                       vitorias_jogador2.append(ganhador2total)
                       velhas.append(velhatotal)


                       for k in range(len(linhasusadas)):
                           conhecimento[linhasusadas[k]][10] += 2
                       break


                   elif (resultado == 2):
                       ganhador2total += 1
                       vitorias_jogador1.append(ganhador1total)
                       vitorias_jogador2.append(ganhador2total)
                       velhas.append(velhatotal)
                       ultimapartida = (numeropartidas - acabou) + 1
                       for k in range(len(linhasusadas)):
                           conhecimento[linhasusadas[k]][10] -= 10


                       limpar(conhecimento)
                       break
                   elif (resultado == 0):
                       velhatotal += 1
                       vitorias_jogador1.append(ganhador1total)
                       vitorias_jogador2.append(ganhador2total)
                       velhas.append(velhatotal)
                       for k in range(len(linhasusadas)):
                           conhecimento[linhasusadas[k]][10] += 1
                       break


                   #print("Vez da maquina 2:")


                   maquinaimpossivel(vet, -1, cont, vetorjogadas, 0)
                   cont += 1


                   resultado = verificarganhador(vet)
                   if (resultado == 1):
                       ganhador1total += 1
                       vitorias_jogador1.append(ganhador1total)
                       vitorias_jogador2.append(ganhador2total)
                       velhas.append(velhatotal)


                       for k in range(len(linhasusadas)):
                           conhecimento[linhasusadas[k]][10] += 2
                       break
                   elif (resultado == 2):
                       ganhador2total += 1
                       vitorias_jogador1.append(ganhador1total)
                       vitorias_jogador2.append(ganhador2total)
                       velhas.append(velhatotal)
                       ultimapartida = (numeropartidas - acabou) + 1
                       for k in range(len(linhasusadas)):
                           conhecimento[linhasusadas[k]][10] -= 10


                       limpar(conhecimento)
                       break
                   elif (resultado == 0):
                       velhatotal += 1
                       vitorias_jogador1.append(ganhador1total)
                       vitorias_jogador2.append(ganhador2total)
                       velhas.append(velhatotal)
                       for k in range(len(linhasusadas)):
                           conhecimento[linhasusadas[k]][10] += 1
                       break


               acabou -= 1


       print("0 primeiro ganhou: ", ganhador1total)
       print("0 segundo ganhou: ", ganhador2total)
       print("Velha: ", velhatotal)
       print("\n")
       print("Ultima partida perdida:", ultimapartida)
       escrever_em_txt(conhecimento, "BASEDEDADOS")
       mostrargrafico(vitorias_jogador1, vitorias_jogador2, velhas, numeropartidas)




   elif(opcao == 8):
       ganhador1total = 0
       ganhador2total = 0
       velhatotal = 0
       vitorias_jogador1 = []
       vitorias_jogador2 = []
       velhas = []


       instrucao()
       inicia = int(input("Quem inicia o jogo: 1 - Maquina Aleatorio ou 2 - Agente inteligente "))
       numeropartidas = int(input("Numero de partidas:"))
       acabou = numeropartidas


       if (inicia == 1):
           while (acabou != 0):
               vet = []
               linhasusadas = []
               vetorjogadas = []
               vet = preencherVetor(vet)
               cont = 0
               j = 0


               while True:


                   #print("Vez da maquina 1:")


                   posicao2 = random.randint(1, 9)
                   posicao2 = posicao2 - 1
                   maquina(vet, posicao2, 1, 0)
                   cont += 1


                   resultado = verificarganhador(vet)
                   if (resultado == 1):
                       ganhador1total += 1
                       vitorias_jogador1.append(ganhador1total)
                       vitorias_jogador2.append(ganhador2total)
                       velhas.append(velhatotal)
                       ultimapartida = (numeropartidas - acabou) + 1


                       for k in range(len(linhasusadas)):
                           conhecimento[linhasusadas[k]][10] -= 10


                       limpar(conhecimento)
                       break
                   elif (resultado == 2):
                       ganhador2total += 1
                       vitorias_jogador1.append(ganhador1total)
                       vitorias_jogador2.append(ganhador2total)
                       velhas.append(velhatotal)


                       for k in range(len(linhasusadas)):
                           conhecimento[linhasusadas[k]][10] += 2
                       break
                   elif (resultado == 0):
                       velhatotal += 1
                       vitorias_jogador1.append(ganhador1total)
                       vitorias_jogador2.append(ganhador2total)
                       velhas.append(velhatotal)


                       for k in range(len(linhasusadas)):
                           conhecimento[linhasusadas[k]][10] += 1
                       break


                   #print("Vez da maquina 2:")
                   agente(vet, -1, 0, linhasusadas, conhecimento)


                   cont += 1


                   resultado = verificarganhador(vet)
                   if (resultado == 1):
                       ganhador1total += 1
                       vitorias_jogador1.append(ganhador1total)
                       vitorias_jogador2.append(ganhador2total)
                       velhas.append(velhatotal)
                       ultimapartida = (numeropartidas - acabou) + 1


                       for k in range(len(linhasusadas)):
                           conhecimento[linhasusadas[k]][10] -= 10


                       limpar(conhecimento)


                       break
                   elif (resultado == 2):
                       ganhador2total += 1
                       vitorias_jogador1.append(ganhador1total)
                       vitorias_jogador2.append(ganhador2total)
                       velhas.append(velhatotal)


                       for k in range(len(linhasusadas)):
                           conhecimento[linhasusadas[k]][10] += 2
                       break
                   elif (resultado == 0):
                       velhatotal += 1
                       vitorias_jogador1.append(ganhador1total)
                       vitorias_jogador2.append(ganhador2total)
                       velhas.append(velhatotal)


                       for k in range(len(linhasusadas)):
                           conhecimento[linhasusadas[k]][10] += 1
                       break


               acabou -= 1
       else:
           while (acabou != 0):
               vet = []
               linhasusadas = []
               vetorjogadas = []
               vet = preencherVetor(vet)
               cont = 0


               while True:


                   #print("Vez da maquina 1:")
                   agente(vet, 1, 0, linhasusadas, conhecimento)
                   cont += 1


                   resultado = verificarganhador(vet)
                   if (resultado == 1):
                       ganhador1total += 1
                       vitorias_jogador1.append(ganhador1total)
                       vitorias_jogador2.append(ganhador2total)
                       velhas.append(velhatotal)


                       for k in range(len(linhasusadas)):
                           conhecimento[linhasusadas[k]][10] += 2


                       break


                   elif (resultado == 2):
                       ganhador2total += 1
                       vitorias_jogador1.append(ganhador1total)
                       vitorias_jogador2.append(ganhador2total)
                       velhas.append(velhatotal)
                       ultimapartida = (numeropartidas - acabou) + 1


                       for k in range(len(linhasusadas)):
                           conhecimento[linhasusadas[k]][10] -= 10


                       limpar(conhecimento)
                       break
                   elif (resultado == 0):
                       velhatotal += 1
                       vitorias_jogador1.append(ganhador1total)
                       vitorias_jogador2.append(ganhador2total)
                       velhas.append(velhatotal)


                       for k in range(len(linhasusadas)):
                           conhecimento[linhasusadas[k]][10] += 1


                       break


                   #print("Vez da maquina 2:")


                   posicao2 = random.randint(1, 9)
                   posicao2 = posicao2 - 1
                   maquina(vet, posicao2, -1, 0)


                   resultado = verificarganhador(vet)
                   if (resultado == 1):
                       ganhador1total += 1
                       vitorias_jogador1.append(ganhador1total)
                       vitorias_jogador2.append(ganhador2total)
                       velhas.append(velhatotal)


                       for k in range(len(linhasusadas)):
                           conhecimento[linhasusadas[k]][10] += 2


                       break
                   elif (resultado == 2):
                       ganhador2total += 1
                       vitorias_jogador1.append(ganhador1total)
                       vitorias_jogador2.append(ganhador2total)
                       velhas.append(velhatotal)
                       ultimapartida = (numeropartidas - acabou) + 1


                       for k in range(len(linhasusadas)):
                           conhecimento[linhasusadas[k]][10] -= 10


                       limpar(conhecimento)
                       break
                   elif (resultado == 0):
                       velhatotal += 1
                       vitorias_jogador1.append(ganhador1total)
                       vitorias_jogador2.append(ganhador2total)
                       velhas.append(velhatotal)


                       for k in range(len(linhasusadas)):
                           conhecimento[linhasusadas[k]][10] += 1


                       break


               acabou -= 1


       print("0 primeiro ganhou: ", ganhador1total)
       print("0 segundo ganhou: ", ganhador2total)
       print("Velha: ", velhatotal)
       print("Ultima partida perdida:", ultimapartida)
       print("\n")
       escrever_em_txt(conhecimento, "BASEDEDADOS")
       mostrargrafico(vitorias_jogador1, vitorias_jogador2, velhas, numeropartidas)




   elif(opcao==9):
       ganhador1total = 0
       ganhador2total = 0
       velhatotal = 0
       vitorias_jogador1 = []
       vitorias_jogador2 = []
       velhas = []


       instrucao()


       numeropartidas = int(input("Numero de partidas:"))
       acabou = numeropartidas


       while (acabou != 0):
           vet = []
           linhasusadas = []
           linhasusadas2 = []
           vet = preencherVetor(vet)


           while True:


               #print("Vez da maquina 1:")
               agente(vet, 1, 0, linhasusadas, conhecimento)
               # time.sleep(1)


               resultado = verificarganhador(vet)
               if (resultado == 1):
                   ganhador1total += 1
                   vitorias_jogador1.append(ganhador1total)
                   vitorias_jogador2.append(ganhador2total)
                   velhas.append(velhatotal)




                   for k in range(len(linhasusadas)):
                       conhecimento[linhasusadas[k]][10] += 2


                   for k in range(len(linhasusadas2)):
                       conhecimento2[linhasusadas2[k]][10] -= 10


                   limpar(conhecimento)
                   limpar(conhecimento2)


                   break
               elif (resultado == 2):
                   ganhador2total += 1
                   vitorias_jogador1.append(ganhador1total)
                   vitorias_jogador2.append(ganhador2total)
                   velhas.append(velhatotal)


                   for k in range(len(linhasusadas)):
                       conhecimento[linhasusadas[k]][10] -= 10


                   for k in range(len(linhasusadas2)):
                       conhecimento2[linhasusadas2[k]][10] += 2


                   limpar(conhecimento)
                   limpar(conhecimento2)


                   break
               elif (resultado == 0):
                   velhatotal += 1
                   vitorias_jogador1.append(ganhador1total)
                   vitorias_jogador2.append(ganhador2total)
                   velhas.append(velhatotal)


                   for k in range(len(linhasusadas)):
                       conhecimento[linhasusadas[k]][10] += 1


                   for k in range(len(linhasusadas2)):
                       conhecimento2[linhasusadas2[k]][10] += 1


                   break


               #rint("Vez da maquina 2:")
               agente(vet, -1, 0, linhasusadas2, conhecimento2)
               # time.sleep(1)




               resultado = verificarganhador(vet)
               if (resultado == 1):
                   ganhador1total += 1
                   vitorias_jogador1.append(ganhador1total)
                   vitorias_jogador2.append(ganhador2total)
                   velhas.append(velhatotal)


                   for k in range(len(linhasusadas)):
                       conhecimento[linhasusadas[k]][10] += 2


                   for k in range(len(linhasusadas2)):
                       conhecimento2[linhasusadas2[k]][10] -= 10


                   limpar(conhecimento)
                   limpar(conhecimento2)


                   break
               elif (resultado == 2):
                   ganhador2total += 1
                   vitorias_jogador1.append(ganhador1total)
                   vitorias_jogador2.append(ganhador2total)
                   velhas.append(velhatotal)


                   for k in range(len(linhasusadas)):
                       conhecimento[linhasusadas[k]][10] -= 10


                   for k in range(len(linhasusadas2)):
                       conhecimento2[linhasusadas2[k]][10] += 2


                   limpar(conhecimento)
                   limpar(conhecimento2)


                   break
               elif (resultado == 0):
                   velhatotal += 1
                   vitorias_jogador1.append(ganhador1total)
                   vitorias_jogador2.append(ganhador2total)
                   velhas.append(velhatotal)


                   for k in range(len(linhasusadas)):
                       conhecimento[linhasusadas[k]][10] += 1


                   for k in range(len(linhasusadas2)):
                       conhecimento2[linhasusadas2[k]][10] += 1


                   break


           acabou -= 1


       print("0 primeiro ganhou: ", ganhador1total)
       print("0 segundo ganhou: ", ganhador2total)
       print("Velha: ", velhatotal)
       print("\n")


       mostrargrafico(vitorias_jogador1, vitorias_jogador2, velhas, numeropartidas)


       print(len(conhecimento))
       print(len(conhecimento2))
       for linha in conhecimento:
           print(linha)
       print("conhecimento 2 ----------------------------")
       for linha in conhecimento2:
           print(linha)



