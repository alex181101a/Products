product = []
while True:
	name = input('Product name is: ')
	if name == 'q':
	    break
	price = input('Price is: ')
	product.append([name,price])
print(product)

