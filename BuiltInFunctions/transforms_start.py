#use transform functions like sorted(),filter() and map()

def filterFunc(x):
    if x % 2 == 0:
        return False
    return True

def filterFunc2(x):
    if x.isupper():
        return False
    return True

def squareFunc(x):
    return x**2

def toGrade(x):
    if x >= 90:
        return 'A'
    elif x >=80 and x< 90:
        return 'B'
    else:
        return 'F'

def main():
    #define some sample sequences to operate on
    nums = (1,2,3,44,6,576,7,44,88)
    chars="abcdeFgHiJKLmNoP"
    grades= (81,56,89,90,99,75,49)

    # TODO: use filter to remove items from a list
    odds = list(filter(filterFunc, nums))
    print(odds)
    # TODO use filter on non-numeric sequence
    lowers = list(filter(filterFunc2, chars))
    print(lowers)
    # TODO: use map to create a new sequence of values - maps one value to another
    squares = list(map(squareFunc,nums))
    print(squares)
    # TODO: use sorted() and map() to change numbers to grades
    grades = sorted(grades)
    letters = list(map(toGrade, grades))
    print(letters)

if __name__ == "__main__":
    main()