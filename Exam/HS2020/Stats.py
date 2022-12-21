def stats(students):
    matric = [x for x in students.keys()]
    items = [x for x in students.items()]
    val_list = []
    total_values = []
    avg_grade_student = {}
    avg_grade_subject = {}

    for student in matric:
        val_list.append(students[student])
    
    for list in val_list:
        values = []
        for val in list:
            values.append(val[1])
   
        total_values.append(values)
    total_values = [round( (sum(x)/len(x)), 2) for x in total_values]

    subjects_grades = []
    for list in val_list:
        subjects_grades.extend(list)


    for student, avg in zip(matric, total_values):
        avg_grade_student[student]=avg
   
    
    avg_grade_per_subject = {}
    for subject, grade in subjects_grades:
        avg_grade_per_subject.setdefault(subject, []).append(grade)

    for i in avg_grade_per_subject.keys():
        avg_grade_per_subject[i]=  round( sum(avg_grade_per_subject[i])/len(avg_grade_per_subject[i]) ,2)

    # student_avg_grade = {}
    # for i in students.keys():
    #     student_avg_grade[i] = [list(x) for x in students[i]]

    return avg_grade_student, avg_grade_per_subject



raw = {"12-345-678": [("Math", 5.5),  ("Biology", 5.75), ("Latin", 4.25)],
    "09-876-543": [("Latin", 3.5), ("Biology", 4.5)],
    "01-111-111": [("Latin", 4.5), ("Biology", 4.75), ("French", 3.00)],
    }

print(stats(raw))


# students, subjects = stats(raw)
# assert(len(students) == 3)
# assert(len(subjects) == 4)
# assert(students["12-345-678"] == 5.17)
# assert(subjects["Latin"] == 4.08)