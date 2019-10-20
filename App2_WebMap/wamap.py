import folium
import pandas

map = folium.Map(location=[42.0020547,-120.220774], zoom_start=5, tiles="Stamen Terrain")
vdata = pandas.read_csv("Volcanoes.txt")
lat = list(vdata["LAT"])
lon = list(vdata["LON"])
elv = list(vdata["ELEV"])
name = list(vdata["NAME"])

fg = folium.FeatureGroup(name="Wa Map")

for lt, ln, el, na in zip(lat, lon, elv, name):
    fg.add_child(folium.Marker(location=[lt,ln], popup="<span style='display: inline; width:200px; height:25px'>"+na + "<br/>Elevation " +str(el)+"</span>", icon=folium.Icon(color="green")))


map.add_child(fg)
map.save("WaMap.html")