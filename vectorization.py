import numpy as np

w = np.array([1.0, 2.5, -3.3])
x = np.array([10, 20, 30])
b = 4
n = 3

def without_vectorization():
    f = (w[0] * x[0]) + (w[1] * x[1]) + (w[2] * x[2]) + b
    return f

def with_for_loop():
    f = 0
    for j in range(0, n):
        f = f + (w[j] * x[j])
    f = f + b
    return f

def vectorization():
    f = np.dot(w, x) + b
    return f

def main():
    f = vectorization()
    print(f)

main()









