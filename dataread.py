import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from collections import OrderedDict
from scipy.signal import butter, filtfilt, welch
from scipy import signal
from scipy.signal import firwin, lfilter, welch
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

x_values=np.arange(len(floats))*0.03125
plt.plot(x_values,floats)
#plt.xticks(np.arange(0,0.03125), fontsize=8)
plt.xticks(np.arange(0, len(floats)*0.03125, 1), fontsize=8)
#print(len(floats)*0.03125)
plt.xlabel('Time (s)')
plt.ylabel('Normalized Values')
plt.show()



fs = 32  # sampling frequency
fc = 0.5  # cutoff frequency
N = 101  # number of taps
b = signal.firwin(N, fc, pass_zero=False, window='hamming', fs=fs)
filtered_data= signal.convolve(floats, b, mode='same')

# plot filtered signal
plt.plot(filtered_data)
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.show()


"""
#filter specifications
fs = 153.3
fs1 = 32
cutoff = 10
nyq = 0.5 * fs
order = 4 
b, a = butter(order, cutoff/nyq, btype='low')
filtered_data = filtfilt(b, a, floats)
"""

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
breathing_rate = xf1[max_index]
print("Breathing rate: {:.2f} Hz".format(breathing_rate))


        

