#use iterator functions like enumerate, zip, iter, next

def main():
    #define a list of days in English and French
    days = ["sun", "mon", "tue", "wed", "thur", "fri", "sat"]
    daysFr = ["dim", "lun", "mar", "mer", "jeu", "ven", "sam"] 

    # TODO: use iter to create an iterator over a collection - creates iterable object
    i = iter(days)
    print(next(i))
    print(next(i))
    print(next(i))
    # TODO: iterate using a function and a sentinel ('') - if the iterator gets to a sentinel value, it will stop iterating
    with open("testfile.txt") as fd:
        for line in iter(fd.readline, ''):
            print(line)
            
    # TODO: use regular iteration over days
    for m in range(len(days)):
        print(m+1,days[m])
    # TODO: using enumerate reduces code an provides a counter
    for i,m in enumerate(days, start=1):
        print(i,m)
    # TODO: use zip to combine sequences
    for m in zip(days, daysFr):
        print(m)
        


if __name__ == '__main__':
    main()