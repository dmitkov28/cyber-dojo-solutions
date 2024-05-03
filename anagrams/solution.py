from itertools import permutations

def generate_anagrams(input_str: str):
    return ["".join(x) for x in  list(permutations(input_str, len(input_str)))]

