"""
This file is part of ChiVO
Copyright (C) Rodrigo Jara

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

def recortar(matriz, borde):
    fila_mayor = 0
    fila_menor = borde[0]
    columna_mayor = 0
    columna_menor = borde[1]

    for i in range(len(borde)-1):

        if i % 2 != 0:
            continue
        if fila_mayor < borde[i]:
            fila_mayor = borde[i]
        if fila_menor > borde[i]:
            fila_menor = borde[i]
        if columna_mayor < borde[i+1]:
            columna_mayor = borde[i+1]
        if columna_menor > borde[i+1]:
            columna_menor = borde[i+1]

    for i in range(len(borde)-1):

        if i % 2 != 0:
            continue
        borde[i] = borde[i] - fila_menor
        borde[i+1] = borde[i+1] - columna_menor


    matriz_final = np.zeros((fila_mayor - fila_menor + 1, columna_mayor - columna_menor + 1))

    for i in range(fila_menor, fila_mayor+1):
        for j in range(columna_menor, columna_mayor+1):
            matriz_final[i - fila_menor][j - columna_menor] = matriz[i][j]

    return matriz_final
