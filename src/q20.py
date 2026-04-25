from itertools import permutations


def solve(number) -> bool:
    s = str(number)
    n = len(s)

    if n % 2 != 0:
        return False

    half = n // 2
    num = int(s)

    seen = set()
    for perm in permutations(s):
        fang1_str = ''.join(perm[:half])
        fang2_str = ''.join(perm[half:])

        pair = tuple(sorted([fang1_str, fang2_str]))
        if pair in seen:
            continue
        seen.add(pair)

        if fang1_str[-1] == '0' and fang2_str[-1] == '0':
            continue

        if int(fang1_str) * int(fang2_str) == num:
            return True

    return False
