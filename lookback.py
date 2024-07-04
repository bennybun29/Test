numbers = []
enterNum = True

while enterNum == True:
    num = int(input("Enter a number: "))
    numbers.append(num)
    answer = str(input("Do you want to add more?(y/n): "))
    if answer == "y":
        enterNum = True
    elif answer == "n":
        numbers.sort()
        numbers.reverse()
        print(numbers)
        enterNum = False
    else:
        print("Invalid. Try Again!")
