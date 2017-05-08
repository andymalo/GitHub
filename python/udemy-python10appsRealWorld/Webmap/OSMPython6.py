import folium
import pandas

df = pandas.read_csv('Volcanoes-USA.txt', sep=',' )

map = folium.Map(location=[df['LAT'].mean(),df['LON'].mean()], zoom_start=6, tiles='Mapbox bright')

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

fg = folium.FeatureGroup(name="Volcano_Locations")

for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
    fg.add_child(folium.Marker(location=[lat,lon], popup= name, icon= folium.Icon(color = colorChoiceByElev(elev), icon_color='green')))

map.add_child(fg)

map.add_child(folium.GeoJson(data=open('convert.json'),
                             name='World Population',
                             style_function=lambda x: {'fillColor:':'green' if x['properties']['POP2005']<=10000000 else 'orange' if 10000000 < x['properties']['POP2005']<2000000 else 'red'}))

map.add_child(folium.LayerControl())

map.save("test7.html")



