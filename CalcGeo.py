import math

def calc_slope(l_seattube, ang_seattube, l_reach, l_stack):
    
    l_seattube_height = math.sin(deg_to_rad(ang_seattube)) * l_seattube
    print('l_seattube_height: ' + str(l_seattube_height))
    l_seattube_setback = math.cos(deg_to_rad(ang_seattube)) * l_seattube
    print('l_seattube_setback: ' + str(l_seattube_setback))
    l_toptube_effective = l_reach + l_seattube_setback
    print('l_toptube_effective: ' + str(l_toptube_effective))
    l_toptube_rise = l_stack - l_seattube_height
    print('l_toptube_rise: ' + str(l_toptube_rise))
    ang_slope = math.atan(l_toptube_rise / l_toptube_effective)
    print('ang_slope: ' + str(rad_to_deg(ang_slope)))
    return l_seattube_setback, l_seattube_height, l_reach, l_stack

def deg_to_rad(deg_in):
    return deg_in * math.pi / 180

def rad_to_deg(rad_in):
    return rad_in * 180 / math.pi
