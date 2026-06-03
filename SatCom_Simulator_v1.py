# =========================
# IMPORTS
# =========================

import math
import matplotlib.pyplot as plt

# =========================
# FUNCTIONS
# =========================

def free_space_path_loss(frequency_hz, distance_m):
    c = 3e8
    term1 = 20 * math.log10(distance_m)
    term2 = 20 * math.log10(frequency_hz)
    term3 = 20 * math.log10(4 * math.pi / c)
    return term1 + term2 + term3


def calculate_eirp(power_dbw, tx_gain_db):
    return power_dbw + tx_gain_db


def received_power(eirp_dbw, fspl_db):
    return eirp_dbw - fspl_db


def noise_power(k, temperature):
    return 10 * math.log10(k * temperature)


def carrier_to_noise(pr_dbw, noise_db):
    return pr_dbw - noise_db


def received_power_rain(eirp_dbw, fspl_db, rain_db):
    return eirp_dbw - fspl_db - rain_db


# =========================
# INPUT PARAMETERS
# =========================

f = 24e9
d = 3.8e7

k = 1.38e-23
T = 500

# =========================
# BASELINE LINK BUDGET
# =========================

fspl = free_space_path_loss(f, d)
print("FSPL:", fspl, "dB")

eirp = calculate_eirp(20, 45)
print("EIRP:", eirp, "dBW")

pr = received_power(eirp, fspl)
print("Received Power:", pr, "dBW")

noise = noise_power(k, T)
print("Noise Power:", noise, "dB")

cn = carrier_to_noise(pr, noise)
print("C/N0:", cn, "dB")

# =========================
# TEMPERATURE ANALYSIS
# =========================

temps = [200, 300, 500, 800, 1000]
cn_values = []

for T in temps:
    noise = noise_power(k, T)
    cn = carrier_to_noise(pr, noise)
    cn_values.append(cn)

plt.plot(temps, cn_values)
plt.xlabel("Temperature (K)")
plt.ylabel("C/N0 (dB)")
plt.title("C/N0 vs Temperature")
plt.show()

# =========================
# DISTANCE ANALYSIS
# =========================

distances = [3e7, 5e7, 7e7, 3.336e7]
cn_values_dist = []

for d in distances:
    fspl_dist = free_space_path_loss(f, d)
    pr_dist = received_power(eirp, fspl_dist)
    noise = noise_power(k, 500)
    cn_dist = carrier_to_noise(pr_dist, noise)
    cn_values_dist.append(cn_dist)

plt.plot(distances, cn_values_dist)
plt.xlabel("Distance (m)")
plt.ylabel("C/N0 (dB)")
plt.title("C/N0 vs Distance")
plt.show()

# =========================
# RAIN FADE ANALYSIS
# =========================

rain_values = [0, 5, 10, 15, 20, 23, 25, 30]
cn_rain_values = []

noise = noise_power(k, 500)

for rain in rain_values:
    pr_rain = received_power_rain(eirp, fspl, rain)
    cn_rain = carrier_to_noise(pr_rain, noise)
    cn_rain_values.append(cn_rain)

plt.plot(rain_values, cn_rain_values)
plt.xlabel("Rain Attenuation (dB)")
plt.ylabel("C/N0 (dB)")
plt.title("C/N0 vs Rain Attenuation")
plt.show()