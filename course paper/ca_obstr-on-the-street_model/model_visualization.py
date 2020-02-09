import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import copy
import random

import an_obstruction_on_the_street_model as mymodel


def add_car_free_place_q(array, l_car):  # returns True, if a car is able to be added, False - if isn't
    if l_car:
        for i in range(len(array[:2])):
            if array[i][1]:  # if x > 0
                return [True, i]
            else:  # if x = 0
                if array[i][0]:  # if i'st element of list of cars at right line
                    return [False]
        return [True, 0]
    else:
        for i in range(len(array[:1])):
            if array[i][1]:
                return [True, i]
            else:
                return [False]
        return [True, 0]


def add_car(array, road_len, l_car, v_car):  # returns a new array of cars if new car is able to be added, returns the same array - if ins't
    t = add_car_free_place_q(array, l_car)
    if t[0]:
        array_c = array.tolist()
        array_c.insert(t[1], [l_car, 0, v_car])
        neighbors_list = mymodel.neighbors(np.array(array_c), t[1])
        neighbors_distance_list = mymodel.neighbors_distance(np.array(array_c), t[1], road_len)
        if neighbors_list[0 + l_car] == 'none':
            t1 = True
        else:
            t1 = array_c[neighbors_list[0 + l_car]][2] <= neighbors_distance_list[0 + l_car]
        if neighbors_distance_list[2 + l_car] == 'none':
            t2 = True
        else:
            t2 = v_car <= neighbors_distance_list[2 + l_car]
        if t1 and t2:
            return np.array(array_c)
        else:
            return array
    return array


def make_array(sparse_array, road_len):  # returns an np.array transformed from my sparse array
    array = np.zeros((2, road_len + 1), dtype=np.float)
    for i in sparse_array:
        if i[2] >= 0:
            array[i[0], i[1]] = 1
        else:
            array[i[0], i[1]] = 0.5
    return array


def make_obstruction_zone(array, zone_ends):
    array_c = mymodel.my_binary_search(array, [1, zone_ends[0], -1])
    for i in range(zone_ends[0] + 1, zone_ends[1] + 1):
        array_c = mymodel.my_binary_search(array_c, [1, i, -1])
    return array_c


def make_all_obstruction_zone(array, obstr_zone):
    array_c = copy.deepcopy(array)
    for i in obstr_zone:
        array_c = make_obstruction_zone(array_c, i)
    return array_c


# mymodel_vis.get_steps(3600, np.array([]), 10820, 5, 0.2, [[1000, 1020]], [[1021, 1820]], 1, [], t)
def get_steps(n, array, road_len, v_max_two_lane=5, v_max_conv_zone=2, v_max_obstr_zone=3, p_brake=0.2, convergence_zone=0, obstruction_zone=0, aadd=0, addit_cars=[], random_addition=0):  # returns an array of model's steps of [road_len, step0, step1, ... , stepn-1] type
    # gets a list of type [[l_car, v_car, step], .., [l_car, v_car, step]] or nothing as addit_cars variable
    car_insert_step = random.randint(15, 40) - 1
    q = random_addition
    if obstruction_zone:
        out_arrays = [road_len, make_all_obstruction_zone(array, obstruction_zone)]
    else:
        out_arrays = [road_len, array]
    l = len(addit_cars)
    t = 0
    # print('car_insert_step is {0}'.format(car_insert_step))  # delete it
    for i in range(n):
        print('step: {0}'.format(i))  # delete it
        if aadd:
            if addit_cars and t != l:  # nonrandom addition of cars
                if i == addit_cars[t][2]:
                    out_arrays.append(
                        add_car(
                            mymodel.obstruction_model_step(
                                out_arrays[-1], road_len, v_max_two_lane, v_max_conv_zone, v_max_obstr_zone,
                                p_brake, convergence_zone, obstruction_zone
                            ),
                            road_len, addit_cars[t][0], addit_cars[t][1]
                        )
                    )
                    t += 1
                else:
                    out_arrays.append(
                        mymodel.obstruction_model_step(
                            out_arrays[-1], road_len, v_max_two_lane, v_max_conv_zone, v_max_obstr_zone,
                            p_brake, convergence_zone, obstruction_zone
                        )
                    )
            elif addit_cars and t == l:  # if additional cars were ended
                out_arrays.append(
                        mymodel.obstruction_model_step(
                            out_arrays[-1], road_len, v_max_two_lane, v_max_conv_zone, v_max_obstr_zone,
                            p_brake, convergence_zone, obstruction_zone
                        )
                    )
            elif random_addition:  # random addition of cars
                if car_insert_step == i and q:
                    new_array_1 = mymodel.obstruction_model_step(
                            out_arrays[-1], road_len, v_max_two_lane, v_max_conv_zone, v_max_obstr_zone,
                        p_brake, convergence_zone, obstruction_zone
                        )
                    new_array_2 = add_car(new_array_1, road_len, random.randint(0, 1), random.randint(1, 3))
                    if new_array_1.tolist() == new_array_2.tolist():
                        car_insert_step += 1
                        out_arrays.append(new_array_1)
                    else:
                        out_arrays.append(new_array_2)
                        car_insert_step = i + random.randint(8, 15)
                        q -= 1
                else:
                    out_arrays.append(
                        mymodel.obstruction_model_step(
                            out_arrays[-1], road_len, v_max_two_lane, v_max_conv_zone, v_max_obstr_zone,
                            p_brake, convergence_zone, obstruction_zone
                        )
                    )
        else:
            out_arrays.append(
                mymodel.obstruction_model_step(
                    out_arrays[-1], road_len, v_max_two_lane, v_max_conv_zone, v_max_obstr_zone,
                    p_brake, convergence_zone, obstruction_zone
                )
            )
    return out_arrays


def make_animation(steps):  # returns an animation of a traffic flow
    fig = plt.figure()
    frames = []
    rl = steps[0]
    for i in steps[1:]:
        j = make_array(i, rl)
        im = plt.imshow(j, cmap='Blues', animated=True)
        frames.append([im])
    animation.ArtistAnimation(fig, frames, interval=320, blit=True, repeat_delay=5000)
    plt.show()
