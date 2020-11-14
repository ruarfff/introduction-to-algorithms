def sort(numbers):
    for i, num in enumerate(numbers[1:]):
        idx = i
        j = i + 1
        while idx >= 0 and numbers[idx] > num:
            numbers[idx + 1] = numbers[idx]
            idx = idx - 1
        numbers[idx + 1] = num
    return numbers


print(sort([1, 2]))
print(sort([3, 1, 2, 6, 0]))
print(sort([]))
print(sort([5, 2, 4, 6, 1, 3]))
