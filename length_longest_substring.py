from typing import Dict


def length_longest_substring(s: str) -> int:
    dictionary: Dict[str, int] = {}
    highest_length = 0
    length = 0
    for c in s:
        if dictionary.get(c) is None:
            dictionary[c] = 1
            length += 1
        else:
            if length > highest_length:
                highest_length = length
            length = 0
            dictionary = {}
    return highest_length


if __name__ == "__main__":
    result = length_longest_substring("abrkaabcdefghijjxxx")
    print(result)
