import geopandas as gpd
import matplotlib.pyplot as plt

data_url = 'https://raw.githubusercontent.com/jcanalesluna/bcn-geodata/master/districtes/districtes.geojson'
districts = gpd.read_file(data_url)

ax = districts.plot(column='NOM',figsize=(10,6),legend=True)
plt.show()