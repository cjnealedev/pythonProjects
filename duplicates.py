import sys
duplicated_words = sys.argv[1:]
unique_list = list(set(duplicated_words))
unique_list.sort(reverse=True)
print(unique_list)