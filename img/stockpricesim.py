# %%
from math import *
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rc('font', family='serif')


def simulate_gbm(S0, mu, sigma, T, n_steps):
    Z = np.zeros(n_steps + 1)
    dt = T / n_steps
    Z[0] = log(S0)

    epsilon = np.random.randn(n_steps)

    for i in range(0, n_steps):
        Z[i+1] = Z[i] + (mu - 0.5 * sigma**2) * dt + \
            sigma * sqrt(dt) * epsilon[i]

    return np.exp(Z)


n_steps = 365   # days in a year
T = 1           # one year
sigma = 0.2     # 20% volatility per year
mu = 0.08       # 8% growth per annum
S0 = 100        # initial stock price

times = np.linspace(0, 1, n_steps+1)
S = simulate_gbm(S0, mu, sigma, T, n_steps)

# mpl.use("pgf")
ax = plt.gca()
ax.plot(times, S)
ax.set_xlabel('Time')
ax.set_ylabel('Stock price')
ax.set_title('Discrete time geometric Brownian motion')
# save as PGF file which can be used in your document via `\input`
plt.savefig("stock.pgf")
plt.savefig("stock.pdf")  # save as PDF created with LaTeX

# %%
