def intersection(arrays):
    """
    Finds the intersection of list of numbers.
    """
    numbers = {}
    for array in arrays:
        for number in array:
            if number not in numbers:
                numbers[number] = 1
            else:
                numbers[number] += 1
    result = []
    for number in numbers:
        if numbers[number] > 1:
            result.append(number)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
