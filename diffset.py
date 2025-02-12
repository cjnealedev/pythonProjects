import sys
set_a = sys.argv[1:]
set_b = ['apple', 'banana', 'mango', 'orange']
list_a = set(set_a)
list_b = set(set_b)
def match (set_a,set_b):
    nonmatches = list_a - list_b
    print(nonmatches)
match(list_a,list_b)