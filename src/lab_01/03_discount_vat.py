price = input('price=')
discount = input('discount=')
vat = input('vat=')
price = float(price)
discount = float(discount)
vat = float(vat)

base = price * (1 - discount/100)
vat_amount = base*(vat/100)
total = base+vat_amount

print('База посл скидки:', "{:.2f}".format(round(base,2)))
print('НДС:', "{:.2f}".format(round(vat_amount,2)))
print('Итого к оплате:', "{:.2f}".format(round(total, 2)))