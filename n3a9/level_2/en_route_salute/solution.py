from __future__ import print_function

def num_salutes(hall):
    right = []
    left = []
    for i in range(len(hall)):
        if hall[i] == '>':
            right.append(i)
        if hall[i] == '<':
            left.append(i)

    crossings = 0
    for r in right:
        for l in left:
            if r < l:
                crossings += 1

    return crossings*2

if __name__ == "__main__":
    print(num_salutes("--->-><-><-->-"))
    print(num_salutes(">----<"))
    print(num_salutes("<<>><"))
