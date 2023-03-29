import matplotlib.pyplot as plt
import csv
import numpy as np
with open('datastore.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    rows = list(csv_reader)
    for j in range(4,119):
          s = rows[j]
          new_list = s[2:770]                                                                                                                                                                                                                                                                                                                      
          norm = [float(i)/float(max(new_list)) for i in new_list]
          floats = norm.append(norm)
          #norm.append(range(0,767) for k in norm)
          #norm.append() 
          #floats = [float(k) for k in norm]  
          print(norm.count(norm[0]))
             
j=j+1
#plt.plot(norm) 
#plt.ylabel('normalized amplitude')
#plt.xlabel('samples')
#plt.show()
print(floats.count(floats[0]))






#for m in range(0,117):
    #plt.plot(m,floats[m]) 
    #plt.show()
#for m in floats:
     #plt.plot(floats[m])
#plt.show()  
#print(floats.count(floats[0]))
#for m in range(0,768):
      #for n in np.arange(0,61,0.005):
           #plt.plot(n,floats[m])
           #plt.show()
#for l in np.arange(0,61,0.005):
     # plt.plot(l,floats[0])

    

        

