"""Module docstring"""


# imports
# CONSTANTS

def main():
    """Function docstring"""
    # statements...
    get_password()


def get_password():
    """Function docstring"""
    # statements...
    password = input('Enter password: ')
    for i in range(len(password)):
        print('*', end="")
    print()
    # another way
    print('*' * len(password))


main()




