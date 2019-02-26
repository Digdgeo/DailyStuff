
import landsatxplore.api
from landsatxplore.earthexplorer import EarthExplorer

api = landsatxplore.api.API('******', '*******')
ee = EarthExplorer('******', '******')

# Request
scenes = api.search(
    dataset='LANDSAT_8_C1',
    latitude=37.01,
    longitude=-5.93,
    start_date=m,
    end_date=t,
    max_cloud_cover=100)

print('{} scenes found.'.format(len(scenes)))

for scene in scenes:
    
    sc = scene['displayId']
    if scene['displayId'].split('_')[2] == '202034':
        print('downloading:', sc)
        ee.download(scene_id=sc, output_dir='/home/last/Descargas')
        
ee.logout()
api.logout()