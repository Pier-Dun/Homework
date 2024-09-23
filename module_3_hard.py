def calculate_structure_sum(*args):
    result = 0
    for i in args:
        if isinstance(i, list) or isinstance(i, tuple) or isinstance(i, set):
            result += calculate_structure_sum(*i)
        elif isinstance(i, dict):
            for j, k in i.items():
                if isinstance(j, tuple) or isinstance(j, set):
                    result += calculate_structure_sum(j)
                elif isinstance(j, str):
                    result += len(j)
                else:
                    result += j
                if isinstance(k, list) or isinstance(k, tuple) or isinstance(k, set) or isinstance(k, dict):
                    result += calculate_structure_sum(k)
                elif isinstance(k, str):
                    result += len(k)
                else:
                    result += k
        elif isinstance(i, str):
            result += len(i)
        else:
            result += i
    return result

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(calculate_structure_sum(data_structure))
