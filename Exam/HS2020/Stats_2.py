def stats(students):
    dic1 = {}
    for student in students.keys():
        dic1[student] = [list(x) for x in students[student]]

    def flat_list(l):
        return [item for sublist in l for item in sublist]

    dic2 = {}
    for student in dic1.keys():
        dic2[student] = flat_list(dic1[student])

    dic3 = {}
    for student in dic2.keys():
        dic3[student] = [x for x in dic2[student] if not type(x) == str]

    avg_grade_student = {}
    for student in dic3.keys():
        avg_grade_student[student] = round(  sum(dic3[student]) / len(dic3[student]),2)


    subject_grades = flat_list([x for x in students.values()])

    dic4 = {}
    for sub, grade in subject_grades:
        dic4.setdefault(sub, []).append(grade)

    avg_grade_subject = {}
    for sub in dic4.keys():
        avg_grade_subject[sub] = round(  sum(dic4[sub]) / len(dic4[sub]),2)

  
    return avg_grade_student, avg_grade_subject


raw = {"12-345-678": [("Math", 5.5),  ("Biology", 5.75), ("Latin", 4.25)],
    "09-876-543": [("Latin", 3.5), ("Biology", 4.5)],
    "01-111-111": [("Latin", 4.5), ("Biology", 4.75), ("French", 3.00)],
    }
students, subjects = stats(raw)
assert(len(students) == 3)
assert(len(subjects) == 4)
assert(students["12-345-678"] == 5.17)
assert(subjects["Latin"] == 4.08)