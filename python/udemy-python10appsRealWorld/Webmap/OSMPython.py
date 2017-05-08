import folium

print(dir(folium))

map = folium.Map(location=[45.372,-121.69],zoom_start=10)
print(map)

map.save('test.html')

map = folium.Map(location=[45.372,-121.697],zoom_start=10, tiles='Stamen Terrain')

map.save('test2.html')