try:
    # Code that may raise a ValueError
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))
    result = a / b
    print('Division:', result)
except ZeroDivisionError:
    b=int(input('Enter second number: '))
    print('division', a /b)
except ValueError:
    # Handle the ValueError here
    print('Invalid input. Please enter valid numbers.')
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))
    print('division', a / b)
