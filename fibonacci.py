n = 10
num1 = 0
num2 = 1
successive_number = num2 
count = 1
 
while count <= n:
    print(successive_number, end=" ")
    count += 1
    num1, num2 = num2, successive_number
    successive_number = num1 + num2
print()
