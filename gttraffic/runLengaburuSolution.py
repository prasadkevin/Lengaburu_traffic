# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 18:21:03 2020

@author: prasad
"""
# File to run for Lengaburu problem

from dataSetup import InputDataStructures,problem_setup
from orbits import Orbit,OrbitGraph
from vehicles import Vehicle,SuperCar,TukTuk,Bike
from traffic import CityTraffic
from routeSelection import RouteSelection


# Final method to display output in proper format
def display_output(vehicle,orbit_destination,problem):
	if problem == 1:
		output =  'VEHICLE_NAME ORBIT_NO : ' + vehicle + "  " + orbit_destination[0][0]
# 	else:
# 		output = "Vehicle "+ vehicle + " to "
# 		for each in enumerate(orbit_destination):
# 			output = output + each[1][1]  +  " via " + each[1][0] + " and " 
# 		output = output[:-5]		
	return output



def run_lengaburu():
	# Structure setup and input data
	orbit_data,vehicle_data,weather_list,vehicles_allowed_in_weather,vehicle_preferred_order,orbit_traffic_limit,weather,crater_weather_impact,point_start,points_to_visit,problem = problem_setup()

	# create city traffic object and model the environment of weather and traffic limits
	blr = CityTraffic()
	blr.initialize(orbit_data,vehicle_data,vehicles_allowed_in_weather,crater_weather_impact)
	blr.model_environment(weather,orbit_traffic_limit)

	# create route selection object and setup preferences
	routeSelector = RouteSelection()
	routeSelector.set_preferences(vehicle_preferred_order)

	# evaluate best route and display
	vehicle,orbit_destination = routeSelector.evaluate_best_route(blr,point_start,points_to_visit)

	# Get display format
	output = display_output(vehicle,orbit_destination,problem)
	return output

if __name__ == '__main__':
	output = run_lengaburu()
	print(output)

