#Oii prof. Fraan. Só queria deixar um recadinho de agradecimento. Tive somente uma aula presencialmente com você, então é provavel que não lembre de mim, mas só queria falar que eis uma exelente profissional e uma incrivel teacher, vamos todos sentir muito sua falta!!! Beijão
#Cores para dar uma enfeitada no terminal
RED   = "\033[1;31m"  
RESET = "\033[0;0m"

saldoCliente=0
cadastro=0
#Criando a lista para armazenar dados do cliente
lNomeCliente=[]
lSobrenomeCliente=[]
lCpfCliente=[]
lEmailCliente=[]
lTelefoneCliente=[]
lSenhaCliente=[]

#Criando listas para armazenar dados da conta do cliente
lDeposito=[]
lSacar=[]

#Função para dar espaçamento no menu
def linhas():
    print("-"*35)

nomeIncio=input("Insira seu nome: ")
linhas()
print("Olá", nomeIncio, "seja bem-vindo ao Banco Digital i2137, é um prazer recebe-lo(a).")
print("1-Quero me cadastrar\n2-Conhecer o Banco Digital i2137\n3-Sair")
linhas()
#AQUI ESTÁ TODAS A VALIDAÇÕES
#Validando o nome para que tenha pelo menos 3 letras
def validaNome(nomeCliente):
    while (len(nomeCliente)<3): 
        print(RED+"Seu nome deve conter mais que 3 letras"+RESET)
        nomeCliente=input("Informe seu nome novamente: ")
    
#Validando o sobrenome para que tenha pelo menos 3 letras
def validaSobrenome(sobrenomeCliente):
    while (len(sobrenomeCliente)<3): 
        print(RED +"Seu sobrenome deve conter mais que 3 letras"+ RESET)
        sobrenomeCliente=input("Informe seu sobrenome novamente: ")

import re
#Validando email para que tenha pelo menos um caracter
def validaemail(emailCliente):
    regex=re.compile('@')
    if (regex.search(emailCliente)==None):
        print(RED+"Email invalido"+RESET)
        emailCliente=input("Seu email não se encaixa nos padrões globais. \nInsira seu email novamente com esse termo '@hotmail.com': ")

#validando a senha para que tenha pelo menos 5 digitos
#Professora, tentei colocar um .isalnum() para verificar se todos os caracteres são alfanúmerico ou tudo letra ou tudo número, mas essa validação não deu certo
def validaSenha(senhaCliente):
    while (len(senhaCliente)<5):
        print(RED+"Sua senha deve ter pelo menos 5 caracteres"+RESET)   
        senhaCliente=int(input("Informe sua senha novamente: "))  

#Validações da conta do cliente
def validadeposito(depositoCliente):
    while True:
        if depositoCliente.isnumeric():
            saldoCliente=saldoCliente+depositoCliente
            break
        else:
            print(RED+"Esse campo aceita somente caracteres numéricos."+RESET)
            depositoCliente=(input("Insire novamente: "))

def validaSaque(sacarCliente):
    saldoCliente=saldoCliente-sacarCliente
    if saldoCliente<0:
        print(RED+"Você não possui saldo em sua conta para efetuar um saque"+RESET)


def validaSaldo():
    saldoConta=depositoCliente+saldoConta

def validaTranferencia():
    if saldoCliente<0:
        print("Você não possui saldo em sua conta para efetuar a transferencia")
def menuPrincipal():
    menuPrincipal=input("Conte-nos o que deseja fazer: ")
    #Pedindo para o cliente informar seus dados
    if menuPrincipal=='1':
        nomeCliente=(input("Informe seu nome: "))
        validaNome(nomeCliente)        
        sobrenomeCliente=(input("Informe seu Sobrenome: "))
        validaSobrenome(sobrenomeCliente)      
        cpfCliente=int(input("Informe seu CPF: "))   
        emailCliente=(input("Informe seu E-mail: ")) 
        validaemail(emailCliente)
        numeroCliente=int(input("Informe seu número de telefone: "))   
        senhaCliente=(input("Informe uma senha de segurança: "))
        validaSenha(senhaCliente)
        #Inserindo dados nas listas
        lNomeCliente.append(nomeCliente)
        lSobrenomeCliente.append(sobrenomeCliente)
        lCpfCliente.append(cpfCliente)
        lEmailCliente.append(emailCliente)
        lTelefoneCliente.append(numeroCliente)
        lSenhaCliente.append(senhaCliente)
        linhas()
        #Menu de operações básicas
        print("\nBem-Vindo ao nosso Banco Sr.",nomeCliente," agora você é nosso parceiro. Aqui está seus dados do cadastro:" )
        print("Seu nome:",lNomeCliente[0],lSobrenomeCliente[0],"\nSeu CPF:",lCpfCliente[0],"\nSeu E-mail:",lEmailCliente[0],"\nSeu telefone:",lTelefoneCliente,"\nSua senha de segurança:",lSenhaCliente[0])
        linhas()
        print("4-Quero depositar\n5-Quero sacar\n6-Quero conferir saldo\n7-Quero transferir\n8-Quero encerrar minha conta")
        linhas()
        menuOperacoes=input("O que deseja fazer: ")
        if menuOperacoes=='4':
            depositoCliente=input("Qual o valor que você gostaria de depositar Sr. "+str(nomeCliente)+": ")
            validadeposito(depositoCliente)
            lDeposito.append(depositoCliente)
            print(lDeposito[0])
    
        if menuOperacoes=='5':
            sacarCliente=input("Qual valor você gostaria de sacar: ")
            validaSaque(sacarCliente)
            lSacar.append(sacarCliente)
    
        if menuOperacoes=='6':
           print("Seu saldo é de:",saldoCliente)
           validaSaldo()
    
        if menuOperacoes=='7':
           print("Qual valor você deseja transferir: ")
           validaTranferencia()

        if menuOperacoes=='8':
           encerrarConta=input("Você deseja encerrar sua conta Sr. "+str(nomeCliente)+"? (Sim\Não)")
           if encerrarConta=='Sim':
               print("Nós da Banco Digital i2137 agradecemos pela preferência, tenha um bom dia!")
           if encerrarConta=='Não':
               menuOperacoes()
                


        


        
    

    
        










