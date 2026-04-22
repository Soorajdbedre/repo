def arithmetic(a, b):
    return {
        'Addition': a + b,
        'Subtraction': a - b,
        'Multiplication': a * b,
        'Division': a / b if b != 0 else 'undefined',
        'Modulus': a % b if b != 0 else 'undefined'
    }

# Input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Call the function and print results
results = arithmetic(num1, num2)
# print(results)
for operation, result in results.items():
    print(f"{operation}: {result}") 

print("This is working")