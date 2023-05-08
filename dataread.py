import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from collections import OrderedDict
from scipy.signal import butter, filtfilt, welch
from scipy import signal
from scipy.signal import firwin, lfilter, welch, freqz
from scipy.signal.windows import hamming
from numpy import convolve


with open('datastore.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    rows = list(csv_reader)
    for j in range(4,118):
          s = rows[j]
          new_list = s[2:770]
          #print(s)
          #print(new_list)
          norm = [float(i)/float(max(new_list)) for i in new_list]
          floats = [float(k) for k in norm]
          #print(max(new_list),'max')
          #print(norm)
          #print("Normalised values")
          #print(floats)
    j=j+1

#print(floats)

x_values=np.arange(len(floats))*0.0625
plt.plot(x_values,floats)
#plt.xticks(np.arange(0,0.03125), fontsize=8)
plt.xticks(np.arange(0, len(floats)*0.0625, 2), fontsize=8)
#print(len(floats)*0.03125)
plt.xlabel('Time (s)')
plt.ylabel('Normalized Values')
plt.show()



# Apply bandpass filter
fs = 16  # Sampling rate (Hz)
f_low = 0.1  # Lower cutoff frequency (Hz)
f_high = 0.5  # Upper cutoff frequency (Hz)
order = 4  # Filter order
b, a = signal.butter(order, [f_low * 2 / fs, f_high * 2 / fs], btype='band')
filtered_data = signal.filtfilt(b, a, floats)

# Plot filtered signal
x_values = np.arange(len(filtered_data)) / fs
plt.plot(x_values, filtered_data)
plt.xlabel('Time (s)')
plt.ylabel('Filtered Values')
plt.show()



#fft specifications

N = 1000
freq = 16
T = 1.0 / freq

#without filter
y = np.array(floats[:N])
yf = np.fft.fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
psd = 2.0/N * np.abs(yf[:N//2])**2

plt.plot(xf, psd)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power Spectral Density (PSD)')
plt.show()



# With filter
y1 = np.array(filtered_data[:N])
yf1 = np.fft.fft(y1)
xf1 = np.linspace(0.0, 1.0/(2.0*T), N//2)
psd1 = 2.0/N * np.abs(yf1[:N//2])**2

plt.plot(xf1, psd1)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power Spectral Density (PSD)')
plt.show()



max_index = np.argmax(psd1)
breathing = xf1[max_index]
breathing_rate= breathing*60
print("Breathing rate: {:.2f} bpm".format(breathing_rate))

# Calculate time domain energy and entropy for filtered_data
energy_time = np.sum(np.square(filtered_data))
hist, bins = np.histogram(filtered_data, bins='auto', density=True)
prob = hist / np.sum(hist)
entropy_time = -np.sum(prob * np.log2(prob))
print('Energy in time domain=',energy_time)
print('Entropy in time domain=',entropy_time)



# Calculate frequency domain energy and entropy for filtered_data
freq, psd = welch(filtered_data, fs=fs, nperseg=256)
energy_freq = np.sum(psd)
prob_freq = psd / np.sum(psd)
entropy_freq = -np.sum(prob_freq * np.log2(prob_freq))
print('Energy in freq domain=',energy_freq)
print('Entropy in freq domain=',entropy_freq)
