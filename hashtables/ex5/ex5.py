# Your code here



def finder(files, queries):
    """
    Finds file names and returns file paths.
    """
    file_locations = {}

    for filepath in files:
        filename = filepath.split("/")[-1]
        if filename in file_locations:
            file_locations[filename].append(filepath)
        else:
            file_locations[filename] = [filepath]

    result = []
    for filename in queries:
        if filename in file_locations:
            for filepath in file_locations[filename]:
                result.append(filepath)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
