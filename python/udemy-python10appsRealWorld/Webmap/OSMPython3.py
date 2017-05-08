import folium
import pandas

map = folium.Map(location=[45.372, -121.6972], zoom_start=4, tiles='Stamen Terrain')
#folium.Marker([45.3288, -121.6625], popup='Mt. Hood Meadows').add_to(map_1)
#folium.Marker([45.3311, -121.7113], popup='Timberline Lodge').add_to(map_1)
#folium.Marker([45.3311, -121.2222], popup='Timberline 2').add_to(map_1)
#map_l.save("test3.html")

df = pandas.read_csv('Volcanoes-USA.txt', sep=',' )
print(df)

for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):


    folium.Marker([lat,lon], popup= name, icon= folium.Icon(color = 'green' if elev in range(0,1000)  else 'orange' if elev in range(1000,3000) else 'red')).add_to(map)

map.save("test3.html")




