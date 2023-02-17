
import csv
with open('datastore.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    rows = list(csv_reader)
    for j in range(4,120):
          s = rows[j]
          new_list = s[2:770]
          #print(s)
          #print(new_list)
          norm = [float(i)/float(max(new_list)) for i in new_list]
          print(norm)
    j=j+1
    
#norm = [float(i)/float(max(new_list)) for i in new_list]
#print(norm)
        
    
'''
import pandas as pd

read_data = pd.read_csv("datastore.csv")
print(read_data)
'''
