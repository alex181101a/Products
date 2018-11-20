import os # operating system
product = []
#讀取檔案
def read_file(filename):

	with open(filename, "r", encoding = 'utf-8') as f:    #讀取檔案,寫入檔案 讀取檔案 都有編碼問題
		for line in f:
			if '商品, 價格' in line:               #continue 跟break一樣只可以寫在loop裡,continue為跳到下一迴的意思(還在迴圈內)<break為結束迴圈
				continue
			name, price = line.strip().split(',')  #若要存到3等分或4等分以上可設定3或4等分以上參數，先去除\n換行符號(strip),在分割('逗點')(split),分割完後為清單
			product.append([name, price])		   #將name 及price存到product 清單內
			#	s = line.strip().split(',')            #先去除\n換行符號,在分割('逗點'),分割完後為清單
			#	print(s)
	return product                                 #有return 可以回存資料


#讓使用者輸入
def user_input(product):
	while True:
		name = input('Product name is: ')
		if name == 'q':
		    break
		price = input('Price is: ')
		price = int(price)
		product.append([name,price])
	print(product)
	return product

#印出所有購買紀錄
def print_product(product):
	for p in product:
		print(p)
		print(p[0],'的價格是', p[1])

#寫入檔案
def write_file(filename, product):
	with open(filename, 'w', encoding = 'utf-8') as f:     #encoding = 'utf-8' 通用編碼,寫入檔案及讀取檔案都需要邊碼
		f.write('商品, 價格\n')         #也可以寫成 '商品' + ',' + '價格\n'
		for p in product:
			f.write(p[0] + ',' + str(p[1]) + '\n')    #csv 檔通常以逗點區隔; 字串 用 +  合併





                        #主程式

def main(product):

	filename = 'product.csv'
	if os.path.isfile(filename):     #相對路徑
		print('yes')
		product = read_file(filename) 
	else: 
		print('Not found....')

	product = user_input(product)
	print_product(product)
	write_file(filename, product)

main(product)

