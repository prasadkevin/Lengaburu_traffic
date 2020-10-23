# Classes for orbits definition and Orbit map

""" Orbit class to store orbit related information. model_orbit_environment models the orbit condition for a
particular weather condition and traffic conditions"""
class Orbit:
	def __init__(self,name,distance,craters,end_points,crater_weather_impact,orbit_traffic_limit=None):
		self.name = name
		self.distance = distance
		self.craters = craters
		self.craters_weather = craters
		self.orbit_traffic_limit = orbit_traffic_limit
		self.orbit_end_points = end_points
		self.crater_weather_impact = crater_weather_impact
	def get_travel_time(self,vehicle,orbit_vehicle_travel_times=None):
		# Uses a dictionary to store travel time for orbit vehicle combinations. Retrieves it from the 
		# dictionary if available, if not calculates it and stores.
		stored = 0
		if orbit_vehicle_travel_times != None:
			stored = orbit_vehicle_travel_times.get(self.name + "__" + vehicle.name,0)
			time_total = stored
		if orbit_vehicle_travel_times==None or stored == 0:
			if self.orbit_traffic_limit != None:
				speed = min(vehicle.speed,self.orbit_traffic_limit)
			else:
				speed = vehicle.speed
			time_travel = self.distance * 1.0/ speed * 60
			time_craters = self.craters_weather * vehicle.time_cross_crater_mins
			time_total = time_travel + time_craters
		if orbit_vehicle_travel_times != None:
			orbit_vehicle_travel_times[self.name + "__" + vehicle.name]=time_total
		return time_total,orbit_vehicle_travel_times
	def model_orbit_environment(self,weather,orbit_traffic_limit):
		# models the environmental impact on the orbit
		self.orbit_traffic_limit = orbit_traffic_limit[self.name + "_traffic_limit"]
		crater_increase_pct = self.crater_weather_impact[weather]
		self.craters_weather = self.craters * crater_increase_pct/100 + self.craters



""" Class for storing the representation of how the orbits are connected.
It has methods to output all connected points and all connected orbits given a point"""
class OrbitGraph:
	def __init__(self,all_orbits=[]):
		self.all_orbits = all_orbits
		self.orbit_map = {}
	def create_maps(self):
		for orbit in self.all_orbits:
			for each in orbit.orbit_end_points:
				oth_point = list(set(orbit.orbit_end_points) - set([each]))[0]
				if self.orbit_map.get(each,None) == None:
					self.orbit_map[each] = {oth_point:[orbit.name]}					
				else:
					if self.orbit_map[each].get(oth_point,None) == None:
						self.orbit_map[each].update({oth_point:[orbit.name]})
					else:
						self.orbit_map[each][oth_point] = self.orbit_map[each][oth_point] + [orbit.name]
	def get_connecting_orbits(self,point_start):
		req_points = list(self.orbit_map[point_start].keys())
		connecting_orbits = []
		connected_end_points = []
		for each in req_points:
			req_orbits = self.orbit_map[point_start][each]
			connecting_orbits = connecting_orbits + req_orbits
			end_points = len(req_orbits) * [each]
			connected_end_points = connected_end_points + end_points
		return connecting_orbits,connected_end_points
	def get_connected_points(self,point):
		result = []
		if self.orbit_map.get(point,None) != None:
			result = list(self.orbit_map[point].keys())
		return result
	def get_map_destinations(self):
		result = list(self.orbit_map.keys())
		return result		
	def get_orbits_points_to_visit(self,point1,points_to_visit,all_paths,incoming_orbit,all_orbits,point_visited,final_path,final_orbits):
		""" A recursive method to give all routes which start from point1 and cover the points in the points to visit
		points_visited is a dictionary which keeps track of which points have already been visited while attempting to find a route
		which covers all points visited. Once such a route is found, it flushes out the paths and orbits and appends it to the 
		list of final paths and final orbits. Start from point 1 and do a depth wise traversal
		 mark the start point as visited """
		point_visited[point1]=1	
		# if its not the first run, keep appending paths and orbits. Update remaining points left to visit
		if incoming_orbit != "":
			all_orbits.append(incoming_orbit)
			all_paths.append(point1)
			points_to_visit = list(set(points_to_visit) - set([point1]))
		# if no points remain to be visited, flush out the temporary lists and append it to final paths and orbits
		if len(points_to_visit)==0:
			final_path.append(all_paths)
			final_orbits.append(all_orbits)
			all_paths = []
			all_orbits = []
		else:
			# Get all connecting orbits from point 1
			connecting_orbits,connected_end_points = self.get_connecting_orbits(point1)
			for i,conn_orbit in enumerate(connecting_orbits):						
				end_point = connected_end_points[i]	
				# If the point has not been visited in the current run, then check from the new point again
				if point_visited.get(end_point,0) == 0:													
					final_path,point_visited,final_orbits,all_paths,all_orbits = self.get_orbits_points_to_visit(end_point,points_to_visit,all_paths,conn_orbit,all_orbits,point_visited,final_path,final_orbits)
		""" Flush out the last point that was visited and mark it as 'not visited'. This is required for marking
		the destination point again as not visited."""
		if len(all_paths)>0:
			all_paths.pop()
			all_orbits.pop()
		point_visited[point1]=0
		return final_path,point_visited,final_orbits,all_paths,all_orbits
	def route_mapper(self,point1,points_to_visit):
		# Calls the get_orbits_points_to_visit function and wraps it up in a proper manner
		all_paths,all_orbits,final_path,final_orbits= [],[],[],[]
		point_visited = {}
		incoming_orbit = ""
		final_path,point_visited,final_orbits,all_paths,all_orbits = self.get_orbits_points_to_visit(point1,points_to_visit,all_paths,incoming_orbit,all_orbits,point_visited,final_path,final_orbits)
		routes = {}
		for i,orbit in enumerate(final_orbits):
			routes[len(routes)+1] = [orbit,final_path[i]]
		return routes

