
import os

def Mosaic(*args):
    
    #Create the dicts to store the path for every bands
    d = {}
    
    #Read the data and write the dicts
    for i in args:
        
        escena = i.split('_')[4] + '_' + i.split('_')[3]
        #print(escena)
        for banda in os.listdir(i):
            if banda.endswith('.TIF'): #and not 'BQA' in banda: #and not 'BQA' in banda:
                b = banda.split('_')[-1].split('.')[0]
                d[b] = []
                        
    for i in args:
        
        #escena = i.split('_')[4] + '_' + i.split('_')[3]
        #print(escena)
        for banda in os.listdir(i):
            if banda.endswith('.TIF'): #and not 'BQA' in banda:
                print(banda)
                b = banda.split('_')[-1].split('.')[0]
                d[b].append(os.path.join(i, banda))
    
    for k, v in d.items():
        str1 = ' '.join(v)
        print(str1)
        
        output = os.path.join('/media/diego/datos_linux/FranHP/Mosaic', v[0].split('_')[4] + '_Mos_' + k + '.TIF') #+ i.split('_')[3]
        #print(output)
        
        os.system('gdal_merge.py -n 0 {} -o {}'.format(str1, output))
        
