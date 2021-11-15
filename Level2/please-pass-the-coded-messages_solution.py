def solution(l):
    if (sum(l)%3==0):
        return ''.join(map(str, sorted(l, reverse=True)))
    else:
        for digit in l:
            if ((sum(l)-digit)%3==0):
                if (digit!=0):
                    l.remove(digit)
                    return ''.join(map(str, sorted(l, reverse=True)))
        for digit in sorted(l):
            if (digit%3!=0):
                l.remove(digit)
                if (sum(l)%3==0):
                    if (len(l) > 0):
                        return ''.join(map(str, sorted(l, reverse=True)))
    return '0'
