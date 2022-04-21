import json
from country_codes import get_country_code
from pygal.maps.world import World
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS


# read the file
filename = 'global_gdp.json'

with open(filename) as f:
	gdp_data = json.load(f)

# build a dictionary of gdp data in 2014
cc_gdp = {}

for gdp_dict in gdp_data:
	if gdp_dict['Year'] == '2014':
		country_name = gdp_dict['Country Name']
		gdp_value = int(float(gdp_dict['Value']))
		code = get_country_code(country_name)
		if code:
			cc_gdp[code] = gdp_value
		else:
			print("ERROR - " + country_name)


# group the gdp into 3 levels
gdp_1, gdp_2, gdp_3 = {}, {}, {}
for code, gdp in cc_gdp.items():
	if gdp < 100000000000:
		gdp_1[code] = gdp
	elif gdp < 10000000000000:
		gdp_2[code] = gdp 
	else:
		gdp_3[code] = gdp

# see how many countries are in each level
print(len(gdp_1), len(gdp_2), len(gdp_3))

# draw the gdp world map
wm_style = RS('#336699', base_style=LCS)
wm = World(style=wm_style)
wm.title = 'GDP in 2014, by Country'
wm.add('0-100bn', gdp_1)
wm.add('100bn-1tn', gdp_2)
wm.add('>1tn', gdp_3)

wm.render_to_file('world_gdp.svg')













