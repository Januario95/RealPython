import folium
import pandas as pd

political_countries_url = (
	'http://geojson.xyz/naturalearth-3.3.0/ne_50m_admin_0_countries.geojson'
)

df = pd.read_csv('footprint.csv')
max_eco_footprint = df["Ecological footprint"].max()

m = folium.Map(
	location=(49.25, -123.12),
	zoom_start=3,
	tiles='cartodb positron'
)
folium.Choropleth(
	geo_data=political_countries_url,
	data=df,
	columns=["Country/region", "Ecological footprint"],
	key_on='feature.properties.name',
	bins=[0, 1, 1.5, 2, 3, 4, 5, 6, 7, 8, max_eco_footprint],
	fill_color='RdYlGn_r',
	fill_opacity=0.8,
	line_opacity=0.3,
	nan_fill_color='white',
	legend_name='Ecological footprint per capita',
	name="Countries by ecological footprint per capita",
).add_to(m)
folium.LayerControl().add_to(m)
# folium.GeoJson(political_countries_url).add_to(m)
m.save('footprint.html')

