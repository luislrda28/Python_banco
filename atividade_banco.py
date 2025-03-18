LIMITE_SAQUES_DIARIO = 3
saques = 0
saldo = 0
limite = 500
extrato = ""

while True:
    
    escolha = input("""
                
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [c] Sair

    """)

    if escolha == 'd':
        valor = float(input("Digte o valor que gostaria de depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito de R$ {valor:.2f}\n"
        else:
            print("Valor inválido! Tente novamente.")

    elif escolha == 's':
        valor = float(input("Informe o valor que deseja sacar: "))
        
        passou_saldo = valor > saldo
        passou_limite = valor > limite
        passou_saques = saques >= LIMITE_SAQUES_DIARIO

        if passou_saldo:
            print("Você não tem saldo suficiente. Tente novamente com outro valor.")

        elif passou_limite:
            print("Seu limite de saque foi excedido. Tente novamente.")

        elif passou_saques:
            print("Você ja realizou 3 saques no dia de hoje. Tente novamente no dia seguinte.")

        elif valor > 0:
            saldo -= valor
            extrato = f"Saque: R$ {valor:.2f}\n"
            saques += 1

        else:
            print("Operação com falhas! Tente novamente.")
    
    elif escolha == 'e':
        print(f"""
           / ================ EXTRATO ================ 
           | Não foram realizadas transações."""if not extrato else extrato, f"""             
           | Saldo: R$ {saldo:.2f}
           \ =========================================
         """)
    
    elif escolha == 'c':
        break

    else:
        print("Operação inválida! Tente novamente.")

            
        

