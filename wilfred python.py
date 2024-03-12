# python comment -single line
"""
multi-line comment
"""

#variables
student_name ="Wilfred" #data type is string
student_age = 20 #data type is integer
student_fee = 100.0 #data type is float
student_marks = 100
is_male = True #data type is boolean

#outputting the values in the variables
print(student_name)
print(student_age)
print(student_fee)
print(is_male)



#Case sensitivity
student_name="kibe"
STUDENT_NAME="koech"


#variable naming in python
book_price =20
_book_price =20
book_price_123=20

x=y=z=10 #one value to many variables
x,y,z=10,20,30 #multiple value


#casting
price=15
qty=3
total_price=price*qty
print("your charges are" +str(total_price)+ "Ksh")

first_name="Wilfred"
second_name="kibet"
third_name=first_name+" "+str(second_name)
print("My third name is",third_name)

residence = "kasarani"

if residence=="kasarani" or residence=="Embakasi" or residence=="westlands":
    print("You can be governer")
else:
    print("You are not governer")

