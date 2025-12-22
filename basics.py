name = "Megha"          
age = 20               
height = 5.4            
is_student = True       

marks = [80, 85, 90]    
subjects = ("Maths", "CS", "English")  

def calculate_average(marks_list):
    total = 0
    for mark in marks_list:     
        total += mark
    return total / len(marks_list)

def check_pass(avg):
    if avg >= 75:
        return "Distinction"
    elif avg >= 50:
        return "Pass"
    else:
        return "Fail"

# -------- MAIN PROGRAM --------
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)
print("Subjects:", subjects)
average = calculate_average(marks)
result = check_pass(average)

print("Average Marks:", average)
print("Result:", result)
