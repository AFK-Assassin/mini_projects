while True :
    try :
        first = input("enter first number : ")
        if first.lower() == "q" :
            print ("Good bye ")
            break
        num1 = int(first)    
    
        opeartor = input("enter the operator : ") # -, = ,% ,/, * 

        second = input("enter second number : ")
        if second .lower() == "q" :
            print ("Good bye ")
            break
        num2 = int(second) 

        if opeartor == '+' :
            print (num1 + num2)

        elif opeartor == '-' :
            print (num1 - num2)

        elif opeartor == '/' :
            print (num1 / num2)

        elif opeartor == '%' :
            print (num1 % num2)

        elif opeartor == '*' :
            print (num1 * num2)

        else :
            print ("Error!!! use correct operator")
    except:
        print("invalid number")