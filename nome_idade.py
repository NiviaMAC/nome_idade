def calcular_idade():
    # Solicita o nome completo do usuário
    nome = input("Digite seu nome completo: ")

    while True:
        try:
            # Solicita o ano de nascimento
            ano_nascimento = int(input("Digite seu ano de nascimento (entre 1922 e 2021): "))
            
            # Valida o ano de nascimento
            if ano_nascimento < 1922 or ano_nascimento > 2021:
                print("Ano inválido! O ano deve estar entre 1922 e 2021.")
                continue  # Continua o loop para solicitar novamente
            
            # Calcula a idade
            idade = 2022 - ano_nascimento
            
            # Exibe o resultado
            print(f"{nome}, você completou ou completará {idade} anos em 2022.")
            break  # Sai do loop após a entrada correta

        except ValueError:
            print("Entrada inválida! Por favor, digite um número para o ano de nascimento.")

# Chama a função para executar o programa
calcular_idade()