# demonstrate the use of function docstrings

def myFunc(arg1, arg2=None):
    """myFunc(arg1, arg2=None) ---> Doesn't do nothing

    Parameters:
    arg1: The first argument
    arg2: The second argument

    """
    print(arg1, arg2)

def main():
    print(myFunc.__doc__)

if __name__ == '__main__':
    main()