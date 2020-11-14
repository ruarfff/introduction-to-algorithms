def search(numbers, val):
    for i, num in enumerate(numbers):
        if num is val:
            return i
    return None


print(search([1, 2], 3))
print(search([3, 1, 2, 6, 0], 1))
print(search([], 1))
print(search([5, 2, 4, 6, 1, 3], 3))
