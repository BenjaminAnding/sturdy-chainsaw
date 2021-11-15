def solution(n):
    coefficients = [1]+[0]* n
    for i in range(1, n+1):
        for j in range(n, i-1, -1):
            coefficients[j] += coefficients[j-i]
            print(coefficients)
    return coefficients[n] - 1
