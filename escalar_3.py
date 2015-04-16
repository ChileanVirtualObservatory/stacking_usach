"""
This file is part of ChiVO, the Chilean Virtual Observatory
A project sponsored by FONDEF (D11I1060)
Copyright (C) 2015 Universidad Tecnica Federico Santa Maria
                   Universidad de Chile
                   Pontificia Universidad Catolica
                   Universidad de Concepcion
                   Universidad de Santiago

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""
#!/usr/bin/python

import numpy as np
import math
import info_imagen

def escalar(matriz, NAXIS1, NAXIS2, razon):
    
    # ------- S I  R A Z O N  E S   1  N O   S E   E S C A L A --------
    if (razon == 1):
        return matriz

    
    if ( razon < 1):
        # ----------- E N C O G E R     I M A G E N ------------
        matriz_final = np.zeros((round((NAXIS1-1)*razon+1),round((NAXIS2-1)*razon+1)))
        for x in range(NAXIS1):
            for y in range(NAXIS2):
                matriz_final[round(x*razon)][round(y*razon)] = matriz[x][y]
        return matriz_final
    else:
        # ----------- A G R A N D A R   I M A G E N ------------
        matriz_final = np.zeros(((NAXIS1-1)*round(razon)+1,(NAXIS2-1)*round(razon)+1))
        for x in range(NAXIS1):
            for y in range(NAXIS2):
                matriz_final[x*round(razon)][y*round(razon)] = matriz[x][y]

    x = y = 0
    razon = int(round(razon))

    # ------- I N T E R P O L A C I O N    P R O P I A M E N T E   T A L -----------
    # 1 Calculamos los porcentajes los cuales son constantes, el calculo se realiza desde (0,0) a (razon, razon)
    
    porcentajes = []
    for i in range(razon+1):
        for j in range(razon+1):
            if i == 0 and j == 0 or i == 0 and j == razon or i == razon and j == 0 or i == razon and j == razon:
                continue
            else:
                suma_distancias = info_imagen.distancia(i,j,0,0) + info_imagen.distancia(i,j,razon,0) + info_imagen.distancia(i,j,0,razon) + info_imagen.distancia(i,j,razon,razon)
                porcentajes.append(info_imagen.distancia(i,j,razon,razon)/suma_distancias)
                porcentajes.append(info_imagen.distancia(i,j,razon,0)/suma_distancias)
                porcentajes.append(info_imagen.distancia(i,j,0,razon)/suma_distancias)
                porcentajes.append(info_imagen.distancia(i,j,0,0)/suma_distancias)

    posicion_vector = 0
    while x < (NAXIS1-1)*razon:
        while y < (NAXIS2-1)*razon:

            pos = [x,y,x+razon,y,x,y+razon,x+razon,y+razon]
                                   
            for i in range(x,x+razon+1):
                for j in range(y,y+razon+1):

                    if( i == pos[0] and j == pos[1] or i == pos[2] and j == pos[3] or i == pos[4] and j == pos[5] or i == pos[6] and j == pos[7]):
                        continue
                                   
                    matriz_final[i][j] = matriz[x][y] * porcentajes[posicion_vector] + matriz[x][y+razon-1] * porcentajes[posicion_vector+1] + matriz[x+razon-1][y] * porcentajes[posicion_vector+2] + matriz[x+razon-1][y+razon-1] * porcentajes[posicion_vector+3]
                    posicion_vector +=4
                                   
            y = y + razon
        y = 0
        x = x + razon
    
    return matriz_final
