def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Invalid input types. Both arguments must be numbers.")
    except (IndexError, ValueError):
        # This block catches exceptions of both kinds
        print("Error: IndexError or ValueError.")
    else:
        # Code to be executed if no exception was raised in the try block
        print(f"The result is {result}.")
    finally:
        print("This message will always be printed, regardless of whether an exception was raised or not.")
