import pynbody
import numpy as np 
import matplotlib.pyplot as plt 
from pynbody import filt, array
import pandas as pd 

filenamelist =  '/mnt/data0/jillian/h568/h568.cosmo75.4096gsHsbBH.000240'

nfilenames = len(filenamelist)

BHiordlist =[]

k=2
def findBH(s):
    BHfilter = pynbody.filt.LowPass('tform',0.0)
    BH = s.stars[BHfilter]
    return BH

def findBHhalos(s,BH):
    BHhalos = BH['amiga group']
    return BHhalos

for j in range(nfilenames):
    if j %2==0:
        k=k+2
        print("                                                                                       Merger #", (2+k)/2)
        print("                                                                   Before Merger")
        print(" ")
        print("Primary BH", BHiordist[k])
        print("Secondary BH", BHiordlist[k+1])
    
    if j%2==1:
        print("                                                                   After Merger")
        print(" ")
        print("Merged BH: ", BHiordlist[k])
        
    s = pynbody.load(filenamelist[j])
    h = s.halos()
    s.physical_units()
    BHfilter = np.where((s.stars['iord']==BHiordlist[k])|(s.stars['iord']==BHiordlist[k+1]))
    BH = s.stars[BHfilter]
    BHhalos = findBHhalos(s,BH)
    
    data = np.zeros((5,len(BH)))
    
    f = open("findingBH.txt","a")
    for i in range(len(BH)):
        if BHhalos[i]==0:
          print("Skipping, halos = 0")
          continue
       pynbody.analysis.halo
       x = BH['pos'][[i],0]
       y = BH['pos'][[i],1]
       z = BH['pos'][[i],2]
       distance = ((x**2+y**2+z**2)**0.5)
       starmass = h[BHhalos[i]].s['mass'].sum()
       redshift = s.properties['z']
       if i%2==0 :
           MassRatio = MassRatio_list[i/2]
           data[0,i] = BH['iord'][i]
           data[1,i] = BHhalos[i]
           data[2,i] = distance(0)
           data[3,i] = starmass
           data[4,i] = redshift
           data[5,i] = MassRatio
           
    data = np.transpose(data)
    df = pd.DataFrame(data = data, columns = ['Black Hole ID#','Host Galaxy', 'Distance(kpc)', 'Total Stellar Mass', 'Redshift', 'Mass Ratio'])
    df = df[df['Host Galaxy']!=0] 
    df =str(df)
    print(df) 
    f.write(df)
f.close()      