# Version 1
def Lab_3_3_v1()
	record = []
	for i in range(10, 100):
		list_i = [int(x) for x in str(i)]
		if len(set(list_i)) != 2:
			continue
		for j in range(10, 100):
			list_j = [int(x) for x in str(j)] + list_i
			if len(set(list_j)) != 4:
				continue
			for k in range(10, 100):
				list_k = [int(x) for x in str(k)] + list_j
				if len(set(list_k)) != 6:
					continue
				prd = i * j * k
				list_prd =[int(x) for x in str(prd)]
				if set(list_prd) == set(list_k):
					ans = [i, j, k, prd]
					ans.sort()
					if ans not in record:
						record.append(ans)

	for t in record:
		print("{} * {} * {} = {}".format(t[0], t[1], t[2], t[3]))

		
