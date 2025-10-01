import matplotlib.pyplot as plt 
import numpy as np 

data= np.loadtxt('timeTable.txt')

BHid = data[:,0]
#print("ID",BHid)
dCen = data[:,1]
#print("distance",dCen)
timeBH = data[:,2]
#print("time",timeBH)


#BHid=BHid[0]
#dCen=dCen[0]
#timeBH=timeBH[0]
#print (BHid)
uniqueBHid = np.unique(BHid)
print("uniqueID", uniqueBHid)



for id in uniqueBHid:
    print(id)
    aragorn = np.where(BHid == id)
    print(aragorn[0])
    gimli = dCen[aragorn[0]]
    print("gimli",gimli)
    legolas = timeBH[aragorn[0]]
    print("legolas", legolas)
    plt.plot(legolas,gimli)
    plt.xlabel("Time (Gyr)")
    plt.ylabel("Distance from Galaxy Center (kpc)")
    plt.title("Distance from Center OverTime")
    plt.show()
    
    

    