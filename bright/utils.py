def count_same_tokens(str1: str, str2: str) -> int:
    tks1 = str1.lower().split(" ")
    tks2 = str2.lower().split(" ")

    return len(list(set(tks1) & set(tks2)))
