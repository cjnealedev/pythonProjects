import sys
def grade():
    grades = {'Biology':80, 'Physics':88, 'Chemistry':98, 'Math':89, 'English':79, 'Music':67, 'History':68, 'Art':53, 'Economics':95, 'Psychology':88}
    remove = sys.argv[1]
    new_grades = {key: value for key, value in grades.items() if key != remove}
    average = round(sum(new_grades.values()) / len(new_grades),2)
    print(average)

grade()