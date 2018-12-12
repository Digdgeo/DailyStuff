

import os
import numpy as np
from datetime import date


def get_escenas_values(path):

    '''Con este script, podemos calcualr el valor en días que le corresponde a una escena dentro de un ciclo 
    hidrológico. Con suerte, será la base para el cálculo del hidroperiodo'''
    
    
    escenas = [i[:8] for i in os.listdir(path) if i.endswith('.shp')]
    years = set([i[:4] for i in escenas])
    d0 = date(int(years), 9, 1)
    
    ndays = []
    nmeds = []
    pcortes = []
    values = []
    
    for i in sorted(escenas):
        escenaF = [int(i[:4]), int(i[4:6]), int(i[6:8])]
        d1 = date(escenaF[0], escenaF[1], escenaF[2])
        delta = d1 - d0
        ndays.append(delta.days)
    
    for n in range(len(ndays)-1):    
        p = (ndays[n+1] - ndays[n])/2
        nmeds.append(p)

    for n, e in enumerate(nmeds):
        pcortes.append(e + ndays[n])

    for n in range(len(pcortes)-1):
        p = (pcortes[n+1] - pcortes[n])
        values.append(p)

    escenas_valor = dict(zip(sorted(escenas), values))
    
    return escenas_valor
