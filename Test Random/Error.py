def divide(value):
    try:
        return 42/value
    except ZeroDivisionError:
        return "Error: Invalid argument."


print(divide(2))
print(divide(1))
print(divide(0))

#or
"""
def divide(value):
    return 42/value
    
try:
    print(divide(2))
    print(divide(1))
    print(divide(0))
except ZeroDivisionError:
    print("Error: Invalid argument.")

"""