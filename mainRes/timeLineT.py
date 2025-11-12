import pynbody
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import astropy.units as u
import pylab
import itertools as it
import warnings
import decimal
import statistics
import numpy.core.defchararray as npd
from itertools import tee
from pynbody import filt, array 
import csv
#resultdataset = npd.equal(dataset1, dataset2)

files = '/mnt/data0/jillian/h568/productionrun/files.list'
files = np.genfromtxt(files, dtype='str')
print(len(files))
files = files[0]

#creating an array to put all the distance results into
dCen=[]
BHid=[]

# function to find black hole
def findBH(s):
    BHfilter = pynbody.filt.LowPass('tform',0.0)
    BH = s.stars[BHfilter]
    return BH
print("defined BHs")

#function to find the halos that the galaxy is in
def findBHhalos(s):
    BH = findBH(s)
    BHhalos = BH['amiga.grp']
    return BHhalos
print("define halos")
#using the function the halos

def getz(s):
    return s.properties['z']

def gettime(s):
    return pynbody.analysis.cosmology.age(s)

print("loop begins")

f =  open("foundTLT.txt", "w+") 
#for file in files:     # loading the snapshot
s =pynbody.load('/mnt/data0/jillian/h568/productionrun/'+files)
print("loaded snapshot", s)
# convert the units 
s.physical_units()
#  load any available halo
h = s.halos()
BH = findBH(s)
BHhalos = findBHhalos(s)
print("BHhalos", BHhalos)
#sorting the halos, indexes/indecis are like an exact address   
sortedhalo = np.argsort(BHhalos)
print ("current halo" , BHhalos[sortedhalo])

for i in sortedhalo:
    
    #which halo are we on?
    currenthalo = BHhalos[i]
    print ('current halo: ', currenthalo)
    print ("iterant", i)
    #put the galaxy you care about in the center of the simulation
    pynbody.analysis.angmom.faceon(h[currenthalo])
    #this is the position of black hole
    BHposition=BH['pos']

    #putting the x-values into a column
    BHx= BHposition[[i],0]
    print ("x postion", BHx)
   
    #putting the y-values into a column
    BHy= BHposition[[i],1]
    print ("y position", BHy)

    #putting the z-values into a column
    BHz= BHposition[[i],2]
    print ("z position", BHz)

    #the .5 is the square root , this is the distance formula this is the distance of the black hole from the center of its host galaxy
    distance =((BHx**2)+(BHy**2)+(BHz**2))**(.5)
    print ("distance from center:", distance[0])
    
    starmass = h[currenthalo].s['mass'].sum()
    gasmass = h[currenthalo].g['mass'].sum()
    virialmass = starmass+gasmass+h[currenthalo].d['mass'].sum()
    
    dCen.append(distance[0])
    BHid.append(BH['iord'][i])   
    
   
    
    
    t = BH['age']
    print("age of BH", t)
    
    
zip(BHid,dCen)
with open ('foundTLT.csv','w') as f:
    writer= csv.writer(f, delimiter= '\t')
    writer.writerows(zip(BHid,dCen))
    
f.close()
