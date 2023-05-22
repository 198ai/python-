import numpy as np


# sigmoid激活函数
def sigmoid(a):
    return 1 / (1 + np.exp(-a))


x1 = np.array([[1], [2]])
w1 = np.array([[0.4, 0.3], [0.7, 0.6]])
b1 = np.array([[1.0], [1.0]])
a1 = w1.dot(x1)

x2 = sigmoid(a1)
w2 = np.array([[0.2, 0.3], [1, 0.7]])
b2 = np.array([[1.0], [1.0]])
a2 = w2.dot(x2)

y = sigmoid(a2)
t = np.array([[1], [0]])

X = [x1, x2]
A = [a1, a2]
W = [w1, w2]
B = [b1, b2]

# 网络的最大层数，即输入层和输出层之间的层数
max_layer = len(X)

# 激活函数的导数，用于计算反向传播中的梯度
def f(a):
    return (1 - sigmoid(a)) * sigmoid(a)


def g(l, j):
    if max_layer == l:
        return (y[j] - t[j]) * f(A[l - 1][j])
    else:
        output = 0
        m = A[l - 1].shape[0]
        for i in range(m):
            output += g(l + 1, i) * W[l][j, i] * f(A[l - 1][j])
        return output


def diff(j, k, l):
    return g(l, j) * X[l - 1][k]


def diff_b(j, l):
    return g(l, j)


for _ in range(100):
    for l in range(len(X)):

        for j in range(W[l].shape[0]):
            for k in range(W[l].shape[1]):
                print(W[l][j, k])
                W[l][j, k] = W[l][j, k] - diff(j, k, l + 1)
            B[l][j] = B[l][j] - diff_b(j, l + 1)
    A[0] = W[0].dot(X[0])
    X[1] = sigmoid(A[0])
    A[1] = W[1].dot(X[1])
    y = sigmoid(A[1])

print(y)
