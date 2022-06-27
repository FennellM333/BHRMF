import pynbody
import numpy as np 
import matplotlib.pyplot as plt 
from pynbody import filt, array
import pandas as pd 
import pylab 

file =  '/mnt/data0/jillian/h568/h568.cosmo75.4096gsHsbBH.000240'

s = pynbody.load(file)

s.keys(file)

#initializes the command to find black holes
def findBH(s):
    BHfilter = pynbody.filt.LowPass('tform',0.0)
    BH = s.stars[BHfilter]
    return BH

def findBHhalos(s,BH):
    BHhalos = BH['amiga.grp']
    return BHhalos

#
h = s.halos()  
s.physical_units()  
BHfilter = pynbody.filt.LowPass('tform',0.0) 
BH =  s.stars[BHfilter]  
BHhalos = findBHhalos(s, BH)

print(type(BHhalos))
print(type(BHhalos['tform']))