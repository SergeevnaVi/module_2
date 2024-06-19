def calculate_structure_sum(data):
    def recurse(element, summa):
        if isinstance(element, int):
            return summa + element
        elif isinstance(element, str):
            return summa + len(element)
        elif isinstance(element, list) or isinstance(element, tuple) or isinstance(element, set):
            for item in element:
                summa = recurse(item, summa)
        elif isinstance(element, dict):
            for key, value in element.items():
                summa = recurse(key, summa)
                summa = recurse(value, summa)
        return summa
    return recurse(data, 0)


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)