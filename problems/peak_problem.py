
def isPeak(arr, n, num, i, j):
	if (i >= 0 and arr[i] > num):
		return False

	if (j < n and arr[j] >= num):
		return False
	return True

def isTrough(arr, n, num, i, j):

	if (i >= 0 and arr[i] < num):
		return False

	if (j < n and arr[j] <= num):
		return False
	return True

def printPeaksTroughs(arr, n):
	peak = []
	trough = []
	for i in range(n):
		if (isPeak(arr, n, arr[i], i - 1, i + 1)):
			peak.append(arr[i])
			print(arr[i], end = " ")
		if (isTrough(arr, n, arr[i], i - 1, i + 1)):
			trough.append(arr[i])
			print(arr[i], end = " ")
	print('Peaks = ', peak)
	print('trough = ', trough)

arr = [5, 10, 5,5,5,5, 7, 4, 3, 5]
n = len(arr)

printPeaksTroughs(arr, n)

