import sys
my_ints = sys.argv[1:]
int_list = []
output=[]
def comp():
    for s in my_ints:
        int_list.append(int(s))
    for i in int_list:
        if i % 3 == 0:
            i *= 10
        output.append(i)
    print(output) 
comp()