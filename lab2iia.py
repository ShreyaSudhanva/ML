import numpy as np
from matplotlib import pyplot as plt
from scipy.special import factorial
from scipy.stats import chi2

# Sample of a normal distribution
samples = np.random.normal(size=10000)

# Build a histogram from the sample
bins = np.linspace(-5, 5, 30)
histogram, bins = np.histogram(samples, bins=bins, density=True)
bin_centers = 0.5 * (bins[1:] + bins[:-1])

# Plot the graph
plt.figure(figsize=(6, 4))
plt.plot(bin_centers, histogram, label="Normal")

# Sample for a Poison distribution
t = np.arange(0, 20, 0.1)
d = np.exp(-5) * np.power(5, t) / factorial(t)
plt.plot(t, d, 'bs', label="Poison")

# Sample for Chisquare distribution
num = chi2.numargs
[seq] = [0.6, ] * num
rv = chi2(seq)
distribution = np.linspace(0, np.minimum(rv.dist.b, 5))
plt.plot(distribution, rv.pdf(distribution), label='chi-square', c='r')

# Plot all three
plt.legend()
plt.show()
