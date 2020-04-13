from __future__ import print_function

def answer(l): # More efficient way ?
    doubles = []
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[j] % l[i] == 0:
                doubles.append((l[i], l[j]))

    triples = []
    num_triples = 0
    for i in range(len(doubles)):
        for j in range(i+1, len(doubles)):
            if doubles[i][1] == doubles[j][0]:
                triple = (doubles[i][0], doubles[i][1], doubles[j][1])
                if not (triple in triples):
                    triples.append(triple)
                    num_triples += 1

    return num_triples

if __name__ == "__main__":
    print(answer([1, 2, 3, 4, 5, 6]))
    print(answer([1, 1, 1]))
