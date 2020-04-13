from __future__ import print_function

def answer(start, length):
    checksum = 0
    for i in range(length**2):
        n = start + i
        eol = (length-1)*int(i/length)+length # End of line limit
        if i < eol:
            checksum = checksum ^ n
    return checksum

if __name__ == "__main__":
    print(answer(0, 3))
    print(answer(17, 4))
