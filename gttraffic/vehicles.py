
# Classes for Vehicles and their sub classes

class Vehicle:
	def __init__(self,name,speed,time_cross_crater_mins,vehicles_allowed_in_weather):
		self.name = name
		self.speed = speed
		self.time_cross_crater_mins = time_cross_crater_mins
		self.travel_allowed = None
		self.vehicles_allowed_in_weather = vehicles_allowed_in_weather
	def model_vehicle_environment(self,weather):
		if self.name in self.vehicles_allowed_in_weather[weather]:
			self.travel_allowed = 1
		else:
			self.travel_allowed = 0


class SuperCar(Vehicle):
	def __init__(self,name,speed,time_cross_crater_mins,vehicles_allowed_in_weather):
		Vehicle.__init__(self,name,speed,time_cross_crater_mins,vehicles_allowed_in_weather)



class TukTuk(Vehicle):
	def __init__(self,name,speed,time_cross_crater_mins,vehicles_allowed_in_weather):
		Vehicle.__init__(self,name,speed,time_cross_crater_mins,vehicles_allowed_in_weather)


class Bike(Vehicle):
	def __init__(self,name,speed,time_cross_crater_mins,vehicles_allowed_in_weather):
		Vehicle.__init__(self,name,speed,time_cross_crater_mins,vehicles_allowed_in_weather)
