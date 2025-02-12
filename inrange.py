import sys
def multiples():
    input_value = int(sys.argv[1])
    results = []
    for i in range(3000, 5001):
        if i % input_value == 0 and i % (input_value + 7) == 0 and i % (input_value * input_value) == 0:
            results.append(i)
    print(results)
multiples()