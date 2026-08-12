def classificar_faixa_etaria():
    idade = int(input("Digite sua idade: "))

    if idade >= 0 and idade <= 12:
        print("Criança")
    elif idade <= 17:
        print("Adolescente")
    elif idade <= 59:
        print("Adulto")
    elif idade >= 60:
        print("Idoso")
    else:
        print("Idade inválida.")

classificar_faixa_etaria()