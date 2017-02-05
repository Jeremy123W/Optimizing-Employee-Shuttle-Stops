#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 20:22:48 2017

@author: jeremy
"""
import itertools
import matplotlib.pyplot as plt

#input number of stops and total distance per section
Section_1=[(2,4.443288894436137),
           (3,4.32550657196003),
           (4,4.24510185476948)]
Section_2=[(2,3.4775575720267273),
           (3,2.9888868253362606),
           (4,2.8638046862278705)]
Section_3=[(2,2.123775614486866),
           (3,1.868219917112954),
           (4,1.8092163367658658)]
Section_4=[(1,0.19379909084842276),
           (2,0.19036118812729588),]

#get all combinations with 10 total stops
combination_10_stops=[]
for combination in itertools.product(Section_1,Section_2,Section_3,Section_4):
    total_stops=0
    for num_stops,distance in combination:
        total_stops+=num_stops
    if total_stops==10:
        combination_10_stops.append(combination)

#create tuple 
tuple_comb=[]
for sec1,sec2,sec3,sec4 in combination_10_stops:
    x=(str(sec1[0]) + ', ' + str(sec2[0])+', '+ str(sec3[0])+', ' + str(sec4[0]))
    y=sec1[1]+sec2[1]+sec3[1]+sec4[1]
    tuple_temp = (x,y)
    tuple_comb.append(tuple_temp)
    
#sort tuple based on total distance
tuple_comb=sorted(tuple_comb,key=lambda x: x[1])

#create x and y for plot
y=[]
x=[]
for sections,total_distance in tuple_comb:
    y.append(total_distance)
    x.append(sections)
    
#create plot
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xticks(range(len(y)), minor=False)
ax.set_xticklabels(x, rotation=45)
ax.axis([0,13,8.8,10.2])
ax.bar(range(len(y)), y, width=.3, color="blue")
ax.set_ylabel('Total Distance')
ax.set_xlabel('Number of Stops per Section: Section 1, Section 2, Section 3, Section 4')
ax.set_title('Total Distance with Ten Bus Stops')
plt.show()