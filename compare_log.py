from collections import defaultdict

files = ['Implementation/logs/wisconsin.log', 'Implementation/logs/clemson.log', 'Implementation/logs/utah.log']

def compare_files():
	file_wise_ops = defaultdict(list)
	for file in files:
		with open(file, 'r') as f:
			file_wise_ops[file] = list(f)


	print(file_wise_ops[files[0]])
	length = len(file_wise_ops[files[0]])
	total_count = 0
	error_count = 0
	for i in range(214, length):
		total_count += 1
		val1 = file_wise_ops[files[0]][i]
		val2 = file_wise_ops[files[1]][i]
		val3 = file_wise_ops[files[2]][i]
		if val1 != val2 or val2 != val3 or val3 != val1:
			error_count += 1 

	return error_count*100 / total_count

if __name__ == "__main__":
	error_percent = compare_files()
	print(error_percent)