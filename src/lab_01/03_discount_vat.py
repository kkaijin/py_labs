price = float(input())
discount = float(input())
vat = float(input())

base = price * (1 - discount/100)
vat_amount = base*(vat/100)
total = base+vat_amount

print('База посл скидки:', round(base,2))
print('НДС:', round(vat_amount,2))
print('Итого к оплате:', round(total, 2))