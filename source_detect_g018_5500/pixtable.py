from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import interpolate



hdulist = fits.open('sfind_senmap.rms.fits')


scidata = hdulist[0].data

#print hdulist[0].header['CDELT1']
#print hdulist[0].header['CDELT2']

#print scidata.shape
#print scidata.dtype.name
#print(scidata[2356.9, 4726.9])
#print scidata[:, 4727]

#print scidata[0,:]
#print len(scidata[0,:])  #4727
#print len(scidata[:,0])  #2357


x_column=[]
y_column=[]
pixval=[]


for i in range(0,len(scidata[:,0])):

    for j in range(0,len(scidata[0,:])):
    
        x_column.append(i)
        y_column.append(j)
        pixval.append(scidata[i,j])

#print len(pixval)
#print len(x_column)
#print len(y_column)


#pix_table=np.column_stack((x_column, y_column, pixval))

#np.savetxt('./pix_table.cat', pix_table, delimiter=' ')

pixval.sort()


new_list = []
for value in pixval:
    if new_list and new_list[-1][0] == value:
        new_list[-1].append(value)
    else:
        new_list.append([value])


#print len(new_list[0])

#print new_list[0][0]
#print new_list[1][0]
#print new_list[2][0]
#print len(new_list[:][0])
#print new_list[278][0]
#print new_list[279][0]
#print new_list[280][0]
#print new_list[281][0]
#print new_list[-1][0]

#print new_list[:][0]
#print len(new_list)    # 7006 rows in your example
#print len(new_list[0]) # 280 columns in your example
#print len(new_list[34])
#print len(new_list[766])
#print len(new_list[455])
#print len(new_list[33])
#print len(new_list[6443])
#print len(new_list[5433])


pix_value=[]
pix_number=[]
for count in range(0,len(new_list)):

    pix_value.append(new_list[count][0])
    pix_number.append(len(new_list[count]))


pix_number_cum=np.cumsum(pix_number)
area_cum=pix_number_cum*(abs(hdulist[0].header['CDELT1']))*(abs(hdulist[0].header['CDELT2']))  #number--> deg^2

pix_value = np.array(pix_value)
pix_value=np.array([float(i) for i in pix_value])
pix_value=pix_value*1000.0 #from Jy --> mJy

pix_nubmer_table=np.column_stack((pix_value, pix_number, pix_number_cum, area_cum))

np.savetxt('./pix_nubmer_table.cat', pix_nubmer_table, delimiter=' ')




plt.plot(pix_value, area_cum)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Sensitivity (mJy)')
plt.ylabel('Cumulative Area (deg^2)')
plt.rc('font', size=30)  #==========================================================HERE (font size)
plt.grid(True)
#plt.legend()
#plt.title('')                                                                       #========================================================HERE
plt.show()









template_file = open("./flux_cumcounts_table.cat", "r")    #========================================================HERE
lines = template_file.readlines()
template_file.close()


flux_cumcounts_table=[]

for i in range(0, len(lines)):
    separated_lines=lines[i].split() 
    flux_cumcounts_table.append(separated_lines)


flux_cumcounts_table = np.array(flux_cumcounts_table)

flux_observed=flux_cumcounts_table[:,0]
cum_number_counts_observed=flux_cumcounts_table[:,1]

flux_observed = np.array(flux_observed)
flux_observed=np.array([float(i) for i in flux_observed])
cum_number_counts_observed = np.array(cum_number_counts_observed)
cum_number_counts_observed=np.array([float(i) for i in cum_number_counts_observed])



#print flux_observed
#print cum_number_counts_observed


interpolate_function_flux = interpolate.interp1d(pix_value, area_cum, bounds_error=False, fill_value=area_cum[-1])  #assume linear interpolation
area_cum_interp=[]
number_over_area=[]

for i_cum in range(0, len(cum_number_counts_observed)):

    area_cum_loop=interpolate_function_flux(flux_observed[i_cum])
    area_cum_interp.append(area_cum_loop)
    number_over_area.append(cum_number_counts_observed[i_cum]/area_cum_loop)



print area_cum_interp
print number_over_area
print flux_observed






#plt.plot(flux_observed, number_over_area)
plt.plot(flux_observed, number_over_area, '-o')
plt.xscale('log')
#plt.yscale('log')
plt.xlabel('Flux (mJy)')
plt.ylabel('Number Counts per Area (deg^-2)')
plt.rc('font', size=30)  #==========================================================HERE (font size)
plt.grid(True)
#plt.legend()
#plt.title('')                                                                       #========================================================HERE
plt.show()


