# Traffic related classes

from orbits import Orbit,OrbitGraph
from vehicles import Vehicle,SuperCar,TukTuk,Bike


class CityTraffic:
	def __init__(self):
		self.all_orbits = []
		self.orbit_dict = {}
		self.all_vehicles = []
		self.vehicle_dict = {}
		self.orbit_map = None
	def initialize_orbits(self,orbit_data,crater_weather_impact):	
		for orbit in orbit_data:
			distance = orbit_data[orbit]['distance']
			craters = orbit_data[orbit]['craters']
			end_points = orbit_data[orbit]['end_points']
			orbit = Orbit(orbit,distance,craters,end_points,crater_weather_impact)			
			self.all_orbits.append(orbit)
		self.orbit_dict = {orbit.name:orbit for orbit in self.all_orbits}			
	def initialize_orbit_map(self):	
		self.orbit_map = OrbitGraph(self.all_orbits)
		self.orbit_map.create_maps()
	def initialize_vehicles(self,vehicle_data,vehicles_allowed_in_weather):
		for vehicle in vehicle_data:			
			speed = vehicle_data[vehicle]['speed']
			time_cross_crater_mins = vehicle_data[vehicle]['time_cross_crater_mins']
			# CHECK IF THIS NEEDS CHANGE. VERY TIED IN TO DATA
			if vehicle == "Car":
				vehicle = SuperCar(vehicle,speed,time_cross_crater_mins,vehicles_allowed_in_weather)				
			elif vehicle == "Tuk Tuk":
				vehicle = TukTuk(vehicle,speed,time_cross_crater_mins,vehicles_allowed_in_weather)				
			elif vehicle == "Bike":
				vehicle = Bike(vehicle,speed,time_cross_crater_mins,vehicles_allowed_in_weather)				
			else:
				print("Throw Exception")
			self.all_vehicles.append(vehicle)
		self.vehicle_dict = {vehicle.name:vehicle for vehicle in self.all_vehicles}
	def initialize(self,orbit_data,vehicle_data,vehicles_allowed_in_weather,crater_weather_impact):
		self.initialize_orbits(orbit_data,crater_weather_impact)
		self.initialize_orbit_map()
		self.initialize_vehicles(vehicle_data,vehicles_allowed_in_weather)
		# return self.all_orbits,self.orbit_dict,self.orbit_map,self.all_vehicles,self.vehicle_dict
	def model_environment(self,weather,orbit_traffic_limit):
		for orbit in self.all_orbits:
			orbit.model_orbit_environment(weather,orbit_traffic_limit)
		for vehicle in self.all_vehicles:
			vehicle.model_vehicle_environment(weather)

