# divide by zero
try:
    x = 10 / 0
except:
    print("Something went wrong!")
finally:
    print("This runs no matter what.")

# multiple exceptions for specific errors
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("You can't divide by zero.")
except ValueError:
    print("Invalid input! Please enter a number.")
finally:
    print("Program ended.")

# index exception
try:
    # some risky code
    li = []
    li[1]
except TypeError:
    print("Caught a TypeError!")
except IndexError:
    print("Caught an IndexError!")


# catching all exceptions
try:
    li = []
    li[1]
except Exception as e:
    print("Error occurred:", e)

# File not found error
try:
    f = open("file.txt")
except FileNotFoundError:
    print("File not found!")
finally:
    print("Closing resources...")