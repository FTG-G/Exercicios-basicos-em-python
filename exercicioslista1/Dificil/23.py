real = float(input("Digite o valor em reais: "))

dolar = (real * 0.19)

impostoreal = (real * (5.38/ 100))
impostodol = (dolar * (5.38 / 100) )

print(f"R$ {real} é equivalente a USD {dolar}")

print(f"O imposto de renda sobre essa transação é de R$ {impostoreal} / USD {impostodol}")