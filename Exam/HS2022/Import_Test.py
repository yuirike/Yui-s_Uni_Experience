import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from HS2020.Stats_2 import stats


raw = {"12-345-678": [("Math", 5.5),  ("Biology", 5.75), ("Latin", 4.25)],
    "09-876-543": [("Latin", 3.5), ("Biology", 4.5)],
    "01-111-111": [("Latin", 4.5), ("Biology", 4.75), ("French", 3.00)],
    }
    
students, subjects = stats(raw)
assert(len(students) == 3)
assert(len(subjects) == 4)
assert(students["12-345-678"] == 5.17)
assert(subjects["Latin"] == 4.08)

print(stats(raw))