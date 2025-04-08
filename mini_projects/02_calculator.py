first = int(input("enter first number : "))
opeartor = input("enter the operator : ") # -, = ,% ,/, * 
second = int(input("enter the operator : "))

if opeartor == '+' :
    print (first + second)
elif opeartor == '-' :
    print (first - second)
elif opeartor == '/' :
    print (first / second)
elif opeartor == '%' :
    print (first % second)
elif opeartor == '*' :
    print (first * second)

else :
    print ("error")