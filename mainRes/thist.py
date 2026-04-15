import numpy as np
import matplotlib.pyplot as plt
import pynbody
import scipy.stats 
import pynbody.analysis.cosmology as cosmo

# Define directories and files
file = "/mnt/data0/jillian/h568/productionrun2023/h568.cosmo75.4096gsHsbBH.starlog"
s = pynbody.snapshot.tipsy.StarLog(file)
s.physical_units()

#blackhole = np.where(s['tform'] < 0.0)
#tBH = s[blackhole[0]]['tform']

tBH = -s['tform'][s['tform'] < 0.0]
tBH = tBH.in_units('Gyr')

#cosmo_obj = s.properties
#zBH= np.array([cosmo.redshift_from_time(cosmo_obj,t)for t in tBH])
try:
    zBH = cosmo.redshift(s, tBH)
except Exception as e:
    print(f"Error calculating redshift: {e}")
    zBH= [cosmo.redshift(s, t) for t in tBH]

print("zBH- ", zBH)
print(s['tform'].units)

#zBH = [11.80371496 11.6348144  11.4004107  11.36530628 11.2273333  11.21035611 11.21035611 10.8198158  10.7731691  10.74232572 10.7116834  10.62094202 10.62094202 10.56141552 10.5466526  10.51726751 10.51726751 10.44461481 10.44461481 10.38731052 10.38731052 10.38731052 10.35892602 10.28873125 10.27482197 10.21961002 10.20591229 10.17864171 10.13804501 10.12459442 10.08448486]
#plt.figure(figsize(8,6))
plt.hist(zBH, bins =25, color='white', edgecolor='black', alpha=0.5, )
plt.gca().invert_xaxis()
plt.xlabel("Redshift")
plt.ylabel("BH Formation Time")

plt.show()