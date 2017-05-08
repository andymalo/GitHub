import folium
import pandas

df = pandas.read_csv('Volcanoes-USA.txt', sep=',' )

map = folium.Map(location=[df['LAT'].mean(),df['LON'].mean()], zoom_start=6, tiles='Stamen Terrain')

def colorChoiceByElev(Elev):

    minimum = int(min(df['ELEV']))
    step = int((max(df['ELEV'])-min(df['ELEV']))/3)

    if Elev in range(minimum,minimum+step):
        col = 'green'
    elif Elev in range(minimum+step,minimum+step*2):
        col = 'orange'
    else:
        col = 'red'
    return col

for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
    folium.Marker([lat,lon], popup= name, icon= folium.Icon(color = colorChoiceByElev(elev))).add_to(map)

map.save("test5.html")




