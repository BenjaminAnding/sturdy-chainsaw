def solution(s):
    c, t = 0
    for char in s:
        if char == '>':
            c += 1
        elif char == '<':
            t = t + c
    return 2 * t