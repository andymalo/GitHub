import folium
import pandas

map = folium.Map(location=[45.372, -121.6972], zoom_start=4, tiles='Stamen Terrain')
df = pandas.read_csv('Volcanoes-USA.txt', sep=',' )

def colorChoiceByElev(Elev):
    if Elev in range(0,1000):
        col = 'green'
    elif Elev in range(1000,3000):
        col = 'orange'
    else:
        col = 'red'
    return col

for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
    folium.Marker([lat,lon], popup= name, icon= folium.Icon(color = colorChoiceByElev(elev))).add_to(map)

map.save("test5.html")




