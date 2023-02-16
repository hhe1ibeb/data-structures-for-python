from stack import Stack


def is_match(p1, p2):
    if p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    elif p1 == "(" and p2 == ")":
        return True
    return False


def is_paren_balanced(paren):
    s = Stack()
    is_balanced = True
    for char in paren:
        if char in "{[(":
            s.push(char)
        else:
            if s.is_empty():
                is_balanced = False
                return False
            else:
                top = s.pop()
                if not is_match(top, char):
                    is_balanced = False
                    return False
    if s.is_empty() and is_balanced:
        return True
    else:
        return False


try:
    while True:
        print(is_paren_balanced(input("Input String: ")))
except EOFError:
    pass
