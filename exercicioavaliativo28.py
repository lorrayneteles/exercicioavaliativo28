#peça o valor da compra e aplique um desconto de 5% e se o valor for maior que 100 e de 10% se for maior que 500

compra = float(input('Qual o valor da compra?'))
if compra > 100 and compra <= 500:
    desconto = compra * 0.05
elif compra > 500:
    desconto = compra * 0.10
else:
    desconto = 0
total = compra - desconto
print(f'O valor da compra com desconto é R${total:.2f}')
