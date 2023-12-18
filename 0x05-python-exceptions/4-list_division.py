#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    tmp_result = 0
    for i in range(0, list_length):
        try:
            tmp_result = my_list_1[i] / my_list_2[i]
        except TypeError:
            tmp_result = 0
            print("Wrong type")
        except ZeroDivisionError:
            tmp_result = 0
            print("out of range")
        finally:
            pass
        new_list.append(tmp_result)
        return new_list
