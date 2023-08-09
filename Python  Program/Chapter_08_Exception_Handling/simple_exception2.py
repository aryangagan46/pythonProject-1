
import os

# os.remove(r'C:\Users\DARSHAN BM\Newproject1')

try:
    os.remove(r'C:\Users\DARSHAN BM\Newproject1\bodystyle.css')
except:
    print('error while deleting  the file')

finally:
    print("end of program")

"""
build in exceptions
"""
print(dir(locals()['__builtins__']))
s = dir(locals()['__builtins__'])
print(type(s))
print(len(s))