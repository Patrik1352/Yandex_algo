import math

def calculate_correct_probability(L, M):
    return (2 * L**2) / (M**2 * math.pi) / 2

L = float(input())
M = float(input())

print(calculate_correct_probability(L,M))