from geopy import distance
import numpy as np

newport_ri = (41.49008, -71.312796)
cleveland_oh = (41.499498, -81.695391)

college_geo = []
chickfila_geo = []
with open('colleges_locations.txt', encoding='latin1') as colleges, open('chickfila_locations.txt', encoding='latin1') as chickfilas:
    college_geo = [c.split(':') for c in colleges.read().splitlines()]
    chickfila_geo = [c.split(':') for c in chickfilas.read().splitlines()]

def dist_between(geo1, geo2):
    return distance.distance(geo1, geo2).miles

def dist_lis(geo1, lis):
    return [[dist_between(geo1, eval(loc)), loc, name] for name, loc in lis]

total_list = [[dist_lis(eval(loc), chickfila_geo), college] for college, loc in college_geo]

with open('total_list.txt', 'w') as o:
    o.write(repr(total_list))