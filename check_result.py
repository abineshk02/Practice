def check_result(name,marks):
    if marks>=50:
        result = "pass"
    else:
        result ="fail"

    return result

student_name ="megha"
student_marks = 72
final_result = check_result(student_name,student_marks)
print(student_name)
print(student_marks)
print(final_result)