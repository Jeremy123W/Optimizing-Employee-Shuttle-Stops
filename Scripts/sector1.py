#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 20:31:46 2017

@author: jeremy
"""
import math
import pandas as pd
import gmplot
import itertools
import datetime

emp_addresses = pd.read_csv('employees_with_geocode.csv')
bus_stops = pd.read_csv('bus_stops_with_geocode.csv')

#37.727<longitude   <37.782   
#-122.431<lattitude<-122.406

class Point(object):
    '''
    A point in n dimensional space
    '''
    def __init__(self, coords):
        '''
        coords - A list of values, one per dimension
        '''

        self.coords = coords
        self.n = len(coords)

    def __repr__(self):
        return str(self.coords)


def getDistance(a, b):
    '''
    Euclidean distance between two n-dimensional points.
    https://en.wikipedia.org/wiki/Euclidean_distance#n_dimensions
    Note: This can be very slow and does not scale well
    '''
    if a.n != b.n:
        raise Exception("ERROR: non comparable points")

    accumulatedDifference = 0.0
    for i in range(a.n):
        squareDifference = pow((a.coords[i]-b.coords[i]), 2)
        accumulatedDifference += squareDifference
    distance = math.sqrt(accumulatedDifference)

    return distance




gmap = gmplot.GoogleMapPlotter(37.75, -122.427325, 13)

location = []
for index,row in emp_addresses.iterrows():
        if float(row['longitudes'])< -122.406 and float(row['longitudes'])>-122.438 and float(row['lattitudes'])<37.782 and float(row['lattitudes'])>37.76:
            tmp=[]
            tmp.append(row['lattitudes'])
            tmp.append(row['longitudes'])
            location.append(tmp)
            gmap.marker(row['lattitudes'],row['longitudes'],title=row['address']+' employee_id '+str(row['employee_id']))
        
bus_stop=[]
for index,row in bus_stops.iterrows():
    if row['longitudes']<-122.406 and row['longitudes']>-122.438 and row['lattitudes']<37.782 and row['lattitudes']>37.76:
            tmp=[]
            tmp.append(row['lattitudes'])
            tmp.append(row['longitudes'])
            bus_stop.append(tmp)
            #gmap.marker(row['lattitudes'],row['longitudes'],c='blue',title=str(row['lattitudes'])+' '+str(row['longitudes']))

      
location_objects = [] 
for each in location:
    location_objects.append(Point(each))
    
bus_stop_objects = [] 
for each in bus_stop:
    bus_stop_objects.append(Point(each))    

        
start_time = datetime.datetime.now()
print("Start time: ",start_time) 


total_distances=[]
bus_combinations=[]
for combination in itertools.combinations(bus_stop,4):
    distance=0
    for l_obj in location_objects:
        tmp=[]
        for each in combination:
            bus_object = Point(each)
            tmp.append(getDistance(l_obj,bus_object))
        distance += min(tmp)
    total_distances.append(distance)
    bus_combinations.append(combination)
    


index_min = min(range(len(total_distances)), key=total_distances.__getitem__)      
print('overall distance: ',total_distances[index_min])  
print("bus stop locations: ",bus_combinations[index_min])
print("TIME UNITL END: ",datetime.datetime.now()-start_time) 

for each in bus_combinations[index_min]:
    gmap.marker(each[0],each[1],c='green',title="centroid")     
  
 
gmap.draw("section1_4_stops.html")