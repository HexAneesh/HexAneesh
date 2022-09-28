print("Choose an option")
print("1.Multiply")
print("2.Divide")
print("3.Add")
print("4.Sutract")

option = input("Choose an option 1/2/3/4 :")

if option in ('1','3','4'):
    Num1 = float(input("Enter first number:"))
    Num2 = float(input("Enter second number:"))

    if option == '1':
        product = Num1*Num2
        print("Product:",product)

    elif option == '3':
        Sum = Num1+Num2
        print("Sum:",Sum)

    elif option == '4':
        Difference = Num1-Num2
        print("Difference:",Difference)

    elif option == '2':
        Num1 = float(input("Enter Dividend:"))
        Num2 = float(input("Enter Divisor:"))
        Quotient = Num1/Num2
        print("Quotient:",Quotient)
    
    

if option not in ('1','2','3','4'):
    print("Invalid input")
    print("Please enter a number in the list")
