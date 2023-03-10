array = ["hello","I am ByteBrain ","python developer","this problem given by chat gpt"]
def main(list):
	max_long_string = []
	for i in list:
		max_long_string.append(len(i))
	biggest_string = max(max_long_string)
	for i in range(len(list)):
		if biggest_string == len(list[i]):
			print(list[i])
main(array)
#output [ this problem given by chat gpt ]