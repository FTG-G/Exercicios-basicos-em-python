salario_bruto = int(input("Digite seu salario bruto: "))
impostos = int(input("Informe os impostos: "))
plano_saude = int(input("Digite o desconto do plano de saude: "))

descontos = impostos + plano_saude

print("Seu salario liquido é de: ", salario_bruto - descontos,"R$")
