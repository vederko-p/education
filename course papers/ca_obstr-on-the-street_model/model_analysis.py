import numpy as np
import copy

import model_visualization as mymodel_vis
import an_obstruction_on_the_street_model as mymodel


def quantity_of_cars(step_i):  # returns a quantity of cars for one step
    t = 0
    for i in step_i:
        if i[2] != -1:
            t += 1
    return t


def average_v_global(steps):  # returns an average speed of cars at the all road
    s_v = 0
    q_c = 0
    for t in range(1200):
        for j in steps[t]:
            if mymodel.car_q(j[2]):
                s_v += j[2]
                q_c += 1
    return s_v / q_c


def average_v_conv(steps, conv):  # returns an average speed of cars at the convergence zone
    # conv - [[a, b]]
    s_v = 0
    q_c = 0
    for t in range(1200):
        for j in steps[t]:
            if mymodel.car_q(j[2]):
                if mymodel.what_zone(j[1], conv) == 'conv-zone':
                    q_c += 1
                    s_v += j[2]
    return s_v / q_c


def average_v_obstr(steps, obstr):  # returns an average speed of cars at the convergence zone
    # obstr - [[a, b]]
    s_v = 0
    q_c = 0
    for t in range(1200):
        for j in steps[t]:
            if mymodel.car_q(j[2]):
                if mymodel.what_zone(j[1], 0, obstr) == 'obstr-zone':
                    q_c += 1
                    s_v += j[2]
    return s_v / q_c


def density_global(steps):  # returns a traffic flow density at all road
    q_c = 0
    for t in range(1200):
        q_c += quantity_of_cars(steps[t])
    return q_c / 1200


def density_conv(steps, conv):  # returns a traffic flow density at convergence zone
    # conv - [[a, b]]
    q_c = 0
    for t in range(1200):
        for j in steps[t]:
            if mymodel.car_q(j[2]):
                if mymodel.what_zone(j[1], conv) == 'conv-zone':
                    q_c += 1
    return q_c / 1200


def density_obstr(steps, obstr):  # returns a traffic flow density at convergence zone
    # obstr - [[a, b]]
    q_c = 0
    for t in range(1200):
        for j in steps[t]:
            if mymodel.car_q(j[2]):
                if mymodel.what_zone(j[1], 0, obstr) == 'obstr-zone':
                    q_c += 1
    return q_c / 1200
