# Test Suite


# Test the output for problem 1 and problem 2


import unittest
from mock import patch
from lengaburuTraffic import runLengaburuSolution
from lengaburuTraffic.routeSelection import RouteSelection
from lengaburuTraffic.orbits import OrbitGraph,Orbit
from lengaburuTraffic.vehicles import Vehicle,SuperCar,TukTuk,Bike
import mock


print("Starting Testing for Lengaburu problem..")


class TestFinalSolutions(unittest.TestCase):

    @patch('lengaburuTraffic.dataSetup.get_user_input',autospec=True,side_effect=[1,12,10,"sunny"])
    def test_problem1_sample1(self,input):
        self.assertEqual(runLengaburuSolution.run_lengaburu(), 'Vehicle Tuk Tuk on Orbit1')

    @patch('lengaburuTraffic.dataSetup.get_user_input',autospec=True,side_effect=[1,14,20,"windy"])        
    def test_problem1_sample2(self,input):
        self.assertEqual(runLengaburuSolution.run_lengaburu(), 'Vehicle Car on Orbit2')

    @patch('lengaburuTraffic.dataSetup.get_user_input',autospec=True,side_effect=[2,20,12,15,12,"sunny"])        
    def test_problem2_sample1(self,input):
        self.assertEqual(runLengaburuSolution.run_lengaburu(), 'Vehicle Tuk Tuk to Hallitharam via Orbit1 and RK Puram via Orbit4')

    @patch('lengaburuTraffic.dataSetup.get_user_input',autospec=True,side_effect=[2,5,10,20,20,"windy"])        
    def test_problem2_sample2(self,input):
        self.assertEqual(runLengaburuSolution.run_lengaburu(), 'Vehicle Car to RK Puram via Orbit3 and Hallitharam via Orbit4')        


# Test OrbitMap
# def mock_orbits()
class TestOrbitGraph(unittest.TestCase):
    def setup_problem1(self):
        mock_orbit1 = mock.create_autospec(Orbit)
        mock_orbit1.orbit_end_points = ["Silk Dorb","Hallitharam",]
        mock_orbit1.name = "Orbit1"
        mock_orbit2 = mock.create_autospec(Orbit)
        mock_orbit2.orbit_end_points = ["Silk Dorb","Hallitharam",]
        mock_orbit2.name = "Orbit2"
        test_orbit_graph = OrbitGraph([mock_orbit1,mock_orbit2])
        test_orbit_graph.create_maps()
        return test_orbit_graph

    def test_orbit_map_problem1_destination_points(self):
        test_orbit_graph = self.setup_problem1()        
        self.assertEqual(sorted(test_orbit_graph.get_map_destinations()),['Hallitharam','Silk Dorb'])

    def test_orbit_map_problem1_adjacent_points_silk_dorb(self):
        test_orbit_graph = self.setup_problem1()
        self.assertEqual(test_orbit_graph.get_connected_points('Silk Dorb'),['Hallitharam'])

    def test_orbit_map_problem1_adjacent_points_silk_dorb(self):
        test_orbit_graph = self.setup_problem1()
        self.assertEqual(test_orbit_graph.get_connected_points('Silk Dorb'),['Hallitharam'])

    def test_orbit_map_problem1_adjacent_points_hallitharam(self):
        test_orbit_graph = self.setup_problem1()
        self.assertEqual(test_orbit_graph.get_connected_points('Hallitharam'),['Silk Dorb'])

    def test_orbit_map_problem1_connected_orbits_silk_dorb(self):
        test_orbit_graph = self.setup_problem1()
        self.assertEqual(test_orbit_graph.get_connecting_orbits('Silk Dorb')[0],['Orbit1','Orbit2'])

    def test_orbit_map_problem1_connected_orbits_hallitharam(self):
        test_orbit_graph = self.setup_problem1()
        self.assertEqual(test_orbit_graph.get_connecting_orbits('Hallitharam')[0],['Orbit1','Orbit2'])

    def test_orbit_map_problem1_routes_startfrom_silk_dorb_visit_hallitharam(self):
        test_orbit_graph = self.setup_problem1()
        self.assertEqual(test_orbit_graph.route_mapper('Silk Dorb',['Hallitharam']),{1:[['Orbit1'],['Hallitharam']],2:[['Orbit2'],['Hallitharam']]})

    def test_orbit_map_problem1_routes_startfrom_hallitharam_visit_silk_dorb(self):
        test_orbit_graph = self.setup_problem1()
        self.assertEqual(test_orbit_graph.route_mapper('Hallitharam',['Silk Dorb']),{1:[['Orbit1'],['Silk Dorb']],2:[['Orbit2'],['Silk Dorb']]})


    def setup_problem2(self):
        mock_orbit1 = mock.create_autospec(Orbit)
        mock_orbit1.orbit_end_points = ["Silk Dorb","Hallitharam",]
        mock_orbit1.name = "Orbit1"
        mock_orbit2 = mock.create_autospec(Orbit)
        mock_orbit2.orbit_end_points = ["Silk Dorb","Hallitharam",]
        mock_orbit2.name = "Orbit2"
        mock_orbit3 = mock.create_autospec(Orbit)
        mock_orbit3.orbit_end_points = ["Silk Dorb","RK Puram",]
        mock_orbit3.name = "Orbit3"
        mock_orbit4 = mock.create_autospec(Orbit)
        mock_orbit4.orbit_end_points = ["RK Puram","Hallitharam"]
        mock_orbit4.name = "Orbit4"
        test_orbit_graph = OrbitGraph([mock_orbit1,mock_orbit2,mock_orbit3,mock_orbit4])
        test_orbit_graph.create_maps()        
        return test_orbit_graph

    def test_create_map_problem2_destination_points(self):
        test_orbit_graph = self.setup_problem2()
        self.assertEqual(sorted(test_orbit_graph.get_map_destinations()),['Hallitharam','RK Puram','Silk Dorb'])

    def test_orbit_map_problem2_adjacent_points_silk_dorb(self):
        test_orbit_graph = self.setup_problem2()
        self.assertEqual(sorted(test_orbit_graph.get_connected_points('Silk Dorb')),['Hallitharam','RK Puram'])

    def test_orbit_map_problem2_connected_orbits_hallitharam(self):
        test_orbit_graph = self.setup_problem2()
        self.assertEqual(sorted(test_orbit_graph.get_connecting_orbits('Hallitharam')[0]),['Orbit1','Orbit2','Orbit4'])

    def test_orbit_map_problem2_routes_startfrom_silk_dorb_visit_hallitharam(self):
        test_orbit_graph = self.setup_problem2()
        self.assertEqual(test_orbit_graph.route_mapper('Silk Dorb',['Hallitharam']),{1:[['Orbit3','Orbit4'],['RK Puram','Hallitharam']],2:[['Orbit1'],['Hallitharam']],3:[['Orbit2'],['Hallitharam']]})

    def test_orbit_map_problem2_routes_startfrom_hallitharam_visit_silk_dorb(self):
        test_orbit_graph = self.setup_problem2()
        self.assertEqual(test_orbit_graph.route_mapper('Hallitharam',['Silk Dorb']),{1:[['Orbit4','Orbit3'],
            ['RK Puram','Silk Dorb']],2:[['Orbit1'],['Silk Dorb']],3:[['Orbit2'],['Silk Dorb']]})

    def test_orbit_map_problem2_routes_startfrom_hallitharam_visit_rkpuram(self):
        test_orbit_graph = self.setup_problem2()
        self.assertEqual(test_orbit_graph.route_mapper('Hallitharam',['RK Puram']),{1:[['Orbit4'],['RK Puram']],
            2:[['Orbit1','Orbit3'],['Silk Dorb','RK Puram']],3:[['Orbit2','Orbit3'],['Silk Dorb','RK Puram']]})

    def test_orbit_map_problem2_routes_startfrom_silk_dorb_visit_rkpuram(self):
        test_orbit_graph = self.setup_problem2()
        self.assertEqual(test_orbit_graph.route_mapper('Silk Dorb',['RK Puram']),{1:[['Orbit3'],['RK Puram']],
            2:[['Orbit1','Orbit4'],['Hallitharam','RK Puram']],3:[['Orbit2','Orbit4'],['Hallitharam','RK Puram']]})

    def test_orbit_map_problem2_routes_startfrom_silk_dorb_visit_rkpuram(self):
        test_orbit_graph = self.setup_problem2()
        self.assertEqual(test_orbit_graph.route_mapper('Silk Dorb',['RK Puram']),{1:[['Orbit3'],['RK Puram']],
            2:[['Orbit1','Orbit4'],['Hallitharam','RK Puram']],3:[['Orbit2','Orbit4'],['Hallitharam','RK Puram']]})

    def test_orbit_map_problem2_routes_startfrom_silk_dorb_visit_hallitharam_rkpuram(self):
        test_orbit_graph = self.setup_problem2()
        self.assertEqual(test_orbit_graph.route_mapper('Silk Dorb',['Hallitharam','RK Puram']),{1:[['Orbit3',
            'Orbit4'],['RK Puram','Hallitharam']],2:[['Orbit1','Orbit4'],['Hallitharam','RK Puram']],
            3:[['Orbit2','Orbit4'],['Hallitharam','RK Puram']]})

### Testing a new case by increasing the number of orbits. Orbit5 and Orbit6 introduced to visit 
### ALAGNAMROK. Orbit5 joins Silk Dorb and Orbit6 joins ALAGNAMROK and HALLITHARAM

    def setup_orbit_extention(self):
        mock_orbit1 = mock.create_autospec(Orbit)
        mock_orbit1.orbit_end_points = ["Silk Dorb","Hallitharam",]
        mock_orbit1.name = "Orbit1"
        mock_orbit2 = mock.create_autospec(Orbit)
        mock_orbit2.orbit_end_points = ["Silk Dorb","Hallitharam",]
        mock_orbit2.name = "Orbit2"
        mock_orbit3 = mock.create_autospec(Orbit)
        mock_orbit3.orbit_end_points = ["Silk Dorb","RK Puram",]
        mock_orbit3.name = "Orbit3"
        mock_orbit4 = mock.create_autospec(Orbit)
        mock_orbit4.orbit_end_points = ["RK Puram","Hallitharam"]
        mock_orbit4.name = "Orbit4"
        mock_orbit5 = mock.create_autospec(Orbit)
        mock_orbit5.orbit_end_points = ["Silk Dorb","Alagnamrok"]
        mock_orbit5.name = "Orbit5"
        mock_orbit6 = mock.create_autospec(Orbit)
        mock_orbit6.orbit_end_points = ["Alagnamrok","Hallitharam"]
        mock_orbit6.name = "Orbit6"
        test_orbit_graph = OrbitGraph([mock_orbit1,mock_orbit2,mock_orbit3,mock_orbit4,mock_orbit5,mock_orbit6])
        test_orbit_graph.create_maps()        
        return test_orbit_graph


    def test_orbit_map_extension_routes_startfrom_silk_dorb_visit_alagnamrok_hallitharam(self):
        test_orbit_graph = self.setup_orbit_extention()
        self.assertEqual(test_orbit_graph.route_mapper('Silk Dorb',['Alagnamrok','Hallitharam']),
            {1:[['Orbit3','Orbit4','Orbit6'],
            ['RK Puram','Hallitharam','Alagnamrok']],2:[['Orbit5','Orbit6'],['Alagnamrok','Hallitharam']],3:[['Orbit1','Orbit6'],['Hallitharam',
            'Alagnamrok']],4:[['Orbit2','Orbit6'],['Hallitharam','Alagnamrok']],})


class TestOrbit(unittest.TestCase):
    # Mock Vehicles & check travel times
    # check travel times for different weather conditions
    def test_orbit1_bike_travel_time_traffic_limit_sunny_weather(self):
        mock_vehicle = mock.create_autospec(Bike)
        mock_vehicle.speed =  5
        mock_vehicle.time_cross_crater_mins =  2   
        mock_vehicle.name = "Bike"
        weather = "sunny"        
        Orbit1 = Orbit("Orbit1",20,10,["Silk Dorb","Hallitharam"],{"sunny":10,"windy":12,"rainy":20})
        Orbit1.model_orbit_environment(weather,{"Orbit1_traffic_limit":10,"Orbit2_traffic_limit":20})
        self.assertEqual(Orbit1.get_travel_time(mock_vehicle)[0],262)

    def test_orbit2_car_travel_time_traffic_limit_rainy_weather(self):
        mock_vehicle = mock.create_autospec(SuperCar)
        mock_vehicle.speed =  20
        mock_vehicle.time_cross_crater_mins =  5
        mock_vehicle.name = "SuperCar"
        weather = "rainy"        
        Orbit2 = Orbit("Orbit2",20,10,["Silk Dorb","Hallitharam"],{"sunny":10,"windy":12,"rainy":20})
        Orbit2.model_orbit_environment(weather,{"Orbit1_traffic_limit":10,"Orbit2_traffic_limit":10})
        self.assertEqual(Orbit2.get_travel_time(mock_vehicle)[0],180)


    def test_orbit2_tuktuk_travel_time_traffic_limit_rainy_weather(self):
        mock_vehicle = mock.create_autospec(TukTuk)
        mock_vehicle.speed =  10
        mock_vehicle.time_cross_crater_mins =  3
        mock_vehicle.name = "SuperCar"
        weather = "windy"        
        Orbit2 = Orbit("Orbit2",20,10,["Silk Dorb","Hallitharam"],{"sunny":10,"windy":12,"rainy":20})
        Orbit2.model_orbit_environment(weather,{"Orbit1_traffic_limit":10,"Orbit2_traffic_limit":10})
        self.assertEqual(Orbit2.get_travel_time(mock_vehicle)[0],153)
                


class TestVehicles(unittest.TestCase):
    # Check vehicles allowed for diff weather conditions
    def test_car_allowed_sunny(self):
        vehicles_allowed_in_weather = {"sunny":["SuperCar","Bike"],"rainy":["Bike","TukTuk"]}
        supercar = SuperCar("SuperCar",20,3,vehicles_allowed_in_weather)
        supercar.model_vehicle_environment("sunny")
        self.assertEqual(supercar.travel_allowed,1)

    def test_tuktuk_allowed_sunny(self):
        vehicles_allowed_in_weather = {"sunny":["SuperCar","Bike"],"rainy":["Bike","TukTuk"]}
        tuktuk = TukTuk("TukTuk",20,3,vehicles_allowed_in_weather)
        tuktuk.model_vehicle_environment("sunny")
        self.assertEqual(tuktuk.travel_allowed,0)

if __name__ == '__main__':
	unittest.main()






