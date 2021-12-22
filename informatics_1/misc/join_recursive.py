# joins strings recursively without the join() method


def recursive_join(delim: str, values: str) -> str:
    first = values[0]
    if len(values) < 2:
        return first
    first += delim
    return first + recursive_join(delim, values[1:])


print(recursive_join(" ", ["Hello", "world"]) == "Hello world")
