def get_indices_of_item_weights(weights, length, limit):
    """
    Finds the indices of weights.
    """
    cache = {}

    for i in range(length):
        diff, current = limit - weights[i], weights[i]
        if diff in cache:
            return (i, cache[diff])
        else:
            cache[current] = i

    return None
