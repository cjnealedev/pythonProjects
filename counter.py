import sys
def count_characters():
    char_count = {}
    input_string = sys.argv[1]    
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count

result = count_characters()

print(result)