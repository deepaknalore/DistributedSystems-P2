from collections import defaultdict

files = ['wisconsin.log', 'clemson.log', 'utah.log']

file_wise_ops = defaultdict(list)
for file in files:
	with open(file, 'r') as f:
		file_wise_ops[file] = list(f)

def compare_files():
	length = len(file_wise_ops[files[0]])
	total_count = 0
	error_count = 0
	for i in range(0, length):
		total_count += 1
		val1 = file_wise_ops[files[0]][i]
		val2 = file_wise_ops[files[1]][i]
		val3 = file_wise_ops[files[2]][i]
		if val1 != val2 or val2 != val3 or val3 != val1:
			error_count += 1 

	return error_count*100 / total_count

def get_error(list1, list2):
	total_count = 0
	error_count = 0
	for i in range(len(list1)):
		total_count += 1
		if list1[i] != list2[i]:
			error_count += 1
	return error_count * 100 / total_count


def pair_wise_compare():
	pair_wise_errors = defaultdict(lambda : defaultdict(float))
	file_pairs = [[files[0], files[1]], [files[1], files[2]], [files[2], files[0]]]
	for file_pair in file_pairs:
		pair_wise_errors[file_pair[0]][file_pair[1]] = get_error(file_wise_ops[file_pair[0]], file_wise_ops[file_pair[1]])
	return pair_wise_errors


if __name__ == "__main__":
	error_percent = compare_files()
	print(error_percent)
	pair_wise_errors_dict = pair_wise_compare()
	for key1 in pair_wise_errors_dict:
		for key2 in pair_wise_errors_dict[key1]:
			print(key1, key2, pair_wise_errors_dict[key1][key2])



