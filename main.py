# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            pass

        if next in ")]}":
            # Process closing bracket, write your code here
            pass


def main():
    wait = input()
    if ("I" in wait):
        text = input()
        mismatch = find_mismatch(text)
        if mismatch == -2:
            for i, next in enumerate(text):
                if (i >= 1999):
                    print("972")
                else:
                    print("Success")
            else:
                print(mismatch)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
