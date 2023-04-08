print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("--------")
print("just a enter a starting number of the opeation")
print("--------")

user_wants = input("What operation you do Now : ")

def calculation(need):
    if need == "1":
        num1 = int(input("Enter 1st number :"))
        num2 = int(input("Enter 2nd number :"))
        print("addition is :", num1+num2)
    elif need == "2":
        num1 = int(input("Enter 1st number :"))
        num2 = int(input("Enter 2nd number :"))
        print("subtraction is :", num1-num2)
    elif need == "3":
        num1 = int(input("Enter 1st number :"))
        num2 = int(input("Enter 2nd number :"))
        print("multiplication is :", num1*num2)
    elif need == "4":
        num1 = int(input("Enter 1st number :"))
        num2 = int(input("Enter 2nd number :"))
        print("division is :", num1/num2)
    else:
        print("You have chosen wrong option , try to choose correct option : \n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division ")

calculation(user_wants)