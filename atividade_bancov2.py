def menu():
    menu = """
\n============ MENU ============                      
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [nc] Nova conta
        [nu] Novo usuário        
        [c] Sair
===============================
"""
    return input(menu).strip()

def criar_usuario(usuarios):
    cpf = input(("Informe o seu CPF (somente números): "))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe um usuário com este CPF!")
        return
    
    nome = input("Informe o seu nome completo: ")
    data_nascimento = input("Informe a sua data de nascimento (dd-mm-aa): ")
    endereço = input("Informe o seu endereço (bairro - cidade - estado - pais): ")

    usuarios.append({"nome":nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereço})

    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuario_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_filtrados[0] if usuario_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input(("Informe o seu CPF (somente números): "))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usário não encontrado. Tente criar um usuário primeiro.")

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito:\tR$ {valor:.2f}\n"
        print(f"Depósito realizado com sucesso!")
    else:
        print("Valor inválido! Tente novamente com outro valor.")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, saques, LIMITE_SAQUES_DIARIO):
    passou_saldo = valor > saldo
    passou_limite = valor > limite
    passou_saques = saques >= LIMITE_SAQUES_DIARIO

    if passou_saldo:
        print("\nVocê não tem saldo suficiente. Tente novamente com outro valor.")

    elif passou_limite:
        print("\nSeu limite de saque foi excedido. Tente novamente.")

    elif passou_saques:
        print("\nVocê ja realizou 3 saques no dia de hoje. Tente novamente no dia seguinte.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        saques += 1
        print("Saque realizado com sucesso!")

    else:
        print("Operação com falhas! Tente novamente.")
        
    return saldo, extrato, saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n============= EXTRATO =============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}") 
    print("\n===================================")
    return saldo, extrato     

def main():
    LIMITE_SAQUES_DIARIO = 3
    AGENCIA = '0001'
    
    saques = 0
    saldo = 0
    limite = 500
    extrato = ""
    usuarios = []
    numero_conta = 1

    while True:
        
        escolha = menu()

        if escolha == 'd':
            valor = float(input("Digte o valor que gostaria de depositar: "))

            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif escolha == 's':
            valor = float(input("Informe o valor que deseja sacar: "))
            
            saldo, extrato, saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                saques=saques,
                LIMITE_SAQUES_DIARIO=LIMITE_SAQUES_DIARIO
            )
        
        elif escolha == 'e':
            exibir_extrato(saldo, extrato=extrato)
        
        elif escolha == 'nu':
            criar_usuario(usuarios)

        elif escolha == 'nc':
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                numero_conta += 1
        
        elif escolha == 'c':
            break

        else:
            print("Operação inválida! Tente novamente.")


main()            
        

