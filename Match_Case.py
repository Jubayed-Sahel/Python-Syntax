a=int(input("enter num: "))

match a:
    case 3:
        print("The value is 3")
    case 2:
        print("The value is 2")
    case 1:
        print("The value is 1")
    case _:
        print("Other number")
