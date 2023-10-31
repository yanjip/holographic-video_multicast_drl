# time: 2023/10/31 9:55
# author: YanJP
import numpy as np
np.random.seed(0)
# Set the parameters
average_power_loss = 1e-3  # Average power loss (10^(-3))
num_samples = 1000  # Number of fading samples to generate

# Calculate the Rayleigh scale parameter (sigma)
# The scale parameter is related to the average power loss as follows:
# average_power_loss = 2 * sigma^2
sigma = np.sqrt(average_power_loss / 2)

# Generate independent Rayleigh fading samples
rayleigh_samples = sigma * np.random.randn(num_samples) + 1j * sigma * np.random.randn(num_samples)

rayleigh_samples =abs(rayleigh_samples)
# rayleigh_samples = np.random.exponential(1e-6, num_samples)
# rayleigh_samples =abs(np.random.rayleigh(scale=1, size= num_samples)*1e-3)
# The above code generates complex samples, where the real and imaginary parts
# are both independently Rayleigh distributed.

# Optionally, you can plot a histogram of the fading samples to visualize
# the Rayleigh distribution.
# import matplotlib.pyplot as plt
#
# plt.hist(np.abs(rayleigh_samples), bins=50, density=True)
# plt.title("Rayleigh Fading Samples")
# plt.xlabel("Amplitude")
# plt.ylabel("Probability Density")
# plt.show()

np.save('runs/constant/channel.npy', rayleigh_samples)