c = [['Arad', 0], ['Zerind', 75], ['Timisoara', 118], ['Sibiu', 140]]
a = [['Arad', 0]]


def get_diff(a: list, b: list) -> list:
    return list(set(a) ^ set(b))


get_diff(c, a)
