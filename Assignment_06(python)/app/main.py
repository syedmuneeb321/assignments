


def manage_student_database()->None:
    student_list = []
    student_id = 1
    

    while True:
        exit = False
        input_value =  input("Please enter the student's name (or type 'stop' to finish):").strip()
        if input_value == "stop":
            break 
        
        if len(student_list) > 0:
            for student in student_list:
                if student[1] == input_value:
                    print("This name is already in the list.")
                    exit = True
                
        if not exit:
            student_list.append((student_id,input_value))
            student_id += 1

    print(" ")
    print("Complete List of Students (Tuples):")
    print(student_list,"\n")
    

    print("List of Students with IDs:")
    
    
    students_names_list = []
    for student in student_list:
        student_name = student[1]
        print(f"ID: {student[0]},Name: {student_name}")
        students_names_list.append(student_name)
    
    print(" ")
    
    
    print(f"Total Number of students: {len(student_list)}")
    
    print(f"Total length of all student names combined:{len("".join(students_names_list))}")
    
    print(f"The student with the longest name is: {max(students_names_list,key=len)}")
    print(f"The student with the shortest name is: {min(students_names_list,key=len)}")

    print("\n")

    


if __name__ == "__main__":
    manage_student_database()




    