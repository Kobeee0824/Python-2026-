inputmore = ""

while inputmore != "N":
  try: 
    num1 = float(input("Enter First Number: "))
    operator = input("Enter Operator (+ | - | * | /): ")
    num2 = float(input("Enter Second Number: "))


    def getAnswer(num1, operator, num2):
      if operator == "+":
        return num1 + num2
      elif operator == "-":
        return num1 - num2
      elif operator == "*":
        return num1 * num2
      elif operator == "/":
        return num1 / num2
    
    answer = getAnswer(num1, operator, num2)
    print(f"The answer is {answer}")

    inputmore = input("Do you want to input again?(Y/N): ").upper()
  except:
    print("Invalid Input!")


print("Thank you for playing!")
