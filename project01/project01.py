# Author: Saj Patel
# Write a function named count_chars()
# Problem 1
def count_chars(string):
	""" Counts the number of times each char has been used in 
	the string passed"""
	dict = {}
# assigning keys as each character present in the string
	for char in string:
		keys = dict.keys()
		if char in keys:
			dict[char] += 1
		else:
			dict[char] = 1
	return dict
# Write a function named concat_dicts()
# Problem 2
def concat_dicts(dict1, dict2):
	""" Merges the two dictionaries that are passed in the method"""
	# creates a new dictionary and adds dict1 to it
	merged_dict = dict1.copy()
	# adding the content of dict2 into the merged_dict
	for key in dict2:
		if key not in merged_dict or dict2[key] > merged_dict[key]:
			merged_dict[key] = dict2[key]
	return merged_dict
# write a function named diff_lists()
# Problem 3
def diff_lists(list1, list2):
	"""checks to see what elements in the two lists are unique between 
	the two and returns a new list with those elements"""
	new_list = []
	for elem in list1:
		if elem not in list2:
			new_list.append(elem)
	for elem in list2:
		if elem not in list1:
			new_list.append(elem)
	return new_list
# write a function named print_dict_subset
# problem 4
def print_dict_subset(lis, dic):
	"""gets the keys from the list and checks to see if the 
	key exists in the dictionary if so it prints the value
	associated to the key"""
	for elem in lis:
		if elem in dic:
			print(dic.get(elem))
