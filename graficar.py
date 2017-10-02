# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 16:53:21 2016

@author: Fede
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import matplotlib.patches as patches

#%reset #si quiero resetear todas las variables

temp, Hmedia, Mmedia  = np.loadtxt('out_file.txt', usecols=range(0,3),unpack=True, skiprows=9) #carga los datos del archivo. El unpack=True transpone los datos para sacarlos facil como x,y=cols

fig = plt.figure()
ax1 = fig.add_subplot(1,2,1) #cantidad de graficos por columnas, filas y el útlimo es el número de gráfico donde aparece el gráfico ax1.
ax2 = fig.add_subplot(1,2,2)

####################################################################################################################

###
# Manejar el legend de las figuras
###

#legend(numpoints=1) #hace que muestre los legends markers una sola vez

#h1, l1 = ax1.get_legend_handles_labels() #agarra los parametros del legend de la 1era curva
#h2, l2 = ax2.get_legend_handles_labels() #agarra los parametros del legend de la 2da curva
#ax1.legend(h1+h2, l1+l2, loc=3, numpoints=1) #hace el legend para las diferentes curvas

#ax1.legend(loc=4) #si pones los legends de esta manera los ubica por separado en alguna posición (i=1,2,...)
#ax2.legend(loc=0) #es necesario para que te muestre los labels de las curvas


###
# Cambiar el color de la curva
###

#cmap=plt.cm.autumn #donde autumn es el colormap, dsps definis color = valor entre 0 y 1


####################################################################################################################


# for tl in ax2.get_yticklabels(): #cambia el color de los y-ticks
#     tl.set_color('r')
# for tl in ax1.get_yticklabels():
#     tl.set_color('b')

###
# Setear ejes y grid
###

ax1.legend(numpoints=1)
ax1.set_xlabel('Temperatura')
ax1.set_ylabel(u'Hmedia')
ax1.set_xlim([0,100])
ax1.set_ylim([0,100])
ax1.grid(color='lightgrey', linestyle='-.')

ax2.legend(numpoints=1)
ax2.set_xlabel('Temperatura')
ax2.set_ylabel(u'Mmedia')
ax2.grid(color='lightgrey', linestyle='-.')


fig.tight_layout() # Para que no pisen los graficos

####################################################################################################################

###
# Agregar lineas horizontales y rectangulos semitransparentes
###

# plt.axhline(y=1000,c='black',lw=0.5)
# plt.axhline(y=1005,c='black',lw=0.5)
# plt.axhline(y=1030,c='black',lw=0.5)
# plt.axhline(y=1035,c='black',lw=0.5)



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

####################################################################################################################

###
#Graficar
###


ax1.plot(temp, Hmedia, label = u'Presión','.',  markersize=1) # El u antes del label está para que tome los acentos
ax2.plot(temp, Mmedia, label = 'Mmedia')






plt.show()
