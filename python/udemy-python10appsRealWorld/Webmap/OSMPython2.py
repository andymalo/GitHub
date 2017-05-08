import folium

map_1 = folium.Map(location=[45.372, -121.6972], zoom_start=12, tiles='Stamen Terrain')

folium.Marker([45.3288, -121.6625], popup='Mt. Hood Meadows').add_to(map_1)
folium.Marker([45.3311, -121.7113], popup='Timberline Lodge').add_to(map_1)
folium.Marker([45.3311, -121.2222], popup='Timberline 2').add_to(map_1)

map_1.save("OSMPython2.html")