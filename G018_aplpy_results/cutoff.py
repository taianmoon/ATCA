#DO FIRST
#import os
#os.system('export PATH=$PATH:$HOME/Downloads/montage/bin')

import pyfits
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math
import montage_wrapper as montage
from astropy.io import fits
import matplotlib.cm as cm
import aplpy


#========================================================HERE============================================


input_fits_image_band1='./input/SGP_mf_fbacksub_250_c.fits'  #=====250
input_fits_image_band2='./input/SGP_mf_fbacksub_350_c.fits'    #=====350
input_fits_image_band3='./input/SGP_mf_fbacksub_500_c.fits'  #=====500
input_fits_image_band4='./input/g018.fits'  #=====radio
#input_fits_image_band5='./input/G12v230_IRAC_Mosaic_36.fits'                            #=====3.6 micron
#input_fits_image_band6='./input/G12v230_IRAC_Mosaic_45.fits'                            #=====4.5 micron

band4_present=1  #=================================================================1:yes 0:no (I band)
band5_present=0  #=================================================================1:yes 0:no (3.6 band)
band6_present=0  #=================================================================1:yes 0:no (4.5 band)


#================================Load in fits table===============================================

names_cutoff = pyfits.open('./G018_matches_combined.fits')                            #========================================================HERE
names_cutoff_data = names_cutoff[1].data
X_WORLD_K= names_cutoff_data.field('ra')
Y_WORLD_K= names_cutoff_data.field('dec')
K_mag = names_cutoff_data.field('f250') #==================================================HERE note to correct column name
J_mag = names_cutoff_data.field('f350') #==================================================HERE note to correct column name
H_mag = names_cutoff_data.field('f500') #==================================================HERE note to correct column name
#I_mag = names_cutoff_data.field('f500') #==================================================HERE note to correct column name
NUMBER_K= names_cutoff_data.field('count') #double detection in ATCA
NUMBER_double= names_cutoff_data.field('GroupID') #double detection in ATCA

X_WORLD_radio= names_cutoff_data.field('col1')
Y_WORLD_radio= names_cutoff_data.field('col2')




#===============================make a webpage showing the cutoff images============================================



f=open('./cutoff_images.html','w+')

f.write('<!DOCTYPE html>\n')
f.write('<html>\n')
f.write('<head>\n')
f.write('\t<title>cutoff_images</title>\n')
f.write('</head>\n')
f.write('<body>\n')

f.write('<table border="1">')

f.write('<tr>')



f.write('<td>250 micron</td>')
f.write('<td>350 micron</td>')
f.write('<td>500 micron</td>')

if band4_present==1:
    f.write('<td>5.5 GHz</td>')

if band5_present==1:
    f.write('<td>3.6 micron image</td>')
if band6_present==1:
    f.write('<td>4.5 micron image</td>')

f.write('</tr>')

#==================to be continued in the loop=========================











#==============================do cutoff==========================================================

for counter_cutoff in range(len(X_WORLD_K)):

    try:
        montage.mSubimage(input_fits_image_band1, './output/cutoff_250_'+str(NUMBER_K[counter_cutoff])+'_'+str(counter_cutoff)+'.fits', ra=X_WORLD_K[counter_cutoff], dec=Y_WORLD_K[counter_cutoff], xsize=0.05)
    except:
        print '==problem in ks image=='
    try:
        montage.mSubimage(input_fits_image_band2, './output/cutoff_350_'+str(NUMBER_K[counter_cutoff])+'_'+str(counter_cutoff)+'.fits', ra=X_WORLD_K[counter_cutoff], dec=Y_WORLD_K[counter_cutoff], xsize=0.05)
    except:
        print '==problem in j image=='
    try:
        montage.mSubimage(input_fits_image_band3, './output/cutoff_500_'+str(NUMBER_K[counter_cutoff])+'_'+str(counter_cutoff)+'.fits', ra=X_WORLD_K[counter_cutoff], dec=Y_WORLD_K[counter_cutoff], xsize=0.05)
    except:
        print '==problem in h image=='


    if band4_present==1:
        try:
            montage.mSubimage(input_fits_image_band4, './output/cutoff_radio_'+str(NUMBER_K[counter_cutoff])+'_'+str(counter_cutoff)+'.fits', ra=X_WORLD_K[counter_cutoff], dec=Y_WORLD_K[counter_cutoff], xsize=0.05)
        except:
            print '==problem in i image=='

    if band5_present==1:
        try:
            montage.mSubimage(input_fits_image_band5, './output/cutoff_3p6_'+str(NUMBER_K[counter_cutoff])+'.fits', ra=X_WORLD_K[counter_cutoff], dec=Y_WORLD_K[counter_cutoff], xsize=0.0023)
        except:
            print '==problem in 3.6 micron image=='
    if band6_present==1:
        try:    
            montage.mSubimage(input_fits_image_band6, './output/cutoff_4p5_'+str(NUMBER_K[counter_cutoff])+'.fits', ra=X_WORLD_K[counter_cutoff], dec=Y_WORLD_K[counter_cutoff], xsize=0.0023)
        except:
            print '==problem in 4.5 micron image=='


#============================update cutoff images using aplpy=====================================================

    #cutoff_1=fits.open('./output/cutoff_ks_'+str(counter_cutoff)+'.fits')
    #cutoff_2=fits.open('./output/cutoff_j_'+str(counter_cutoff)+'.fits')
    #cutoff_3=fits.open('./output/cutoff_h_'+str(counter_cutoff)+'.fits')
    #cutoff_4=fits.open('./output/cutoff_i_'+str(counter_cutoff)+'.fits')

    #ax=plt.subplot(111)
    #ax.imshow(cutoff_1[0].data, cmap=cm.gist_heat)
    #plt.axis('off')
    #plt.savefig('./try.jpg')
    #plt.close()


    #cutoff_1.close()
    #cutoff_2.close()
    #cutoff_3.close()
    #cutoff_4.close()




    try:
        cutoff_1 = aplpy.FITSFigure('./output/cutoff_250_'+str(NUMBER_K[counter_cutoff])+'_'+str(counter_cutoff)+'.fits')
        cutoff_1.show_colorscale(cmap=cm.gist_heat, smooth=1)
        cutoff_1.show_markers(xw=[X_WORLD_K[counter_cutoff]], yw=[Y_WORLD_K[counter_cutoff]], marker='+', c='w')
        cutoff_1.show_markers(xw=[X_WORLD_radio], yw=[Y_WORLD_radio], marker='.', c='blue')
        cutoff_1.add_colorbar()
        cutoff_1.add_scalebar(5.0/1800.0)
        cutoff_1.scalebar.set_label('10"')
        cutoff_1.scalebar.set_color('white')
        #cutoff_1.add_beam()
        #cutoff_1.beam.set_color('white')
        #cutoff_1.beam.set_hatch('+')
        cutoff_1.set_title('#'+str(NUMBER_K[counter_cutoff])+';  RA='+str(X_WORLD_K[counter_cutoff])+';  Dec='+str(Y_WORLD_K[counter_cutoff])+';  f250='+str(K_mag[counter_cutoff]))
        cutoff_1.save('./output/cutoff_250_'+str(NUMBER_K[counter_cutoff])+'_'+str(counter_cutoff)+'.jpg')
    except:
        print '============='

    try:
        cutoff_2 = aplpy.FITSFigure('./output/cutoff_350_'+str(NUMBER_K[counter_cutoff])+'_'+str(counter_cutoff)+'.fits')
        cutoff_2.show_colorscale(cmap=cm.gist_heat, smooth=1)
        cutoff_2.show_markers(xw=[X_WORLD_K[counter_cutoff]], yw=[Y_WORLD_K[counter_cutoff]], marker='+', c='w')
        cutoff_2.show_markers(xw=[X_WORLD_radio], yw=[Y_WORLD_radio], marker='.', c='blue')
        cutoff_2.add_colorbar()
        cutoff_2.add_scalebar(5.0/1800.0)
        cutoff_2.scalebar.set_label('10"')
        cutoff_2.scalebar.set_color('white')
        #cutoff_1.add_beam()
        #cutoff_1.beam.set_color('white')
        #cutoff_1.beam.set_hatch('+')
        cutoff_2.set_title('#'+str(NUMBER_K[counter_cutoff])+';  RA='+str(X_WORLD_K[counter_cutoff])+';  Dec='+str(Y_WORLD_K[counter_cutoff])+';  f350='+str(J_mag[counter_cutoff]))
        cutoff_2.save('./output/cutoff_350_'+str(NUMBER_K[counter_cutoff])+'_'+str(counter_cutoff)+'.jpg')
    except:
        print '============='

    try:
        cutoff_3 = aplpy.FITSFigure('./output/cutoff_500_'+str(NUMBER_K[counter_cutoff])+'_'+str(counter_cutoff)+'.fits')
        cutoff_3.show_colorscale(cmap=cm.gist_heat, smooth=1)
        cutoff_3.show_markers(xw=[X_WORLD_K[counter_cutoff]], yw=[Y_WORLD_K[counter_cutoff]], marker='+', c='w')
        cutoff_3.show_markers(xw=[X_WORLD_radio], yw=[Y_WORLD_radio], marker='.', c='blue')
        cutoff_3.add_colorbar()
        cutoff_3.add_scalebar(5.0/1800.0)
        cutoff_3.scalebar.set_label('10"')
        cutoff_3.scalebar.set_color('white')
        #cutoff_1.add_beam()
        #cutoff_1.beam.set_color('white')
        #cutoff_1.beam.set_hatch('+')
        cutoff_3.set_title('#'+str(NUMBER_K[counter_cutoff])+';  RA='+str(X_WORLD_K[counter_cutoff])+';  Dec='+str(Y_WORLD_K[counter_cutoff])+';  f500='+str(H_mag[counter_cutoff]))
        cutoff_3.save('./output/cutoff_500_'+str(NUMBER_K[counter_cutoff])+'_'+str(counter_cutoff)+'.jpg')
    except:
        print '============='

    try:
        if band4_present==1:
            cutoff_4 = aplpy.FITSFigure('./output/cutoff_radio_'+str(NUMBER_K[counter_cutoff])+'_'+str(counter_cutoff)+'.fits')
            cutoff_4.show_colorscale(cmap=cm.gist_heat, smooth=1)
            cutoff_4.show_markers(xw=[X_WORLD_K[counter_cutoff]], yw=[Y_WORLD_K[counter_cutoff]], marker='+', c='w')
            cutoff_4.show_markers(xw=[X_WORLD_radio], yw=[Y_WORLD_radio], marker='.', c='blue')
            cutoff_4.add_colorbar()
            cutoff_4.add_scalebar(5.0/1800.0)
            cutoff_4.scalebar.set_label('10"')
            cutoff_4.scalebar.set_color('white')
            #cutoff_1.add_beam()
            #cutoff_1.beam.set_color('white')
            #cutoff_1.beam.set_hatch('+')
            cutoff_4.set_title('#'+str(NUMBER_K[counter_cutoff])+';  RA='+str(X_WORLD_K[counter_cutoff])+';  Dec='+str(Y_WORLD_K[counter_cutoff])+';  Double Detected Group:'+str(NUMBER_double[counter_cutoff]))
            cutoff_4.save('./output/cutoff_radio_'+str(NUMBER_K[counter_cutoff])+'_'+str(counter_cutoff)+'.jpg')
    except:
        print '============='

    try:
        if band5_present==1:
            cutoff_5 = aplpy.FITSFigure('./output/cutoff_3p6_'+str(NUMBER_K[counter_cutoff])+'.fits')
            cutoff_5.show_colorscale(cmap=cm.gist_heat, smooth=1)
            cutoff_5.show_markers(xw=[X_WORLD_K[counter_cutoff]], yw=[Y_WORLD_K[counter_cutoff]], marker='+', c='w')
            cutoff_5.add_colorbar()
            cutoff_5.add_scalebar(1.0/1800.0)
            cutoff_5.scalebar.set_label('2"')
            cutoff_5.scalebar.set_color('white')
            #cutoff_1.add_beam()
            #cutoff_1.beam.set_color('white')
            #cutoff_1.beam.set_hatch('+')
            cutoff_5.set_title('#'+str(NUMBER_K[counter_cutoff])+';  RA='+str(X_WORLD_K[counter_cutoff])+';  Dec='+str(Y_WORLD_K[counter_cutoff])+';  3.6 micron')
            cutoff_5.save('./output/cutoff_3p6_'+str(NUMBER_K[counter_cutoff])+'.jpg')
    except:
        print '============='

    try:
        if band6_present==1:
            cutoff_6 = aplpy.FITSFigure('./output/cutoff_4p5_'+str(NUMBER_K[counter_cutoff])+'.fits')
            cutoff_6.show_colorscale(cmap=cm.gist_heat, smooth=1)
            cutoff_6.show_markers(xw=[X_WORLD_K[counter_cutoff]], yw=[Y_WORLD_K[counter_cutoff]], marker='+', c='w')
            cutoff_6.add_colorbar()
            cutoff_6.add_scalebar(1.0/1800.0)
            cutoff_6.scalebar.set_label('2"')
            cutoff_6.scalebar.set_color('white')
            #cutoff_1.add_beam()
            #cutoff_1.beam.set_color('white')
            #cutoff_1.beam.set_hatch('+')
            cutoff_6.set_title('#'+str(NUMBER_K[counter_cutoff])+';  RA='+str(X_WORLD_K[counter_cutoff])+';  Dec='+str(Y_WORLD_K[counter_cutoff])+';  4.5 micron')
            cutoff_6.save('./output/cutoff_4p5_'+str(NUMBER_K[counter_cutoff])+'.jpg')
    except:
        print '============='





#===============================make a webpage showing the cutoff images (continued)============================================





    f.write('<tr>')




    f.write('<td>')
    f.write('<a href="./output/cutoff_250_'+str(NUMBER_K[counter_cutoff])+'_'+str(counter_cutoff)+'.jpg" target="_blank"><img src="./output/cutoff_250_'+str(NUMBER_K[counter_cutoff])+'_'+str(counter_cutoff)+'.jpg" alt="./output/cutoff_250_'+str(NUMBER_K[counter_cutoff])+'_'+str(counter_cutoff)+'.jpg" width="600" height="450"></a>')
    f.write('</td>')

    f.write('<td>')
    f.write('<a href="./output/cutoff_350_'+str(NUMBER_K[counter_cutoff])+'_'+str(counter_cutoff)+'.jpg" target="_blank"><img src="./output/cutoff_350_'+str(NUMBER_K[counter_cutoff])+'_'+str(counter_cutoff)+'.jpg" alt="./output/cutoff_350_'+str(NUMBER_K[counter_cutoff])+'_'+str(counter_cutoff)+'.jpg" width="600" height="450"></a>')
    f.write('</td>')

    f.write('<td>')
    f.write('<a href="./output/cutoff_500_'+str(NUMBER_K[counter_cutoff])+'_'+str(counter_cutoff)+'.jpg" target="_blank"><img src="./output/cutoff_500_'+str(NUMBER_K[counter_cutoff])+'_'+str(counter_cutoff)+'.jpg" alt="./output/cutoff_500_'+str(NUMBER_K[counter_cutoff])+'_'+str(counter_cutoff)+'.jpg" width="600" height="450"></a>')
    f.write('</td>')


    if band4_present==1:
        f.write('<td>')
        f.write('<a href="./output/cutoff_radio_'+str(NUMBER_K[counter_cutoff])+'_'+str(counter_cutoff)+'.jpg" target="_blank"><img src="./output/cutoff_radio_'+str(NUMBER_K[counter_cutoff])+'_'+str(counter_cutoff)+'.jpg" alt="./output/cutoff_radio_'+str(NUMBER_K[counter_cutoff])+'_'+str(counter_cutoff)+'.jpg" width="600" height="450"></a>')
        f.write('</td>')

    if band5_present==1:
        f.write('<td>')
        f.write('<a href="./output/cutoff_3p6_'+str(NUMBER_K[counter_cutoff])+'.jpg" target="_blank"><img src="./output/cutoff_3p6_'+str(NUMBER_K[counter_cutoff])+'.jpg" alt="./output/cutoff_3p6_'+str(NUMBER_K[counter_cutoff])+'.jpg" width="600" height="450"></a>')
        f.write('</td>')

    if band6_present==1:
        f.write('<td>')
        f.write('<a href="./output/cutoff_4p5_'+str(NUMBER_K[counter_cutoff])+'.jpg" target="_blank"><img src="./output/cutoff_4p5_'+str(NUMBER_K[counter_cutoff])+'.jpg" alt="./output/cutoff_4p5_'+str(NUMBER_K[counter_cutoff])+'.jpg" width="600" height="450"></a>')
        f.write('</td>')


    f.write('</tr>')







f.write('</table>')

f.write('</body>\n')
f.write('</html>')
f.close()















