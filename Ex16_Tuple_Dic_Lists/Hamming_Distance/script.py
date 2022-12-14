#!/usr/bin/env python3


# Complete the following to implement the described hamming distance function.
# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def hamming_help(string_a,string_b):
    list_a = []
    list_b = []
    for i in string_a:
        list_a.append(i)
    for i in string_b:
        list_b.append(i)
    range_a = len(string_a)
    ind_a = -len(string_a)
    diff = 0

    for i in range(range_a):
        if list_a[ind_a] == list_b[ind_a]:
            ind_a += 1
            continue
        else:
            diff += 1
            ind_a += 1
            continue
    return string_a,string_b,diff


def hamming_dist(signal_1, signal_2):
    signal_1_list = signal_1["data"]
    if len(signal_1_list) != len(signal_2) or len(signal_1_list) == 0:
        return "Empty signal on at least one of the sensors"

    # if len(signal_1_list) == 0:
    #     return "Empty signal on at least one of the sensors"
    for i in signal_1_list:
        if len(i) == len(signal_2[0]):
            continue
        return "Sensor defect detected"

    for i in signal_2:
        if len(i) == len(signal_1_list[0]):
            continue
        return "Sensor defect detected"

###is it possible to bring the two blocks above together?
    # for i in signal_1_list and signal_sensor_2:
    #     if len(i) == len(signal_sensor_2[0]) and len(i) == len(signal_1_list[0]):
    #         continue
    #     return "Sensor defect detected"


#compares each string of both lists, does this by using the negative index
#if strings equal, "run_ind" gets larger, next strings
#if not equal, they get entered into hamming
    else:
        final = []
        run_rang = len(signal_1_list)
        run_ind = -len(signal_1_list)
        for i in range(run_rang):
            if signal_1_list[run_ind] == signal_2[run_ind]:
                run_ind = run_ind+1
            else:
                # print(signal_1_list[run_ind], signal_sensor_2[run_ind])
                run_ind = run_ind+1
                non_equal1 = signal_1_list[run_ind-1]
                non_equal2 = signal_2[run_ind-1]
                final.append(hamming_help(non_equal1,non_equal2))
        return final

signal_sensor_10 = {"times": [0, 1, 2, 3, 4, 5],
                   "data": ["00101110", "11001011", "11110000", "01000011", "11001101", "00011011"]}
signal_sensor_20 = ("00101110", "11001001", "11110011", "01111011", "11001101", "00011011")
print(hamming_dist(signal_sensor_10, signal_sensor_20))
