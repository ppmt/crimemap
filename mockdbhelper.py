class MockDBHelper:
    def connect(self, database="crimemap"):
        pass
    def get_all_crimes(self):
	return [{ 'latitude': 52.912289,
		  'longitude': -2.523355,
		  'date': "2000-01-01",
		  'category': "mugging",
		  'description': "mock description" }]
    def add_crime(self, category, date, latitude, longitude,
            description):
        pass
