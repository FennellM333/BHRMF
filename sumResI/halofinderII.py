import pynbody
import numpy as np 
import matplotlib.pyplot as plt 
from pynbody import filt, array
import pylab 

filenamelist =  '/mnt/data0/jillian/h568/h568.cosmo75.4096gsHsbBH.000240'

# iord? that should give each black hole a unique id to match eventually with their respective halo
s = pynbody.load(filenamelist)
h = s.halos()
s.physical_units()

#filters our stars into black holes
def  locBH(s):      
    BHfilter = pynbody.filt.LowPass('tform',0.0)
    BH = s.stars[BHfilter] 
    return BH
BH = locBH(s)
BHid = BH['iord']

#this should filter those black holes further to only those with halos
def  locBHhalos(s):
    BHhalos = BH['amiga.grp']
    return BHhalos
BHhalos = locBHhalos(s)

dCen = []

for i in range(len(BH)):  #starts the loop that will check how far each black hole is from their respective halos
    if BHhalos[i] == 0: #skips over all the black holes with no halos 
        continue
    pynbody.analysis.halo.center(h[BHhalos[i]], mode='hyb') #actually centers the snapshot on each halo
    x=BH['pos'][[i],0]
    y=BH['pos'][[i],1]
    z=BH['pos'][[i],2]
    #aquires the x y and z coordinates of each black hole relative to its respective center
    dCen.append(((x**2+y**2+z**2)**0.5)[0]) #creates an array of the distances for each black hole

#ok actually this is a loop I lied but this is what I used to format the array into the text file
with open('found.txt' , 'w') as f:
    f.write("       |BH ID|          |Galaxy ID|   |Distance from Center| \n") 
    for a,b,c in zip(BHid,BHhalos,dCen):
        f.write('{0:15}{1:15}         {2:.5}\n'.format(a,b,c))  