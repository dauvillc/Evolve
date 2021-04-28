"""
Tests basic features of the CURDL class
"""
from curdl import CURDL_code


if __name__ == "__main__":
    empty_code = CURDL_code()
    one_child_code = CURDL_code(['T', '', '', '', '', '', ''])
    wrong_code = CURDL_code(['T', '', 'T', '', '', '', ''])

    print("Empty code :", empty_code.check_validity())
    print("One child code: ", one_child_code.check_validity())
    print("Wrong Code: ", wrong_code.check_validity())
