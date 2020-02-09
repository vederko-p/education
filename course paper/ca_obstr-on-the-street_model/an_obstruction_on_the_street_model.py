import numpy as np
import copy
import random


def fix_position(i, l):
    if i < 0:
        return (-1 * (abs(i) % l) + l) % l
    else:
        return i % l


def car_q(car_speed):  # returns True, if an element i is a car, False - if isn't
    return car_speed >= 0


def neighbor_cell(all_cars, i):  # returns True if neighboring cell is free, False - if isn't
    len_l = len(all_cars)
    if len_l == 1:
        return True
    else:
        if all_cars[i, 0]:
            return all_cars[fix_position(i - 1, len_l), 1] != all_cars[i, 1]
        else:
            return all_cars[fix_position(i + 1, len_l), 1] != all_cars[i, 1]


def neighbors(all_cars, i):  # returns a list of positions of neighbors for car i, type: [lb, rb, lf, rf]
    len_l = len(all_cars)
    left_lane_neighbors, right_lane_neighbors, all_neighbors = [], [], []
    # cars behind
    stop = 0
    if all_cars[fix_position(i - 1, len_l), 0]:
        right_lane_neighbors.append(fix_position(i - 1, len_l))
        t = 1
        while all_cars[fix_position(i - 1 - t, len_l), 0]:
            t += 1
            if fix_position(i - 1 - t, len_l) == fix_position(i - 1, len_l):
                stop = 1
                break
            else:
                continue
        if stop:
            left_lane_neighbors.append('none')
        else:
            left_lane_neighbors.append(fix_position(i - 1 - t, len_l))
    else:
        left_lane_neighbors.append(fix_position(i - 1, len_l))
        t = 1
        while all_cars[fix_position(i - 1 - t, len_l), 0] == 0:
            t += 1
            if fix_position(i - 1 - t, len_l) == fix_position(i - 1, len_l):
                stop = 1
                break
            else:
                continue
        if stop:
            right_lane_neighbors.append('none')
        else:
            right_lane_neighbors.append(fix_position(i - 1 - t, len_l))
    # cars forward
    stop = 0
    if all_cars[fix_position(i + 1, len_l), 0]:
        right_lane_neighbors.append(fix_position(i + 1, len_l))
        t = 1
        while all_cars[fix_position(i + 1 + t, len_l), 0]:
            t += 1
            if fix_position(i + 1 + t, len_l) == fix_position(i + 1, len_l):
                stop = 1
                break
            else:
                continue
        if stop:
            left_lane_neighbors.append('none')
        else:
            left_lane_neighbors.append(fix_position(i + 1 + t, len_l))
    else:
        left_lane_neighbors.append(fix_position(i + 1, len_l))
        t = 1
        while all_cars[fix_position(i + 1 + t, len_l), 0] == 0:
            t += 1
            if fix_position(i + 1 + t, len_l) == fix_position(i + 1, len_l):
                stop = 1
                break
            else:
                continue
        if stop:
            right_lane_neighbors.append('none')
        else:
            right_lane_neighbors.append(fix_position(i + 1 + t, len_l))
    all_neighbors = [left_lane_neighbors[0], right_lane_neighbors[0], left_lane_neighbors[1], right_lane_neighbors[1]]
    for j in range(len(all_neighbors)):
        if all_neighbors[j] == i:
            all_neighbors[j] = 'none'
    return all_neighbors


def neighbors_distance(all_cars, i, road_len):  # returns a list of gaps between car i and her neighbors, type:  [lb, rb, lf, rf]
    neighbors_list = neighbors(all_cars, i)
    # d_lb
    if neighbors_list[0] == 'none':
        d_lb = 'none'
    else:
        if neighbors_list[0] < i:
            d_lb = all_cars[i, 1] - all_cars[neighbors_list[0], 1] - 1
        else:
            d_lb = all_cars[i, 1] + road_len - all_cars[neighbors_list[0], 1] - 1
    # d_rb
    if neighbors_list[1] == 'none':
        d_rb = 'none'
    else:
        if neighbors_list[1] < i:
            d_rb = all_cars[i, 1] - all_cars[neighbors_list[1], 1] - 1
        else:
            d_rb = all_cars[i, 1] + road_len - all_cars[neighbors_list[1], 1] - 1
    # d_lf
    if neighbors_list[2] == 'none':
        d_lf = 'none'
    else:
        if neighbors_list[2] > i:
            d_lf = all_cars[neighbors_list[2], 1] - 1 - all_cars[i, 1]
        else:
            d_lf = all_cars[neighbors_list[2], 1] + road_len - all_cars[i, 1] - 1
    # d_rf
    if neighbors_list[3] == 'none':
        d_rf = 'none'
    else:
        if neighbors_list[3] > i:
            d_rf = all_cars[neighbors_list[3], 1] - 1 - all_cars[i, 1]
        else:
            d_rf = all_cars[neighbors_list[3], 1] + road_len - all_cars[i, 1] - 1
    return [d_lb, d_rb, d_lf, d_rf]


def my_binary_search(y, el):  # returns a new list of cars with a inserted car 'el'
    x = copy.deepcopy(y.tolist())
    if not x:
        x.append(el)
        return np.array(x)
    else:
        k, i, j = 0, 0, len(x) - 1
        if el[1] <= x[0][1]:
            if x[0][1] == el[1]:
                if x[0][0]:
                    x.insert(0, el)
                else:
                    x.insert(1, el)
            else:
                x.insert(0, el)
        elif el[1] >= x[-1][1]:
            if x[-1][1] == el[1]:
                if x[-1][0]:
                    x.insert(-1, el)
                else:
                    x.append(el)
            else:
                x.append(el)
        elif True:
            i = 0
            while j - i > 1:
                k = (i + j) // 2
                if x[k][1] <= el[1]:
                    i = k
                else:
                    j = k
            # right neighbor -> left neighbor
            if x[j][1] == el[1]:
                if x[j][0]:
                    x.insert(j, el)
                else:
                    x.insert(j + 1, el)
            elif x[j - 1][1] == el[1]:
                if x[j - 1][0]:
                    x.insert(j - 1, el)
                else:
                    x.insert(j, el)
            else:
                x.insert(j, el)
        return np.array(x)


def in_range_q(x, r):  # returns True, if X in range r, False - if isn't
    return r[0] <= x <= r[-1]


def in_zone(x, zone_coords):  # returns True, if x in zone, False - if isn't
    s = False
    for j in zone_coords:
        if in_range_q(x, j):
            s = True
            break
    return s


def what_zone(x, cz=0, oz=0):  # returns a name of zone which x in
    z = 0
    if cz and in_zone(x, cz):
        z = 'conv-zone'
    elif (not z) and oz and in_zone(x, oz):
        z = 'obstr-zone'
    else:
        z = 'two-lane-zone'
    return z


def lane_change(all_cars, i, road_len, cz, oz):  # returns True if car i is able to change the lane, False if isn't
    neighbors_list = neighbors(all_cars, i)
    neighbors_distance_list = neighbors_distance(all_cars, i, road_len)
    # convergence zone
    if what_zone(all_cars[i, 1], cz, oz) == 'conv-zone':
        if not all_cars[i, 0]:
            return False
        else:
            if neighbor_cell(all_cars, i):
                # c1
                if neighbors_distance_list[2] == 'none':
                    c1 = True
                else:
                    c1 = all_cars[i, 2] <= neighbors_distance_list[2]
                # c2
                if neighbors_list[0] == 'none':
                    c2 = True
                else:
                    c2 = all_cars[neighbors_list[0], 2] <= neighbors_distance_list[0]
                return c1 & c2
            else:
                return False
    # obstruction zone
    elif what_zone(all_cars[i, 1], cz, oz) == 'obstr-zone':
        return False
    # two-lane street
    else:
        if all_cars[i, 0]:
            if neighbors_list[3] == 'none':
                dv = 0
            else:
                dv = all_cars[i, 2] - all_cars[neighbors_list[3], 2]
            w = max(0, min(0.8, 0.1 * dv))
            if neighbor_cell(all_cars, i):
                # c1
                if neighbors_distance_list[3] == 'none':
                    c1 = True
                else:
                    c1 = all_cars[i, 2] > neighbors_distance_list[3]
                # c2
                if neighbors_list[3] == 'none':
                    c2 = True
                else:
                    c2 = all_cars[i, 2] > all_cars[neighbors_list[3], 2]
                # c3
                if neighbors_distance_list[2] == 'none':
                    c3 = True
                else:
                    c3 = all_cars[i, 2] <= neighbors_distance_list[2]
                # c4
                if neighbors_list[0] == 'none':
                    c4 = True
                else:
                    c4 = all_cars[neighbors_list[0], 2] <= neighbors_distance_list[0]
                # c5
                c5 = random.random() < w
                return c1 & c2 & c3 & c4 & c5
            else:
                return False
        else:
            if neighbor_cell(all_cars, i):
                if neighbors_list[1] == 'none':
                    c1 = True
                else:
                    c1 = all_cars[neighbors_list[1], 2] <= neighbors_distance_list[1]
                if neighbors_distance_list[3] == 'none':
                    c2 = True
                else:
                    c2 = all_cars[i, 2] <= neighbors_distance_list[3]
                return c1 & c2
            else:
                return False


def acceleration(car_speed, car_x, cz, oz, v_max_two_lane=5, v_max_conv_zone=2, v_max_obstr_zone=3):  # returns a value of the speed
    if what_zone(car_x, cz, oz) == 'conv-zone':
        return min(car_speed + 1, v_max_conv_zone)
    elif what_zone(car_x, cz, oz) == 'obstr-zone':
        return min(car_speed + 1, v_max_obstr_zone)
    else:
        return min(car_speed + 1, v_max_two_lane)


def braking(all_cars, i, road_len):  # returns a value of the speed
    neighbors_distance_list = neighbors_distance(all_cars, i, road_len)
    if all_cars[i, 0]:
        if neighbors_distance_list[3] != 'none':
            v = min(all_cars[i, 2], neighbors_distance_list[3])
            if neighbors_distance_list[2] != 'none':
                v = min(v, neighbors_distance_list[2] + 1)
        else:
            v = all_cars[i, 2]
    else:
        if neighbors_distance_list[2] != 'none':
            v = min(all_cars[i, 2], neighbors_distance_list[2])
        else:
            v = all_cars[i, 2]
    return v


def randomization(car_speed, p_brake):  # returns a value of the speed
    if (random.random() < p_brake) and (car_speed > 0):
        return car_speed - 1
    else:
        return car_speed


def movement(all_cars, i, road_len):  # returns a new position for a car
    return (all_cars[i, 1] + all_cars[i, 2]) % road_len


def new_array(all_cars):  # returns a new array of cars
    c = np.array([])
    for i in all_cars:
        c = my_binary_search(c, i)
    return c


def obstruction_model_step(array, road_len, v_max_two_lane=5, v_max_conv_zone=2, v_max_obstr_zone=3, p_brake=0.2, convergence_zone=0, obstruction_zone=0):
    # zones - lists of lists which contain coordinates of ends of zones
    array_c = copy.deepcopy(array)
    for i in range(len(array_c)):  # lane changing
        if car_q(array_c[i, 2]):
            if lane_change(array, i, road_len, convergence_zone, obstruction_zone):
                if array_c[i, 0]:
                    array_c[i, 0] = 0
                else:
                    array_c[i, 0] = 1
    array_c2 = copy.deepcopy(array_c)
    for i in range(len(array_c)):  # acceleration -> braking -> randomization
        if car_q(array_c[i, 2]):
            array_c2[i, 2] = acceleration(array_c[i, 2], array_c[i, 1], convergence_zone, obstruction_zone, v_max_two_lane, v_max_conv_zone, v_max_obstr_zone)  # acceleration
            array_c2[i, 2] = braking(array_c2, i, road_len)  # braking
            array_c2[i, 2] = randomization(array_c2[i, 2], p_brake)  # randomization
    for i in range(len(array_c2)):
        if car_q(array_c2[i, 2]):
            array_c2[i, 1] = movement(array_c2, i, road_len)  # movement
    return new_array(array_c2)
