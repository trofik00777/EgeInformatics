def umnozh_list(a):
	k = 1
	for i in a:
		k *= i
	return k


print("hello")
n = int(input())
data = []
for i in range(n):
	data.append(int(input()))
# s = "".join([str(i) for i in data])
# s = s.split("0")
indexes_of_0 = [i for i in range(len(data)) if data[i] == 0] + [len(data)]
predict_of_undatas = []
for i in range(len(indexes_of_0)):  # take data[k1+1:k2]
	if i > 0:
		k1 = indexes_of_0[i - 1]
	else:
		k1 = -1
	k2 = indexes_of_0[i]
	undata = data[k1 + 1:k2]
	count_minuses = sum(1 for j in undata if j < 0)
	if count_minuses % 2 == 0:
		predict_of_undatas.append(umnozh_list(undata))
	else:
		indexes_of_minus1 = [j for j in range(len(undata)) if undata[j] < 0]
		predict_of_undatas.append(umnozh_list(undata[:indexes_of_minus1[-1]]))
		predict_of_undatas.append(umnozh_list(undata[indexes_of_minus1[0] + 1:]))
print(predict_of_undatas)
print(max(predict_of_undatas))
