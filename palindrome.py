import sys
def palindrome():
    str = sys.argv[1]
    str1 = str.lower().replace(" ","").replace(",","").replace(".","")
    str2 = str1[::-1]
    if str1 == str2:
        print("It's a palindrome!")
    else:
        print("It's not a palindrome!")
        
palindrome()