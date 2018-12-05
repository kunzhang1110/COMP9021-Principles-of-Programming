record = []

for i in range(100,1000):
	for j in range(10,100):
			three_list = [int(x) for x in str(i)]
			two_list = [int(y) for y in str(j)]
			row_1_num = str(i * two_list[1])
			row_2_num = str(i * two_list[0])			

			row_1 = [int(x) for x in list(row_1_num)]
			row_2 = [int(y) for y in list(row_2_num)]
			

			product = i*j

			if len(row_1) != 4 or len (row_2) != 3:
				continue

			if product > 9999:
				continue
				
			product_list = [int(x) for x in str(product)]

			col_1 = three_list[2] + two_list[1] + row_1[3] + product_list[3]
			col_2 = three_list[1] + two_list[0] + row_1[2] + row_2[2] + product_list[2]
			if col_1 != col_2:
				continue
			col_3 = three_list[0] + row_1[1] + row_2[1] + product_list[1]
			if col_2 != col_3:
				continue
			col_4 = row_1[0] + row_2[0] + product_list[0]
			if col_3 != col_4:
				continue
			record.append((i, j, product, col_4))

for i, j, prd, s in record:
	print("{} * {} = {}, all columns adding up to {}".format(i, j, prd, s))