def stats(students):
    matric = [x for x in students.keys()]
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



    # subjects = set([x[0] for x in subjects_grades])
    # subjects = [x for x in subjects]
    # grades = []
    # for sub in subjects:
    #     single_grade = []
    #     for sub2 in subjects_grades:
    #         if sub == sub2[0]:
    #             single_grade.append(sub2[1])
    #     grades.append(single_grade)

    # grades = [round( (sum(x)/len(x)), 2) for x in grades]


    for student, avg in zip(matric, total_values):
        avg_grade_student[student]=avg

    # for subject, grade in zip(subjects, grades):
    #     avg_grade_subject[subject]=grade

    
    
    d = {}
    for key, val in subjects_grades:
        d.setdefault(key, []).append(val)

    for i in d.keys():
        d[i]=  round( sum(d[i])/len(d[i]) ,2)



    return avg_grade_student, d




raw = {"12-345-678": [("Math", 5.5),  ("Biology", 5.75), ("Latin", 4.25)],
    "09-876-543": [("Latin", 3.5), ("Biology", 4.5)],
    "01-111-111": [("Latin", 4.5), ("Biology", 4.75), ("French", 3.00)],
    }

# print(stats(raw))


students, subjects = stats(raw)
assert(len(students) == 3)
assert(len(subjects) == 4)
assert(students["12-345-678"] == 5.17)
assert(subjects["Latin"] == 4.08)