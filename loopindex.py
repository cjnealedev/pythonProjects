import sys
loop_list = sys.argv[1:]
int_list = []
ind_list = []
for s in loop_list:
    int_list.append(int(s))
for index, element in enumerate(int_list):
    ind_list.append(int(index))
result = [x + y for x, y in zip(int_list, ind_list)]

print(result)