# python3
#4attempt

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i))
    

        if next in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack:
                return i + 1
            last = opening_brackets_stack.pop()
            if not are_matching(last.char, next):
                return i + 1
    if opening_brackets_stack:
        return opening_brackets_stack[0].position + 1
    else:
        return "Success"
            

def main():
    suc = "Success"
    ch = input()
    if "I" in ch:
        text = input()
        mismatch = find_mismatch(text)
        if mismatch == suc:
            print(suc)
        else:
            print(mismatch)
    elif "F" in ch:
        infile = input("File path: ")
        with open(infile, "r") as file:
            text = file.read()
            mismatch = find_mismatch(text)
            if mismatch != suc:
                print(mismatch)
            else:
                print(suc)
    else: 
        print("wrong input")

    # Printing answer, write your code here

    

if __name__ == "__main__":
    main()
