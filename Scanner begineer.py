Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import pickle
stu ={}
stufile = open('Stu.dat','wb')
ans='y'

=================================== RESTART: C:/Users/SOUNAVA/Documents/fl1.py ===================================
Enter roll no:21
Enter name:Rishav
Enater marks:52
Want to enter more records ?(y/n)...y
Enter roll no:24
Enter name:Riya
Enater marks:45
Want to enter more records ?(y/n)...n

=================================== RESTART: C:/Users/SOUNAVA/Documents/fl2.py ===================================
Traceback (most recent call last):
  File "C:/Users/SOUNAVA/Documents/fl2.py", line 3, in <module>
    empfile = open('Emp.dat','rb')
FileNotFoundError: [Errno 2] No such file or directory: 'Emp.dat'

=================================== RESTART: C:/Users/SOUNAVA/Documents/fl2.py ===================================
{'Rollno': 21, 'Name': 'Rishav', 'Marks': 52.0}

=================== RESTART: C:\Users\SOUNAVA\AppData\Local\Programs\Python\Python310\Stack.py ===================
STACK OPERATIONS
1. Push
2. Pop
3. Display stack
4. Exist
Enter your choice(1-4):1
Enter item 10
STACK OPERATIONS
1. Push
2. Pop
3. Display stack
4. Exist
Enter your choice(1-4):1
Enter item 20
STACK OPERATIONS
1. Push
2. Pop
3. Display stack
4. Exist
Enter your choice(1-4):3
20 <-top
10
STACK OPERATIONS
1. Push
2. Pop
3. Display stack
4. Exist
Enter your choice(1-4):4
