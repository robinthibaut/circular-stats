"""
The p-values from the general Rayleigh test and the vtest are not directly comparable because they are testing
different hypotheses. The general Rayleigh test is testing the hypothesis that the data is uniformly distributed
around the circle, while the vtest is testing the hypothesis that the data is not distributed uniformly around the
circle with a known mean angle. If you are interested in testing whether the data is uniformly distributed around the
circle, you should use the general Rayleigh test. If you are interested in testing whether the data is not
distributed uniformly around the circle with a known mean angle, you should use the vtest.
"""
# Here is a code snippet to explain the difference. We'll be using astropy's Rayleigh test.
# p_rayleigh = circstats.rayleightest(data)
# p_vtest = circstats.vtest(data, mean_angle)
import numpy as np
from astropy.stats import circstats
from matplotlib import pyplot as plt

mean_angle = np.pi

# Generate random data points uniformly distributed across the circle.
# set the random seed to make the example reproducible
np.random.seed(42)
data = np.random.uniform(0, 2 * np.pi, 1000)  # 1000 points

# Compute the p_rayleigh and p_vtest.
p_rayleigh = circstats.rayleightest(data)
# p_rayleigh = 0.539, meaning that the data is uniformly distributed around the circle.
p_vtest = circstats.vtest(data, mean_angle)
# p_vtest = 0.806

print("p_rayleigh = {:.3f}".format(p_rayleigh))
print("p_vtest = {:.3f}".format(p_vtest))

# Plot the data.
plt.figure(figsize=(10, 10))

# Generate 1000 x, y points distributed uniformly around the circle.
x_circle = np.cos(np.linspace(0, 2 * np.pi, 1000))
y_circle = np.sin(np.linspace(0, 2 * np.pi, 1000))

# Plot the circular data points.
plt.plot(
    np.cos(data),
    np.sin(data),
    '.',
    label="Data Points",
)

# Plot a circle to show that the data is uniformly distributed.
plt.plot(
    x_circle,
    y_circle,
    color="k",
    alpha=0.4,
    label="Circle",
)

# Add the legend.
plt.legend()

# Show the plot.
plt.show()

# %%
# Now let's see what happens if we have non-uniformly distributed data.

# Generate randomly distributed data that isn't uniformly distributed.
known_angle = np.pi  # the mean angle
data = np.random.vonmises(known_angle, 2, 58)  # 58 points with a known mean angle

# Compute the p_rayleigh and p_vtest.
p_rayleigh = circstats.rayleightest(data)
# p_rayleigh = 0.000, meaning that the data is not uniformly distributed around the circle, as expected!
p_vtest = circstats.vtest(data, known_angle)
# p_vtest = 0.000, meaning that the null hypothesis is rejected when testing for violations of uniformity with a mean
# direction of 180 degrees.

print("p_rayleigh = {:.3f}".format(p_rayleigh))
print("p_vtest = {:.3f}".format(p_vtest))

# Plot the data.
plt.figure(figsize=(10, 10))

# Plot the circular data points.
plt.plot(
    np.cos(data),
    np.sin(data),
    '.',
    label="Data Points",
)

# Plot a circle to show that the data is not uniformly distributed.
plt.plot(
    x_circle,
    y_circle,
    color="k",
    alpha=0.4,
    label="Circle",
)

# Add the legend.
plt.legend()

# Show the plot.
plt.show()
