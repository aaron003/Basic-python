print("Enter Add keyword for Addition, Mul for Multiplication, Sub for Subtraction or Div for Division")

operator = input("Enter the keyword? ")
first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))

match operator:
    case "Add":
        print("Sum:", first_num + second_num)
    case "Mul":
        print("Mul:", first_num * second_num)
    case "Sub":
        print("Sub:", first_num - second_num)
    case "Div":
        print("Div:", first_num / second_num)
    


  
   