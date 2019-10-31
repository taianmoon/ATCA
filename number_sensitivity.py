import pyfits
import matplotlib.pyplot as plt
import numpy as np
import math



names_wht = pyfits.open('./G018_detected_sources_cat_161201.fits')                            #========================================================HERE
names_wht_data = names_wht[1].data
flux= names_wht_data.field('col7')
flux_err = names_wht_data.field('col12')


flux = np.array(flux)
flux_err = np.array(flux_err)

flux=np.array([float(i) for i in flux])
flux_err=np.array([float(i) for i in flux_err])


flux_err_array=np.column_stack((flux,flux_err))

#print flux_err_array


flux.sort()
flux=flux[::-1]

#print flux

#print len(flux)


number_array=list(range(len(flux)))

#print number_array

number_array_upd=[]

for i in range(0, len(number_array)):

    number_array_upd.append(number_array[i]+1.0)

#print number_array_upd

number_array_upd = np.array(number_array_upd)
number_array_upd=np.array([float(i) for i in number_array_upd])


print number_array_upd
print flux

table_to_be_saved=np.column_stack((flux,number_array_upd))
np.savetxt('./flux_cumcounts_table.cat', table_to_be_saved, delimiter=' ')

plt.plot(flux, number_array_upd, '-o')
plt.xscale('log')
#plt.yscale('log')
plt.xlim([0.0,4.0])
plt.yticks(np.arange(min(number_array_upd)-1, max(number_array_upd)+3, 5.0))
plt.grid()
plt.xlabel('Flux (mJy)')
plt.ylabel('Cumulative number counts')
plt.rc('font', size=30)  #==========================================================HERE (font size)
plt.show()


