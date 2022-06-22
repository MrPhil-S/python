#print (f"First module's name: {__name__}")

#__name__ is a predefined variable when python runs

def main():
    print (f"First module's name: {__name__}")


#is this file being run directly and not being
#imported by another file?

if __name__ == '__main__':
    main()