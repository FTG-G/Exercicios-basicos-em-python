#14 - Uma loja de calçados precisa que você desenvolva um sistema de cálculo de descontos.
#Seu algoritmo receberá 3 variáveis: nome_produto, preco e desconto, o preço será em reais
#(R$) e o desconto em percentual. Então, calcule e exiba o preco_final com desconto.
#Por exemplo, para um calçado de 300 reais, com um percentual de desconto de 15:
#Desconto: 300 * 0.15 = 45
#Preço Final: 300 - desconto -> 300 - 45 = 255

nome_produto = str(input("Digite o nome do pruduto: "))
preco = float(input("Digite o preco: "))
desconto = float(input("Digite o desconto: "))

soma = preco * (desconto / 100)

print(f"O preco final é: {preco - soma}")