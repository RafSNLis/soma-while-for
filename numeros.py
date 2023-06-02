#while
def soma_while(): 
     soma = 0
     numero = int(input("digite o número 0 para sair "))

     while numero != 0:
          soma += numero
          numero = int(input("digite o número 0 para sair ")) 

          print("a soma dos números é ", soma)


#for
def soma_for():
    soma = 0 
    quantidade = int(input("digite quantos números deseja somar "))

    for i in range(quantidade):
        numero = int(input("digite um número "))
        soma += numero 

    print("a soma dos números é", soma) 




#menu
def menu ():
        print("selecione uma opção")
        print("1 para while")
        print("2 para for")
        print("0 para sair")

        escolha = int(input("digite: ")) 


        if(escolha == 1):
            print("você escolheu while")
            soma_while()
         
        elif(escolha == 2):
            print("você escolheu for")
            soma_for()
            
        elif(escolha == 0):
             print("saiu")
             menu()


menu()
    
