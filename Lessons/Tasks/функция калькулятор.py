def math1(num1,num2,operation1):
    if operation1 == "+":
        print(num1+num2)
    elif operation1=="-":
        print(num1-num2)
    elif operation1=="*":
        print(num1*num2)
    elif operation1=="/":
        print(num1/num2)

num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
user_operation1=(input ("Enter operation1"))

user_operation2=int(input("Enter operation2"))

user_operation3=int(input("Enter operation3:"))

user_operation4=int(input("Enter operation4:"))


math1(user_operation1)
math1(user_operation2)
math1(user_operation3)
math1(user_operation4)


  


