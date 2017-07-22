# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 16:53:21 2016

@author: Marco
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import matplotlib.patches as patches

#%reset #si quiero resetear todas las variables

#temp = np.array([22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44])
#interior = np.array([222.4, 241.8, 261.8, 280.8, 301.3, 320.2, 340.0, 359.4, 379.5, 398.9, 419.8, 439.5])
#edfa = np.array([221.3, 241.7, 262.4, 280.4, 301.8, 320.7, 341.0, 360.7, 381.4, 401.4, 420.5, 440.4])
#apd = np.array([210.5, 230.4, 250.8, 270.3, 290.2, 309.4, 329.3, 349.1, 369.1, 388.9, 408.6, 428.7])
#ext = np.array([210.3, 230.3, 250.3, 270.0, 290.0, 310.2, 330.0, 349.9, 369.8, 389.7, 409.6, 429.3])

     




temp, Hmedia, Mmedia  = np.loadtxt('out_file.txt', usecols=range(0,3),unpack=True, skiprows=9) #carga los datos del archivo. El unpack=True transpone los datos para sacarlos facil como x,y=cols

fig = plt.figure()
ax1 = fig.add_subplot(1,2,1) #cantidad de graficos en por columnas, filas y el útlimo es el número de gráfico donde aparece el gráfico ax1.
ax2 = fig.add_subplot(1,2,2)

#ax1.plot(temp, z,'.b', label = u'Presión')

#ax2.plot(tiempo, temp,'.r', label = 'Temperatura')


#legend(numpoints=1) #hace que muestre los legends markers una sola vez

#h1, l1 = ax1.get_legend_handles_labels() #agarra los parametros del legend de la 1era curva
#h2, l2 = ax2.get_legend_handles_labels() #agarra los parametros del legend de la 2da curva
#ax1.legend(h1+h2, l1+l2, loc=3, numpoints=1) #hace el legend para las diferentes curvas

   
#ax2.legend(loc=0) #es necesario para que te muestre los labels de las curvas
#ax1.legend(loc=4) #si pones los legends de esta manera los ubica por separado en alguna posición (i=1,2,...)

###############################################################################
#############################Cambiar el color de la curva######################
###############################################################################

#cmap=plt.cm.autumn #donde autumn es el colormap, dsps definis color = valor entre 0 y 1

###############################################################################
###############################################################################
###############################################################################

# for tl in ax2.get_yticklabels(): #cambia el color de los y-ticks
#     tl.set_color('r')
# for tl in ax1.get_yticklabels():
#     tl.set_color('b')


# tg = (1/30.)*zg + 20

# zextra = np.arange(1035,1100)
# textra = (1/30.)*zextra + 20



ax1.plot(temp, Hmedia, label = 'Hmedia')
ax2.plot(temp, Mmedia, label = 'Mmedia')
#ax1.plot(temp,z,'.',  markersize=1)
# plt.axhline(y=1000,c='black',lw=0.5)
# plt.axhline(y=1005,c='black',lw=0.5)
# plt.axhline(y=1030,c='black',lw=0.5)
# plt.axhline(y=1035,c='black',lw=0.5)

ax1.legend(numpoints=1)
ax1.set_xlabel('Temperatura')
ax1.set_ylabel(u'Hmedia')
ax1.grid(color='lightgrey', linestyle='-.')


ax2.legend(numpoints=1)
ax2.set_xlabel('Temperatura')
ax2.set_ylabel(u'Mmedia')
ax2.grid(color='lightgrey', linestyle='-.')



fig.tight_layout() # Para que no pisen los graficos

# ax1.add_subplot(111, aspect='equal')
# for p in [
#     patches.Rectangle(
#         (0.03, 0.1), 0.2, 0.6,
#         alpha=None,
#     ),
#     patches.Rectangle(
#         (0.26, 0.1), 0.2, 0.6,
#         alpha=1.0
#     ),
#     patches.Rectangle(
#         (0.49, 0.1), 0.2, 0.6,
#         alpha=0.6
#     ),
#     patches.Rectangle(
#         (0.72, 0.1), 0.2, 0.6,
#         alpha=0.1
#     ),
# ]:
#     ax5.add_patch(p)


plt.show()