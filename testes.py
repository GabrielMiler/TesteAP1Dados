import random

def numero_de_lados():
    while True:
        x = input("Forneça o tamanho do dado que será rolado (ENTER para sair) : ")
        if x == "":
            break
        if x.isdigit(): 
            if x == "0":
                print("Informe somente números inteiros maiores que 0")
            else:
                return int(x)
        else:
            print("A informação passada não é válida!")
        
def quantidade_de_dados():
    while True:
        x = input("Forneça o número de dados que serão rolados (em branco == 1) :")
        if x == "":
            return 1
        if x.isdigit(): 
            if x == "0":
                print("Informe somente números inteiros maiores que 0")
            else:
                return int(x)
        else:
            print("A informação passada não é válida!") 

def rolar_dados(n, q):
    for rolagem in range(1, q):
        rolagem = random.randint(1, n)
        return rolagem
    





n = numero_de_lados
q = quantidade_de_dados
numero_de_lados()
quantidade_de_dados()
print(rolar_dados(n, q))
