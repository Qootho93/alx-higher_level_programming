#!/usr/python3
def safe_print_division(a, b):
    try:
        answer = a / b
    except (ZeroDivisionError, FloatingPointError):
        answer = None
    finally:
        print("Insight result: {}".format(answer))
        return answer
