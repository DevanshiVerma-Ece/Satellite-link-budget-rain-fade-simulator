# Satellite-link-budget-rain-fade-simulator

## Overview
This project is a Python-based simulator for analyzing satellite communication links. It calculates key link budget parameters such as Free Space Path Loss (FSPL), Effective Isotropic Radiated Power (EIRP), Received Power, Noise Power, and Carrier-to-Noise Ratio (C/N₀).

The simulator also studies the impact of environmental and system parameters on link performance through graphical analysis.

---

## Features

- Free Space Path Loss (FSPL) Calculation
- Effective Isotropic Radiated Power (EIRP) Calculation
- Received Power Estimation
- Noise Power Calculation
- Carrier-to-Noise Ratio (C/N₀) Analysis
- Rain Fade Modeling
- Performance Visualization using Matplotlib

---

## Equations Used

### Free Space Path Loss

FSPL = 20log10(d) + 20log10(f) + 20log10(4π/c)

where:

- d = Distance between satellite and ground station
- f = Operating frequency
- c = Speed of light

### Effective Isotropic Radiated Power

EIRP = Transmitter Power + Antenna Gain

### Received Power

Received Power = EIRP − FSPL

### Received Power with Rain Attenuation

Received Power = EIRP − FSPL − Rain Attenuation

### Carrier-to-Noise Ratio

C/N₀ = Received Power − Noise Power

---

## Simulations Performed

### 1. C/N₀ vs Temperature

Analyzes the effect of increasing system noise temperature on link quality.

Expected Result:
- Higher temperature leads to lower C/N₀.

### 2. C/N₀ vs Distance

Analyzes the effect of increasing satellite distance on communication performance.

Expected Result:
- Greater distance increases path loss and reduces C/N₀.

### 3. C/N₀ vs Rain Attenuation

Analyzes the impact of rain fade on link performance.

Expected Result:
- Increasing rain attenuation reduces C/N₀.

---

## Technologies Used

- Python
- Math Module
- Matplotlib
---

## Sample Parameters

| Parameter             | Value     |
| Frequency             | 24 GHz    |
| Distance              | 38,000 km |
| Transmitter Power     | 20 dBW    |
| Antenna Gain          | 45 dB     |
| System Temperature    | 500 K     |
---

## Future Improvements

- BER vs C/N₀ Analysis
- Uplink and Downlink Comparison
- Link Availability Analysis
- ITU Rain Attenuation Models
- Interactive GUI Dashboard
---
## Author

Devanshi Verma

Electronics and Communication Engineering Student

Interested in Hardware Systems, Satellite Communications, RF Engineering, and Space Technology.
