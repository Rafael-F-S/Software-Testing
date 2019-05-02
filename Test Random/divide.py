def divide_two_values(first, second):
    if (second == 0.0):
        raise ArithmeticException('Cannot divide by zero!')
    else:
        result = first / second
        return result
    

def check_divide_by_zero(self):

    self.assertRaises(Exception, divide_two_values, (3.0, 0.0))