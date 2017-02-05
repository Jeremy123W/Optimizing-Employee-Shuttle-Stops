#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 20:31:46 2017

@author: jeremy
"""

import pandas as pd
import gmplot


emp_addresses = pd.read_csv('employees_with_geocode.csv')
bus_stops = pd.read_csv('bus_stops_with_geocode.csv')



gmap = gmplot.GoogleMapPlotter(37.75, -122.427325, 13)

for index,row in emp_addresses.iterrows():
        gmap.marker(row['lattitudes'],row['longitudes'],title=row['address']+' employee_id '+str(row['employee_id']))

for index,row in bus_stops.iterrows():
        gmap.marker(row['lattitudes'],row['longitudes'],c='blue',title=str(row['lattitudes'])+' '+str(row['longitudes']))

      


gmap.draw("Overview.html") 