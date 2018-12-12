
import os
import rasterio
import numpy as np
from datetime import date



def get_escenas_values(path):

    '''Con este script, podemos calcualr el valor en días que le corresponde a una escena dentro de un ciclo 
    hidrológico. Con suerte, será la base para el cálculo del hidroperiodo'''
    
    
    escenas = [i[:8] for i in os.listdir(path) if i.endswith('.tif')]
    years = set([i[:4] for i in escenas])
    d0 = date(int(min(years)), 9, 1)
    #print(years)
    
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

    values.append(pcortes[0])
    for n in range(len(pcortes)-1):
        p = (pcortes[n+1] - pcortes[n])
        values.append(p)
    values.append(365-pcortes[-1])

    escenas_valor = dict(zip(sorted(escenas), values))
    
    return escenas_valor


def get_hydroperiod(path, values):
    
    escenas = [i for i in os.listdir(path) if i.endswith('.tif')]
        
    for i in sorted(escenas):
        rs = os.path.join(path, i)
        out = os.path.join(path, os.path.join('outputs', i[:-4] + '_rec.tif'))
        with rasterio.open(rs) as src:
            RS = src.read()
            RS[RS == 1] = get_escenas_values('/home/diego/Ecopotential/shapes/tests/rasters/')[i[:8]]
            print(i, RS.mean())
            
            profile = src.meta
            profile.update(dtype=rasterio.float32)

            with rasterio.open(out, 'w', **profile) as dst:
                dst.write(RS.astype(rasterio.float32))
