import sys    
def count_vowels():
    count = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}
    str = sys.argv[1]
    for char in str:
        if char.lower() in vowels:
            count += 1
        print(count)
count_vowels()