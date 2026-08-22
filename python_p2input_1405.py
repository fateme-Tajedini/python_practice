# A script that takes three numbers as input and caculates the maximum and minimum among them.


number1 = int(input("Enter a number:"))
number2 = int(input("Enter a number:"))
number3 = float(input("Enter a number:"))

if number1 >= number2 and number3 :
    print(number1 ,": max ")
  
elif number2 >= number3:
    print(number2 , ": max")
else:
    print(number3 ,": max ")


if number1 <= number2 and number1:
  print(number1 ,": min ")

elif number2 <= number3:
    print(number2 , ": min")
else:
     print(number3 ,": min ")


# complete


print(type(number1))
print(type(number3))        # Determining the data type.
