import sys
input_string = sys.argv[0]
def shortest_word(input_string):
    words = input_string.split()
    shortest = words[0]

    for word in words:
        if len(word) < len(shortest):
            shortest = word
    print(shortest)
shortest_word()