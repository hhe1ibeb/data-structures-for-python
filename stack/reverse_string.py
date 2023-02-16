from stack import Stack


def reverse_string(stack, input_str):
    for i in range(len(input_str)):
        stack.push(input_str[i])
    s = ""
    for i in range(len(input_str)):
        s += stack.pop()
    return s


stack = Stack()
print(reverse_string(stack, input("Input String: ")))
