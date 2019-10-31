import matplotlib.pyplot as plt
#import glob
import numpy as np
import os.path
#from scipy import interpolate
#from scipy import integrate
import math



radius=[1.0,3.0,5.0,7.0,9.0,11.0,13.0,15.0,17.0,19.0,21.0]    #arcmin


radius = np.array(radius)
radius=np.array([float(i) for i in radius])

#def power(my_list):
#    return [ x**2 for x in my_list ]

area=[]
for i in range(0, len(radius)):
    area_loop=(math.pi*(radius[i])**2)/3600.0  #area in deg^2
    area.append(area_loop)


counts=[0.0,12.0,9.0,5.0,5.0,2.0,2.0,2.0,0.0,1.0,0.0]

counts_accum=[0.0,12.0,21.0,26.0,31.0,33.0,35.0,37.0,37.0,38.0,38.0]


counts = np.array(counts)
counts=np.array([float(i) for i in counts])
counts_accum = np.array(counts_accum)
counts_accum=np.array([float(i) for i in counts_accum])


fig = plt.figure()
ax1 = fig.add_subplot(111)





#ax2 = ax1.twiny()

ax1.plot(area,counts, label='counts', linewidth=4)

ax1.plot(area,counts_accum, label='cumulative counts', linewidth=4, color='g')

#ax2.plot(area, counts_accum)

#plt.title("")   
#ax1.set_xlabel("radius (arcmin)")
ax1.set_xlabel("area (deg^2)")
ax1.set_ylabel("Number of Sources")

ax1.legend(loc=2)
#ax2.legend(loc=2)



plt.rc('font', size=30)  #==========================================================HERE (font size)

plt.show()
