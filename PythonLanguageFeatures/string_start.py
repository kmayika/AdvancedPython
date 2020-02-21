def main():
    b = bytes([0x41,0x42,0x43,0x44])
    print(b)

    s = "This is a string"
    print(s)
    # TODO: concatenating b and s using ''decode'' function to convert to string - utf-8
    b2 = b.decode('utf-8')
    print(s+b2)

    # TODO: concatenate b and s using encode func to convert to bytes - utf-8
    s2 = s.encode('utf-8')
    print(b+s2)

    # TODO: encode string using utf-32
    s3 = s.encode('utf-32')
    print(s3)


if __name__ == '__main__':
    main()
