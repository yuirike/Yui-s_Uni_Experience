# from <File> import <Code>
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Exam_Codes.Exam_5 import encode


A = encode("hello", "xyz", -2)
print(A)



