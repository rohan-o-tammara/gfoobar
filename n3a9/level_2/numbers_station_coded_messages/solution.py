from __future__ import print_function

def answer(l, t):
    results = []
    # More efficient way to do this ?
    for window in range(1, len(l)):
        for i in range(len(l)-window+1):
            sublist = l[i:i+window]
            if sum(sublist) == t:
                results.append([i, i+window-1])

    result = None
    if len(results) == 0:
        result = [-1, -1]
    else:
        result = min(results)

    return result

if __name__ == "__main__":
    print(answer([4, 3, 5, 7, 8], 12))
    print(answer([4, 3, 10, 2, 8], 12))
    print(answer([1, 2, 3, 4], 15))
