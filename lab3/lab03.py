''' Module lab03.py'''
def problem_1(num_list, num):
    return list(filter(lambda x: x % num == 0, num_list))
def problem_2(num_list, dig):
    mylist = [str(i) for i in num_list]
    mylist = [num for num in mylist if str(dig) in str(num)]
    mylist = list(map(int, mylist))
    return mylist
def problem_3(string, char_list):
    mylist = [c for c in string if c not in char_list]
    return "".join(map(str, mylist))
def problem_4(num_list):
    nums = range(2, 10)
    mylist = [num for num in num_list if [num for i in nums if num % i == 0]]
    return mylist
