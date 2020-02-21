# demonstrate the use of keyword only arguments


# use keyword-only arguments to help ensure code clarity --> put an *
def myFunc(arg1, arg2, *, suppressExc=False):
    pass

def main():
    # try to call the function without keyword
    myFunc(1,2, suppressExc=True)

if __name__ == '__main__':
    main()