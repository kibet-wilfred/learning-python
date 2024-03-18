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


num=19

num=int(input("Enter the number to be tested:"))
if num % 2 == 0:
        print("Even")
else:
        print("Odd")


country=input("Enter your country:")
if country=="Kenya":
    print("East african")
elif country=="Uganda":
    print("East african")
elif country=="Tanzania":
    print("East african")
else:
    print("Not east african")




x= 1
while x<=10:
    if x==3 or x==5:

        x+=1
        continue
    print("the number is :", x)
    x+=1
else:
    print("ended")


number=1
total=0
while number<=10:
    if number%2==0:
        total += number
        number+=1
        print("the sum of odd numbers is :", number)
