#17 - Crie um programa que solicite ao usuário o valor inicial de um empréstimo, a taxa de
#juros e o tempo de pagamento em meses. Calcule o valor total a ser pago, considerando
#juros simples. (para calcular o juros simples, utilize a fórmula: capital_inicial *
#taxa_de_juros * tempo da aplicação)

valor_inicial = float(input("Digite o valor: "))

taxa_de_juros = float(input("Digite a taxa: "))

tempo = int(input("Digite o tempo em meses: "))
a_taxa = (taxa_de_juros / 100)
valor_a_ser_pago = valor_inicial * a_taxa * tempo

print(f"Digite o valor a ser pago {valor_a_ser_pago}")