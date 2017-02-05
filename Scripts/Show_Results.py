#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 20:31:46 2017

@author: jeremy
"""

import pandas as pd

import gmplot


emp_addresses = pd.read_csv('employees_with_geocode.csv')
bus_stops = pd.read_csv('Results.csv')


gmap = gmplot.GoogleMapPlotter(37.75, -122.427325, 13)

for index,row in emp_addresses.iterrows():
        gmap.marker(row['lattitudes'],row['longitudes'],title=row['address']+' employee_id '+str(row['employee_id']))

for index,row in bus_stops.iterrows():
        gmap.marker(row['lattitudes'],row['longitudes'],c='green',title=str(row['lattitudes'])+' '+str(row['longitudes']))

      

#for each in centroids:
#    gmap.marker(each[0],each[1],c='green',title="centroid") 




    
  
# color='#FF0000', c=None, title="no implementation"   
gmap.draw("Results.html") 