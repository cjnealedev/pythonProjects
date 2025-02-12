import sys
def gpa():
    gpa_dict = {'A':4.0, 'A-':3.66, 'B+':3.33, 'B':3.0, 'B-':2.66, 'C+':2.33, 'C':2.0, 'C-':1.66, 'D+':1.33, 'D':1.00, 'D-':.66, 'F':0.00}
    input = sys.argv[1].capitalize()
    output=[]
    for i in input:
        output.append(gpa_dict[i])
    print("My GPA is", "{:.2f}".format(sum(output) / len(output)))
    
gpa()