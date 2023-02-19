# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i+1))
        if next in ")]}":
            if not are_matching(opening_brackets_stack[-1].char, next):
                return i+1
            if not opening_brackets_stack:
                return i+1
            opening_brackets_stack.pop()

    if opening_brackets_stack:
        last_open, last_open_index = opening_brackets_stack.pop()
        return last_open_index + 1
    else:
        return "Success"


def main():
    text = input()
    # print(text)
    if "I" in text:
        mismatch = find_mismatch(text)
        if mismatch == "Success":
            print(mismatch)
        else:
            print(mismatch)


if __name__ == "__main__":
    main()
