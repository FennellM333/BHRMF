import pynbody
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

dCen = [2,4,16,32,128,256,512,1024,2048]
BHid = [1,2,3,4,5,6,7,8,9]

#f = open()

"""for row in f:
    row=row.split(' ')
    names.append(row[0])
    marks.append(int(row[1]))
"""
plt.plot(dCen,BHid, color = 'g', label = 'File Data')

plt.xlabel ('Distance from Center', fontsize = 12)
plt.ylabel('Black Hole ID',fontsize = 12)

plt.title('Merger Graph I', fontsize = 20)
plt.legend()
plt.show()



