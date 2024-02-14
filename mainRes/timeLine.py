import pynbody
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import astropy.units as u
import pylab
import itertools as it
from itertools import tee
import warnings
import decimal
import statistics
import numpy.core.defchararray as npd
#resultdataset = npd.equal(dataset1, dataset2)

files = '/mnt/data0/jillian/h568/productionrun/files.list'
files = np.genfromtxt(files, dtype='str')

dCen=[]


# function to find black hole
def findBH(s):
    BHfilter = pynbody.filt.LowPass('tform',0.0)
    BH = s.stars[BHfilter]
    return BH

#function to find the halos that the galaxy is in
def findBHhalos(s):
    BH = findBH(s)
    BHhalos = BH['amiga.grp']
    return BHhalos

#using the function the halos

def getz(s):
    return s.properties['z']

def gettime(s):
    return pynbody.analysis.cosmology.age(s)

f =  open("bhfile.dat", "w+") 
for file in files:
    
    # loading the snapshotS
    s =pynbody.load('/mnt/data0/jillian/h568/productionrun/'+file)
 
    # convert the units 
    s.physical_units()

    #  load any available halo
    h = s.halos()
    BH = findBH(s)
    BHhalos = findBHhalos(s)
    #sorting the halos, indexes/indecis are like an exact address
    currenthalo = np.argsort(BHhalos)
    print (BHhalos[currenthalo])

    for i in currenthalo:
    
        #which halo are we on?
        currenthalo = BHhalos[i]
        print ('current halo: ', currenthalo)
        print (i)
    
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

        #the .5 is the square root , this is the distance formula
        distance =((BHx**2)+(BHy**2)+(BHz**2))**(.5)
        print ("the distance is:", distance)

        starmass = h[currenthalo].s['mass'].sum()
        gasmass = h[currenthalo].g['mass'].sum()
        virialmass = starmass+gasmass+h[currenthalo].d['mass'].sum()
    
        data = [currenthalo, BH['iord'][i], gettime(s),getz(s), BH['mass'][i], BH['r'][i], starmass, gasmass, virialmass] 
        
        
        data= str(data)
        data= data[1:-1]
        f.write(data+'\n')
        t = BH['age']
        print(t)
        print (data)
         

with open('foundTL.txt' , 'w') as f:
    f.write("       |BH ID|          |Galaxy ID|   |Distance from Center|   \n") 
    for a,b,c in zip(BHid,BHhalos,dCen):
        f.write('{0:15}{1:15}         {2:.5}\n'.format(a,b,c))  
f.close()

"""
# Loading files
#files = ('/media/jillian/cptmarvel/cptmarvel.cosmo25cmb.4096g5HbwK1BH.orbit')
#files = ('/media/jillian/storm/storm.cosmo25cmb.4096g5HbwK1BH.orbit')
#files = ('/data/rogue/rogue.cosmo25cmb.4096g5HbwK1BH.orbit')
#files = ('/media/jillian/h148/h148.cosmo50PLK.3072g3HbwK1BH.orbit')
files = ('/media/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.orbit')

BHID=60353246

#h148=101863739,101864796
#243778457
#rogue307622464
#storm: 243778457,243771992
#cpt marvel:89425759

i =np.where(files[:,0]==  BHID)
#print (files[:,0][i])
# The following numbers are from the simulation
m_sol=  1.5928853e16 # justice league simulations
l_kpc = 50000
#m_sol = 2.31e15 # marvelous simulations
#l_kpc  = 25000 #marvelous simulations
timee = 38.78  # Time conversion: simulation units time to Gyr 
d_timee = 1.22386438e18 # Time conversion: simulation units to seconds
#t_square = d_time ^2
t_square = 1.49784401e36
m_g = 1.989e33 # Sun mass in gram
l_cm = 3.086e21 # kpc to cm

# delta energy
Denergy=( files[:,13][i]* m_sol*( l_kpc**2) *m_g *(l_cm**2))/t_square #units here are ergs
#delta time
Dtime = files[:,14][i]*d_timee
dEdt = Denergy/Dtime
Time=((files[:,1][i]))*timee
#print(Time)
#print(timee)
# Functions:

''' Create 2 parallel iterators (a,b) pointing to the first element of the original iterable.
The second iterator, b is moved 1 step forward (the next(b, None)) call).  a points to c0 and b points to c1.
Both a and b can traverse the original iterator independently - the izip function takes the two iterators and makes pairs 
of the returned elements, advancing both iterators at the same pace.'''

def pair(iterable):
    "c -> (c0,c1), (c1,c2), (c2, c3), ..." # This function creates ordered pairs 
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def float_range(start, stop, step):
  while start < stop:                 # Float Range function 
    yield float(start)
    start += decimal.Decimal(step)
    
#this is time interval from 0 to 13.8 Gyr with an interval of 0.01 which equals to 10 million years
intervals = pair(float_range(0,13.8,0.01))
# tmin,tmax for each time interval
centers = [(tmin+tmax)/2. for tmin, tmax in intervals]

def combining(Time,dEdt,intervals):          
                            # Calculate median valuea given intervals
    warnings.simplefilter("ignore")
    out = []

    for tmin, tmax in intervals:
        filter = (Time >= tmin) & (Time < tmax)
        out.append(np.mean(dEdt[filter]))
    return np.array(out)

b = len(intervals)
#print(centers)
#print(combining(Time, dEdt, intervals))
combined= combining(Time, dEdt, intervals)

filez = readcol.readcol('h229.dat',fsep=',')
ID=60353246
j= np.where(filez[:,1]==ID )
Time= filez[:,2][j]
BHmass = filez [:,4][j]
#BHmass=np.log10(mass.to_value(u.Msun))
BHDistance= filez[:,5][j]

fig, ax = plt.subplots(3,1,figsize=(10,20))
#fig, (axs1,axs2) = plt.subplots(2, 1)

ax[0].plot(Time, BHDistance, "k", linewidth=2)
#ax[0].set_xlabel("Time 'Gyr'")
ax[0].set_ylabel("BH Distance 'Kpc'")

ax[1].plot(Time, BHmass,"b", linewidth=2)
#ax[0].set_yscale('log')
#plt.yscale(u'log')
#axs[1].semilogy()
ax[1].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
#ax[1].set_xlabel("Time 'Gyr'")
ax[1].set_ylabel("BH Mass ")

ax[2].plot(centers,combined ,'ro', markersize=6) 
#plt.scatter(Time, dEdt)
ax[2].set_title(" $\Delta$E/$\Delta$t vs Time")
#plt.legend(loc = 'upper right')
ax[2].set_xlabel("Time(Gyrs)")
ax[2].set_ylabel("$\Delta$E/$\Delta$t(Erg/s)")
plt.yscale('log')
plt.ylim(10e35,10e38)

plt.subplots_adjust(left=None,bottom=None,right=None,top=0.8,wspace=None,hspace=None)

plt.savefig(filename='ruth.png')
plt.show()  """