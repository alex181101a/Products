product = []
while True:
	name = input('Product name is: ')
	if name == 'q':
	    break
	price = input('Price is: ')
	price = int(price)
	product.append([name,price])
print(product)

for p in product:
	print(p)
	print(p[0],'的價格是', p[1])

with open("product.csv", 'w', encoding = 'utf-8') as f:     #encoding = 'utf-8' 通用編碼
	f.write('商品' + ',' + '價格\n')         #也可以寫成 '商品, 價格\n'
	for p in product:
		f.write(p[0] + ',' + str(p[1]) + '\n')    #csv 檔通常以逗點區隔; 字串 用 +  合併
