from stack import Stack


def convert_int_to_bin(dec_num):
    binary = Stack()
    k = dec_num
    t = 0
    while k >= 1:
        binary.push(k % 2)
        print(k)
        k = k // 2
        t += 1
    result = ""
    for i in range(t):
        result += str(binary.pop())
    return int(result)


print(convert_int_to_bin(int(input("Input Number: "))))
