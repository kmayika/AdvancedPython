#demo the use of variable argument list - func(*var)---> func([])

# TODO: define a function that takes variable arguments
def addition(*args):
    result = 0
    for arg in args:
        result += arg
    return result

def main():
    # TODO: pass different arguments
    print(addition(5,10,15,20))

    # TODO: pass an existing list
    nums = [5,10,15,20]
    print(addition(*nums))

if __name__ == '__main__':
    main()
