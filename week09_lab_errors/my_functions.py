# this program takes a number and returns a list contain a Fibonacci sequence of that number
# Author: Stephen Kerr

# import logging
import logging

#logging.basicConfig(level=logging.DEBUG)


def fibonacci(n):
    """This function takes a number and returns a list containing the Fibonacci sequence of that number."""
    a = 0
    b = 1
    fibonacci_sequence = [0]
    if n == 0: # if n is 0, return an empty list
        return []
    elif n < 0: # if n is negative, raise a ValueError
        raise ValueError('number must be > 0')

    for i in range(1, n):
        fibonacci_sequence.append(b)
        a, b = b, a + b
    logging.debug('%d: %s', f"Fibonacci sequence for {n}: {fibonacci_sequence}")
    return fibonacci_sequence



if __name__ == '__main__':
    # test the function
    return7 = [0, 1, 1, 2, 3, 5, 8]
    assert fibonacci(7) == return7, f"Expected {return7} but got {fibonacci(7)}"
    return11 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    assert fibonacci(11) == return11, f"Expected {return11} but got {fibonacci(11)}"
    return0 = []
    assert fibonacci(0) == return0, f"Expected {return0} but got {fibonacci(0)}"
    return1 = [0]
    assert fibonacci(1) == return1, f"Expected {return1} but got {fibonacci(1)}"
    try:
        fibonacci(-1)
    except ValueError as e:
        # we want the exception to be raised
        # se we do nothing 
        pass
    else:
        # if the exception was not raised
        # we raise an assertion error
        assert False, "Fibanacci missing ValeueError"
    print('all good')