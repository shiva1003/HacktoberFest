def countingSort(arr, exp1):
	n = len(arr)
	output = [0] * (n)
	c = [0] * (10)
	for i in range(0, n):
		ind = arr[i] // exp1
		c[ind % 10] += 1
	for i in range(1, 10):
		c[i] += c[i - 1]
	i = n - 1
	while i >= 0:
		ind = arr[i] // exp1
		output[c[ind % 10] - 1] = arr[i]
		c[ind % 10] -= 1
		i -= 1
	i = 0
	for i in range(0, len(arr)):
		arr[i] = output[i]
def radixSort(arr):
	max1 = max(arr)
	exp = 1
	while max1 / exp >= 1:
		countingSort(arr, exp)
		exp *= 10
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radixSort(arr)
for i in range(len(arr)):
	print(arr[i],end=" ")
