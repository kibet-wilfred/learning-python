number1=0
number2=20
try:
    x=number2/number1
except Exception as w:
        print("error occurred:",w)
else:
    print(x)
    print("all is well")