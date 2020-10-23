# Setup of Orbits, Vehicles and other preferences
-------------------------------------------------
## Weather Data File (present as data/weather.txt)
------------------
Supply data in this manner - Weather Name,Crater Impact
For Crater Impact, give a negative if it causes a decrease in craters and positive if it causes an increase

Sample Record:
"sunny",-10

## Orbits Data File (present as data/orbits1.txt and data/orbits.txt)
-----------------
Supply orbits in this manner - Orbit Name,distance,craters,start point,end point
All orbit names should be unique, start point and end point should be a part of destinations.txt file
Each orbit record should appear in a newline
Sample Record:
"Orbit1",18,20,"Silk Dorb","Hallitharam"

## Vehicles Data File (present as data/vehicles.txt)
-----------------
Supply vehicle data in this manner - Vehicle,speed,time to cross a crater in mins,1 if travels in sunny weather and 0 otherwise,1 if travels in rainy weather and 0 otherwise,1 if travels in windy weather and 0 otherwise,vehicle preferred order.All vehicle names should be unique.Each vehicle record should appear in a 
newline.The order for flags in weather should be the same order as present in the Weather Data file desribed above.

Sample Record:
"Bike",10,2,1,1,0,1	


# Running the script 
---------------------
Requirement : 
Python 3.6

Package Requirements for Running Test cases:
mock
unittest

No dependencies for the running 
To execute the script , run the python script runLengaburu.py. Ensure that all files are present in the same folder.

 * git clone https://github.com/prasad_kevin/gttraffic
 * cd gttraffic

For Problem 1: Example

python ./gttraffic/runLengaburuSolution.py 
 * Select problem. press 1 for Problem 1 and 2 for Problem 2: 1
 * Enter traffic limit for Orbit1 : 12
 * Enter traffic limit for Orbit2 : 10
 * Input weather.Options are sunny/rainy/windy : sunny


For Problem 2: Example

python ./gttraffic/runLengaburuSolution.py 
 * Select problem. press 1 for Problem 1 and 2 for Problem 2: 2
 * Enter traffic limit for Orbit1 : 5
 * Enter traffic limit for Orbit2 : 10
 * Enter traffic limit for Orbit3 : 20
 * Enter traffic limit for Orbit4 : 20
 * Input weather.Options are sunny/rainy/windy : windy


To run the script as a complete pip installable package
-------------------------------------------------------

Navigate to the root
cd gttraffic

Run -
```python
python pip install .
```

# TESTING
---------

Requirement : 
Python 3 or above

Package Requirements for Running Test cases:
 * mock
 * unittest

Run :

* Navigate to root folder 
```python
cd gttraffic 
python ./tests/runLengaburuTestCases.py

```

OR

The tests can be run directly by calling  setup.py from root folder

```python
cd gttraffic 
python setup.py test

```

It runs a sample set of 25 test cases, which test some of the critical functionality within the application.
Its not exhaustive to the extent of testing all possible cases, but gives an undertanding of how the testing
can be enhanced further.

The tests broadly cover the following areas :

 * It tests the overall expected outputs for problem 1 and problem 2 (Incorporated in this, even though its not strictly a unit testing)
 * It tests the overall expected Route values for different start points and destinations. It also
tests the condition of extensibility by adding a new end point "Alagnamrok" between Silk Dorb and Hallitharam.
Alagnamrok is connected to Silk Dorb via Orbit5 and Hallitharam via Orbit6.
 * It tests the expected travel times for a given Orbit and Vehicle combinations under different weather and traffic conditions
 * It tests for vehicle restrictions given certain weather conditions.


