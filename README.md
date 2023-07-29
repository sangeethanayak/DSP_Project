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

<p align="center">
<img src = "https://github.com/sangeethanayak/DSP_Project/assets/84203911/516af8df-82a2-424b-a569-bf6a57f0fa14.png" height = "300px">
<img src="https://github.com/sangeethanayak/DSP_Project/assets/84203911/5ea577c7-115f-46a4-85d5-1fb4fcde0f1c.png" height="300px">
<img src="https://github.com/sangeethanayak/DSP_Project/assets/84203911/bc94b38d-cded-48b3-8391-1a8f83566fe2.png" height="300px">
<img src = "https://github.com/sangeethanayak/DSP_Project/assets/84203911/8baee83a-759c-4b0d-b7c5-e84e88611a6e.png" height="300px">
<img src="https://github.com/sangeethanayak/DSP_Project/assets/84203911/adf1ea70-c03f-4995-8a0e-1b81a1b88b1e.png"  height="200px">
</p>









