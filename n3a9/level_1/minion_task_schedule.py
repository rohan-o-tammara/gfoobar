def answer(data, n):
    result = data
    nums = set(data)
    for num in nums:
        if data.count(num) > n:
            result = list(filter(lambda x: x != num, result))

    return result

if __name__ == "__main__":
    print answer([5, 10, 15, 10, 7], 1)
    print answer([1, 2, 3], 0)
    print answer([1, 2, 2, 3, 3, 3, 4, 5, 5], 1)
    print answer([1, 2, 3], 6)
