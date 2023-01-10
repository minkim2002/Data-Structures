import sys  # for sys.argv, the command-line arguments
from Stack import Stack


def delimiter_check(filename):
    # TODO replace pass with an implementation that returns True
    # if the delimiters (), [], and {} are balanced and False otherwise.
    delimiter = Stack()
    f = open(filename, "r")
    for i in f:
        if i == '(':
            delimiter.push(i)
        elif i == '{':
            delimiter.push(i)
        elif i == '[':
            delimiter.push(i)
        elif i == ')':
            val = delimiter.pop()
            if val != '(':
                return False
        elif i == '}':
            val = delimiter.pop()
            if val != '{':
                return False
        elif i == ']':
            val = delimiter.pop()
            if val != '[':
                return False
    f.close()
    if len(delimiter) == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    # The list sys.argv contains everything the user typed on the command
    # line after the word python. For example, if the user types
    # python Delimiter_Check.py file_to_check.py
    # then printing the contents of sys.argv shows
    # ['Delimiter_Check.py', 'file_to_check.py']
    if len(sys.argv) < 2:
        # This means the user did not provide the filename to check.
        # Show the correct usage.
        print('Usage: python Delimiter_Check.py file_to_check.py')
    else:
        if delimiter_check(sys.argv[1]):
            print('The file contains balanced delimiters.')
        else:
            print('The file contains IMBALANCED DELIMITERS.')
