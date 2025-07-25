#!usr/bin/python1
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except:
        return False
