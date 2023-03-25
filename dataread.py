import matplotlib.pyplot as plt
from sklearn import preprocessing
import csv
import numpy as np
with open('datastore.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    rows = list(csv_reader)
    for j in range(4,119):
          s = rows[j]
          new_list = s[2:770]
                                                                                                                                                                                                                                                                                                                                            
          #print(new_list)
          norm = [float(i)/float(max(new_list)) for i in new_list]
          
          #print(norm)
          #plt.plot(float(new_list1),float(norm[2]))
          #plt.show()
          
    j=j+1
plt.plot(norm)
plt.ylabel('amplitude')
plt.show()
    

        
    
'''
import pandas as pd

read_data = pd.read_csv("datastore.csv")
print(read_data)
'''
