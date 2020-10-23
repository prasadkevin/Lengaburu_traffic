# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 18:21:03 2020

@author: prasad
"""

# Classes for setting up data Structures and create problem setup
import os

class InputDataStructures():
	def __init__(self,data_dir):
		self.data_dir = data_dir
		self.orbit_data = {}
		self.vehicle_data,self.vehicles_weather,self.vehicles_allowed_in_weather= {},{},{}
		self.vehicle_preferred_order = {}
		self.weather_list = []	
		self.crater_weather_impact = {}	
	def read_text_file(self,filename):
		f = open(self.data_dir+"/"+filename,"rb")
		text_data = []
		for lines in f:
			lines = lines.decode("utf-8").replace("\n","")
			text_data.append(lines)
		return text_data
	def create_orbit_data(self,filename):
		orbit_raw_data = self.read_text_file(filename)
		self.orbit_data = {}
		for each in orbit_raw_data:
			each = each.split(",")
			orbit_name = eval(each[0])
			orbit_distance = eval(each[1])
			orbit_craters = eval(each[2])
			orbit_end_points = [eval(each[3])]
			orbit_end_points = orbit_end_points + [eval(each[4])]
			self.orbit_data[orbit_name] = {"distance":orbit_distance,"craters":orbit_craters,"end_points":orbit_end_points}
	def create_weather_data(self,filename):
		weather_raw_data = self.read_text_file(filename)
		self.weather_list = []		
		self.crater_weather_impact = {}
		for each in weather_raw_data:
			each = each.split(",")
			weather_name = eval(each[0])
			crater_increase_pct = eval(each[1])
			self.weather_list.append(weather_name)			
			self.crater_weather_impact[weather_name] = crater_increase_pct			
	def create_vehicle_data(self,filename):
		vehicle_raw_data = self.read_text_file(filename)		
		for each in vehicle_raw_data:
			each = each.split(",")
			vehicle_name = eval(each[0])
			vehicle_speed = eval(each[1])
			vehicle_time_to_cross_crater = eval(each[2])
			vehicle_sunny = eval(each[3])
			vehicle_rainy = eval(each[4])
			vehicle_windy = eval(each[5])
			vehicle_order = eval(each[6])
			self.vehicle_data[vehicle_name] = {"speed":vehicle_speed,"time_cross_crater_mins":vehicle_time_to_cross_crater}
			# self.vehicles_weather[vehicle_name] = {"sunny":vehicle_sunny,"windy":vehicle_windy,"rainy":vehicle_rainy}
			self.vehicles_weather[vehicle_name] = {weather:eval(each[3+i]) for i,weather in enumerate(self.weather_list)}
			self.vehicle_preferred_order[vehicle_name] = vehicle_order
		for weather in self.weather_list:	
			self.vehicles_allowed_in_weather[weather] = [veh for veh in self.vehicles_weather if self.vehicles_weather[veh][weather]==1]	
	def create_setup(self,orbit_filename,vehicle_filename,weather_filename):
		self.create_orbit_data(orbit_filename)
		self.create_weather_data(weather_filename)
		self.create_vehicle_data(vehicle_filename)							
		return self.orbit_data,self.vehicle_data,self.weather_list,self.vehicles_allowed_in_weather,self.vehicle_preferred_order,self.crater_weather_impact


def get_user_input(text):
	input_ = input(text)
	return input_



def problem_setup():
	problem = 1
	assert(problem == 1 or problem == 2)
	if problem == 1:
		file_list = ["orbits1.txt","vehicles.txt","weather.txt"]
		point_start = "Silk Dorb"
		points_to_visit = ["Hallitharam"]		
	if problem == 2:
		file_list = ["orbits2.txt","vehicles.txt","weather.txt"]	
		point_start = "Silk Dorb"
		points_to_visit = ["RK Puram","Hallitharam"]		
	# setup for orbit and vehicles for selected problem data	
	dirname = os.path.dirname(__file__)
	data_path = os.path.join(dirname, '../data')
	input = InputDataStructures(data_path)
	orbit_data,vehicle_data,weather_list,vehicles_allowed_in_weather,vehicle_preferred_order,crater_weather_impact = input.create_setup(file_list[0],file_list[1],file_list[2])	
	orbit_names = list(orbit_data.keys())
	orbit_names.sort()	
	# ask for traffic limits for orbits present for orbit setup		
# 	data_input = get_user_input('WEATHER ORBIT_1_TRAFFIC_SPEED ORBIT_2_TRAFFIC_SPEED')		
 	# orbit_traffic_limit = {each + "_traffic_limit":int(get_user_input("Enter traffic limit for " + each + " : ")) for each in orbit_names}
	# ask to select one weather	
	weather = ""
	while weather not in weather_list:
# 		weather = get_user_input("Input weather.Options are " +"/".join(weather_list) + " : ")
		data_input = get_user_input('WEATHER ORBIT_1_TRAFFIC_SPEED ORBIT_2_TRAFFIC_SPEED : ')
		orbit_traffic_limit = {'Orbit1_traffic_limit' : int(data_input.split(' ')[1]), 'Orbit2_traffic_limit' : int(data_input.split(' ')[2])}
# 		import pdb
# 		pdb.set_trace()
		weather = data_input.split(' ')[0].lower()
		if weather not in weather_list:
			print("Oops. Weather input does not correspond to options shown")
	return orbit_data,vehicle_data,weather_list,vehicles_allowed_in_weather,vehicle_preferred_order,orbit_traffic_limit,weather,crater_weather_impact,point_start,points_to_visit,problem


