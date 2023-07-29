# Thermal Sensor Data Processing for Estimation of Breath Rate using DSP

## Overview

This project aims to estimate the breath rate of an individual using thermal sensor data and digital signal processing (DSP) techniques. A thermal sensor is used to capture temperature variations caused by the inhalation and exhalation of breath. The collected data is then processed using various DSP algorithms to estimate the breath rate.

## Table of Contents

- [Background](#background)
- [Installation](#installation)
- [Data Format](#data-format)
- [Digital Signal Processing](#digital-signal-processing)
- [Results](#results)

## Background

Breath rate monitoring is essential in various applications, such as sleep monitoring, stress analysis, and health monitoring. Traditional methods involve using specialized equipment, which may not always be convenient. This project explores a non-intrusive approach using thermal sensors and DSP algorithms to estimate breath rate accurately.

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/sangeethanayak/DSP_Project.git
```
## Data Format

The thermal sensor data is collected as a time-series of temperature readings. Each data point contains the temperature value recorded at a specific timestamp. The data is stored in a CSV format.

## Digital Signal Processing

The collected thermal sensor data undergoes several DSP steps, including:
- Filtering: The raw data is passed through a bandpass filter to remove noise and extract the breath-related signal.
- Fast Fourier Transform (FFT): The filtered data is transformed into the frequency domain to identify the dominant frequency associated with breath rate.
- Energy and Entropy Calculation: The energy and entropy of the filtered data are computed to assess breath rate characteristics.

## Results

The breath rate estimation results will be displayed or saved to a file, depending on the implementation. Users can visualize the estimated breath rate over time or receive real-time breath rate updates, depending on the application.







