def has_negatives(a):
    """
    Takes positive number and finds its corresponding negative number
    """
    numbers = {}
    result = []

    for num in a:
        numbers[num] = num

        if num != 0 and -num in numbers:
            result.append(abs(num))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
