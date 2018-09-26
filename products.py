product = []
while True:
	name = input('Product name is: ')
	if name == 'q':
	    break
	price = input('Price is: ')
	product.append([name,price])
print(product)

for p in product:
	print(p)
	print(p[0],'的價格是', p[1])
