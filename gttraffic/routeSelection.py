# Route Selection and Optimization


"""Class for route selection optimization logic. Once all the availble routes are mapped,
then it selects the best route & vehicle combination based on time taken. A route is considered
a combination of multiple orbits."""
class RouteSelection:
	def set_preferences(self,vehicle_preferred_order):
		# Assuming that vehicle preferred order could be setup / changed any time later after the object is created
		self.vehicle_preferred_order = vehicle_preferred_order
	def get_route_vehicle_combinations(self,routes,vehicles_allowed):
		""" Method to get all routes and vehicle combinations given the restriction of using the same vehicle
		for a route consisting of multiple orbits.If later the requirement changes to allow multiple vehicles,
		only this method needs to be changed."""
		all_route_vehicle_combs = {}
		for route in routes.items():
			orbit_vehicles_combs = [[each.name] * len(route[1][0]) for each in vehicles_allowed]
			route_vehicles = [list(zip(route[1][0],orbit_vehicles_combs_ins)) for orbit_vehicles_combs_ins in orbit_vehicles_combs]
			for each_route_vehicle in route_vehicles:
				all_route_vehicle_combs[len(all_route_vehicle_combs)+1]=[each_route_vehicle,route[1][1]*len(each_route_vehicle)]
		return all_route_vehicle_combs
	def get_best_comb(self,combination_times,combinations):
		# gets best route given routes and their travel times
		min_time = min(combination_times)
		indx = [i for i,each in enumerate(combination_times) if each == min_time]
		combinations_best = [combinations[idx] for idx in indx]
		return combinations_best
	def tie_breaker(self,combinations_best):
		# implements the tie breaker logic if multiple best combinations exist
		first_temp_combination = combinations_best
		vehicles_order = [self.vehicle_preferred_order[each[0][0][1]] for each in first_temp_combination]
		vehicle_sel = vehicles_order.index(min(vehicles_order))
		return combinations_best[vehicle_sel]
	def evaluate_best_route(self,cityTraffic,point_start,points_to_visit):	
		# Evaluate best route by taking the vehicles allowed based on weather condition. Gets all routes from
		# Orbit map class. Then creates possible vehicle combinations.
		# For each orbit and vehicle in a given route, gets travel time and finds best combination. Tie breaker
		# logic incorporated
		vehicles_allowed = [vehicle for vehicle in cityTraffic.all_vehicles if vehicle.travel_allowed ==1]	
		combinations=[]
		combination_times = []
		routes = cityTraffic.orbit_map.route_mapper(point_start,points_to_visit)
		route_vehicle_combinations = self.get_route_vehicle_combinations(routes,vehicles_allowed)
		orbit_dict = {orbit.name:orbit for orbit in cityTraffic.all_orbits}
		orbit_vehicle_travel_times = {}
		for idx in route_vehicle_combinations:
			route_vehicle = route_vehicle_combinations[idx][0]
			end_points = route_vehicle_combinations[idx][1]
			route_time = 0
			for orbit,vehicle in route_vehicle:
				orbit_time,orbit_vehicle_travel_times = orbit_dict[orbit].get_travel_time(cityTraffic.vehicle_dict[vehicle],orbit_vehicle_travel_times)
				route_time = route_time + orbit_time
			combinations.append([route_vehicle,end_points])			
			combination_times.append(route_time)
		combinations_best = self.get_best_comb(combination_times,combinations)
		if len(combinations_best) > 1:
			combinations_best = self.tie_breaker(combinations_best)	
		vehicle = combinations_best[0][0][0][1]
		orbit_destination = [(combinations_best[0][0][i][0],combinations_best[0][1][i]) for i,_ in enumerate(combinations_best[0][0])]
		return vehicle,orbit_destination


