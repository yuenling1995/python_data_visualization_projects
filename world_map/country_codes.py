from pygal.maps.world import COUNTRIES



def get_country_code(country_name):
	""" Return the Pygal 2-digit country code for the given country."""
	for code, name in COUNTRIES.items():
		if name == country_name:
			return code 
		if country_name == 'Arab World':
			return 'ae'
		elif country_name == 'Congo, Dem. Rep.':
			return 'cd'
		elif country_name == 'Congo, Rep.':
			return 'cg'
		elif country_name == 'Dominica':
			return 'do'
		elif country_name == 'Egypt, Arab Rep.':
			return 'eg'
		elif country_name == 'Hong Kong SAR, China':
			return 'hk'
		elif country_name == 'Iran, Islamic Rep.':
			return 'ir'
		elif country_name == 'Korea, Dem. Rep.':
			return 'kp'
		elif country_name == 'Korea, Rep.':
			return 'kr'
		elif country_name == 'Macao SAR, China':
			return 'mo'
		elif country_name == 'Macedonia, FYR':
			return 'mk'
		elif country_name == 'Yemen, Rep.':
			return 'ye'

	# if the country is not in the COUNTRIES dict:
	return None









