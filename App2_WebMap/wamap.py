import folium

map = folium.Map(location=[48.0020547,-122.220774], zoom_start=12, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="Wa Map")
fg.add_child(folium.Marker(location=[48.0006705,-122.2173022], popup="Port of Everett", icon=folium.Icon(color="green")))
map.add_child(fg)

map.save("WaMap.html")