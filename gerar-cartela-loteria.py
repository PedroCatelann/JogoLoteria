import random

#MEGA SENA     1-60   CARTELA TEM 6 NUMEROS
#LOTO FACIL    1-25   CARTELA TEM 15
#QUINA         1-80   CARTELA TEM 5 NUMEROS

def megasena():
    
    x = []    
    i = 1    
    while i <= 6:
        sorteado = int(random.random()*15)
        if sorteado not in x and sorteado != 0:
            x.append(sorteado)
            
            i+=1
    x = [str(y+100)[1:3] for y in x]
    x.sort()
    return x

def lotofacil():
    x = []
    i = 1    
    while i <= 15:
        sorteado = int(random.random()*25)
        if sorteado not in x and sorteado != 0:
            x.append(sorteado)
            i+=1
        
    x = [str(y+100)[1:3] for y in x]
    x.sort()
    return x

def quina():
    x = []    
    i = 1    
    while i <= 5:
        sorteado = int(random.random()*80)
        if sorteado not in x and sorteado != 0:
            x.append(sorteado)
            i+=1
    x = [str(y+100)[1:3] for y in x]
    x.sort()
    return x
            

if __name__ == "__main__":

    continua = "S"

    while continua != "N":
        tipo_loteria = int(input("1 - MEGA SENA\n2 - LOTO FACIL\n3 - QUINA\nDigite sua opcao: "))
        
        if tipo_loteria == 1:
            var = int(input("Digite quantas vezes vc deseja gerar: "))
            for x in range(0,var):
                jogo = (" ".join(megasena()))
                print("\n",jogo)
            continua = input("\nDeseja continuar: (S/N)")

        if tipo_loteria == 2:
            var = int(input("Digite quantas vezes vc deseja gerar: "))
            for x in range(0,var):
                jogo = (" ".join(megasena()))
                print("\n",jogo)
            continua = input("\nDeseja continuar: (S/N)")
        
        if tipo_loteria == 3:
            var = int(input("Digite quantas vezes vc deseja gerar: "))
            for x in range(0,var):
                jogo = (" ".join(megasena()))
                print("\n",jogo)
            continua = input("\nDeseja continuar? (S/N): ")
        
    
    

