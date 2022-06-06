import numpy as np

m = 2000
x1 = np.random.normal(m)
x2 = np.random.normal(m)
eta = np.ones(m) + x1 + x2
# eta temporaral used for generate mu
mu = np.exp(eta) / (1 + np.exp(eta))
# y = np.zeros(m)
y = np.random.binomial(np.ones(m), mu)
X = np.stack([np.ones(m), x1, x2], axis=1)
beta = np.zeros(3)
eta = X.dot(beta)

n = 0
beta