#Criar um sistema que possui 3 operações deposito, saque, extrato


opcoes = """
            Seja Bem-Vindo Ao Banco - ESCOLHA UMA OPÇÃO
            1 - Depósito
            2 - Saque
            3 - Extrato
            4- Sair
            """

msg_erro = print("Digite um valor valido")

x = int(input(print(opcoes)))

contador_saques = 0
saldo = 0
extrato = []

while x != 4:
        
        if x == 1:
            while True:
                try:
                    valor_deposito = int(input("Informe o Valor a depositar: \n"))
                    if valor_deposito > 0:
                        tipo_operacao = "Depósito"
                        saldo += valor_deposito
                        extrato.append({"Tipo": tipo_operacao,"Valor": valor_deposito})
                        x = int(input(opcoes[38:]))
                        break
                    else:
                        print("Valor Invalido")
                except ValueError:
                    msg_erro
                    
        elif x == 2:
            if contador_saques < 3:
                while True:
                    try:
                        valor_saque = int(input("Informe o Valor do Saque: \n"))
                        if valor_saque <= saldo and valor_saque <= 500:
                            tipo_operacao = "Saque"
                            saldo -= valor_saque
                            extrato.append({"Tipo": tipo_operacao,"Valor": valor_saque})
                            contador_saques += 1
                            x = int(input(opcoes[38:]))
                            break
                        elif valor_saque > 500:
                            print("Valor de saque maior que o permitido por saque")
                            x = int(input(opcoes[38:]))
                            break
                        else:
                            print("Saldo Insuficiente")
                    except ValueError:
                        msg_erro
            else:
                print("Quantidade de Saques atingiu o Limite")
                x = int(input(opcoes[38:]))

        elif x == 3:
             print(f"Seu extrato atual é: {extrato}, {saldo}")
             x = int(input(opcoes[38:]))

print("Saindo Do Sistema...")