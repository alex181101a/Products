#讀取檔案
product = []

with open("product.csv", "r", encoding = 'utf-8') as f:    #讀取檔案,
	for line in f:
		if '商品, 價格' in line:               #continue 跟break一樣只可以寫在loop裡,continue為跳到下一迴的意思(還在迴圈內)<break為結束迴圈
			continue
		name, price = line.strip().split(',')  #若要存到3等分或4等分以上可設定3或4等分以上參數，先去除\n換行符號,在分割('逗點'),分割完後為清單
		product.append([name, price])		   #將name 及price存到product 清單內
	#	s = line.strip().split(',')            #先去除\n換行符號,在分割('逗點'),分割完後為清單
	#	print(s)
print(product)

#讓使用者輸入
while True:
	name = input('Product name is: ')
	if name == 'q':
	    break
	price = input('Price is: ')
	price = int(price)
	product.append([name,price])
print(product)

#印出所以購買紀錄
for p in product:
	print(p)
	print(p[0],'的價格是', p[1])

#寫入檔案
with open("product.csv", 'w', encoding = 'utf-8') as f:     #encoding = 'utf-8' 通用編碼,寫入檔案及讀取檔案都需要邊碼
	f.write('商品, 價格\n')         #也可以寫成 '商品' + ',' + '價格\n'
	for p in product:
		f.write(p[0] + ',' + str(p[1]) + '\n')    #csv 檔通常以逗點區隔; 字串 用 +  合併
