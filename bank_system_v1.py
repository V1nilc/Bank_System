menu =  """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=>  """

saldo = 0
limite = 500
extrato =  ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor para o depósito: R$"))
        
        if valor > 0:
             saldo += valor
             extrato +=  f"Depósito: R${valor:.2f}\n"
        
        else:
            print("\nA Operação falhou! o valor informado é inválido")

    elif opcao == "2":
            valor = float(input("Informe o valor para o saque: R$"))

            if valor > saldo:
                 print("\nA Operação falhou! Saldo insuficiente.\n")
                 print(f"Saldo: R${saldo:.2f}")

            elif valor > limite:
                 print("\nA Operação falhou! O valor de saque excede o limite.\n")

            elif numero_saques >= LIMITE_SAQUES:
                 print("\nA Operação falhou! Número máximo de saques foi excedido.\n")
            
            elif valor > 0:
                 saldo -= valor
                 extrato += f"Saque: R${valor:.2f}\n"
                 numero_saques += 1

            else:
                print("\nOperação falhou! valor informado é inválido.\n") 

    
    elif opcao == "3":
        print("\n ================= EXTRATO =================")
        print("Não foram realizadas movimentações.\n" if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}\n")
        print("==============================================")

    elif opcao == "4":
      
        break
        
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

        