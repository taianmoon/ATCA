import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.cm as cm


S_avg=[8.5,12.0,17.0,24.0,34.0,49.0,68.0,96.0,135.0,206.0,368.0,589.0,1084.0,1802.0,2960.0,4367.0]  #micro-Jy

Nc_Nexp_literature=[0.0,0.0,0.0,0.0,0.0,0.85,0.91,1.35,1.25,1.46,1.6,4.96,5.25,7.2,14.45,11.11]  #1.0e-2
Nc_Nexp_literature_err=[0.0,0.0,0.0,0.0,0.0,0.2,0.25,0.25,0.29,0.33,0.51,1.28,2.07,3.47,7.01,7.58]  #1.0e-2

Nc_Nexp_us=np.array([0.0,0.0,0.0,0.17,1.082,2.379,1.87,1.694,0.95,0.0,0.0,0.0,0.0,0.0,62.63,0.0])  #1.0e-2
Nc_Nexp_us_err=np.array([0.0,0.0,0.0,0.17,0.54,1.06,0.84,0.55,0.9,0.0,0.0,0.0,0.0,0.0,62.63,0.0])  #1.0e-2

completeness = np.array([4.6666666666666666E-4,4.4E-4,3.733333333333333E-4,2.8E-4,2.4210526315789478E-4,3.9999999999999996E-4,6.0E-4,3.9999999999999996E-4,0.9754000000000034,0.9712000000000023,0.9686666666666696,0.961200000000004,0.9581333333333361,0.9568666666666688,0.9568666666666688,0.9568666666666688])
completeness_err = np.array([0.37796447300922725,0.3892494720807615,0.4225771273642583,0.48795003647426666,0.524749767832802,0.4082482904638631,0.3333333333333333,0.4082482904638631,0.008267286626178347,0.00828514347590038,0.008295970381447566,0.008328129877731776,0.008341447019563422,0.008346966251710258,0.008346966251710258,0.008346966251710258])
#Nc_Nexp_us_err_completeness = (Nc_Nexp_us/completeness)*completeness_err
Nc_Nexp_us_err_completeness = (Nc_Nexp_us/1.0)*completeness_err



plt.scatter(S_avg, Nc_Nexp_literature, color='r', label='Huynh et al. (2015)', s=100) #==========================================================HERE
plt.errorbar(S_avg, Nc_Nexp_literature, yerr=Nc_Nexp_literature_err, color='r', fmt='o', elinewidth=2.0, capsize=4.0, capthick=2.0) #==========================================================HERE

plt.scatter(S_avg, Nc_Nexp_us, color='b', label='C3088, this work', s=100, marker='s') #==========================================================HERE
#plt.errorbar(S_avg, Nc_Nexp_us, yerr=Nc_Nexp_us_err, color='b', fmt='o', elinewidth=2.0, capsize=4.0, capthick=2.0) #==========================================================HERE
plt.errorbar(S_avg, Nc_Nexp_us, yerr=Nc_Nexp_us_err_completeness, color='b', fmt='o', elinewidth=2.0, capsize=4.0, capthick=2.0) #==========================================================HERE

print 'ddddddddd'
print Nc_Nexp_us_err_completeness



plt.grid()
plt.xscale('log',nonposy='clip')
plt.yscale('log',nonposy='clip')
plt.xlabel(r'$S(6cm)$ [$\mu$Jy]')#==========================================================HERE
plt.ylabel(r'$N_c/N_{exp}$ [1x$10^{-2}$]')#==========================================================HERE
plt.rc('font', size=30)  #==========================================================HERE (font size)
plt.legend(loc=2)
plt.tick_params(width=2, length=16, which='major')
plt.tick_params(width=2, length=5, which='minor')


plt.show()




#r'$\alpha_i > \beta_i$'
