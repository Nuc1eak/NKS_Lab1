import numpy as np

INPUT_DATA = sorted(np.array([189, 833, 733, 219, 137, 1542, 164, 261,
                              380, 82, 1668, 1282, 472, 279, 1128, 1715,
                              206, 826, 255, 1528, 353, 296, 1267, 215,
                              58, 346, 618, 562, 341, 1742, 70, 154, 224,
                              1038, 41, 1438, 405, 415, 89, 368, 283, 338,
                              444, 566, 206, 2111, 398, 878, 1766, 128,
                              859, 2853, 23, 1427, 1025, 551, 552, 69,
                              482, 269, 377, 100, 419, 817, 609, 1581,
                              1468, 22, 587, 58, 2313, 104, 122, 154, 493,
                              91, 1591, 447, 15, 101, 1661, 189, 524, 265,
                              370, 221, 1149, 448, 1175, 7, 318, 2084,
                              156, 558, 91, 432, 773, 406, 2088, 83]))

Y_PERCENTAGE = 0.98  # у
TROUBLE_PROOF_WORK_TIME = 414  # час безвідмовної роботи
DEPTH_TIME = 2077  # час інтенсивності відмов
N = len(INPUT_DATA)  # кількість елементів вибірки
K = 10  # кількість інтервалів

max_number = INPUT_DATA[N - 1]
h = max_number / K  # розмах вибірки

intervals = [round(interval * h, 1) for interval in range(K + 1)]
print("Інтервали:", intervals)


def sort_data_via_intervals(data, data_intervals):
    sorted_data = []
    for i in range(K):
        sorted_data.append([])
        for element in data:
            if data_intervals[i] <= element <= data_intervals[i + 1]:
                sorted_data[i].append(element)
    return sorted_data


def f_bar_graph_calculator(data):
    f_bar_graph = []
    for i in range(K):
        f_bar_graph.append(round(len(data[i]) / (N * h), 6))
    return f_bar_graph


def probabilities_calculator(f_array):
    probabilities = []
    for i in range(K):
        area = 0
        for j in range(i + 1):
            area += f_array[j] * h
        probabilities.append(round(1 - area, 2))
    return probabilities


def t_y_calculator(probability):
    d = round((probability - Y_PERCENTAGE) / (probability - 1), 2)
    return round(h - h * d, 2)


def trouble_proof_work_time_probability(f_arr, time):
    square = 0
    i = 0
    while intervals[i + 1] < time:
        square += f_arr[i] * h
        i += 1
    square += f_arr[i] * (time - intervals[i])
    return round(1 - square, 5)


def find_index(number):
    for i in range(K):
        if intervals[i] <= number <= intervals[i + 1]:
            return i


def intensity_trouble_on_time(f_arr):
    index = find_index(DEPTH_TIME)
    probability = trouble_proof_work_time_probability(f_arr, DEPTH_TIME)
    return round(f_arr[index] / probability, 6)


t_cr = sum(INPUT_DATA) / N

sorted_data_intervals = sort_data_via_intervals(INPUT_DATA, intervals)

f = f_bar_graph_calculator(sorted_data_intervals)

p = probabilities_calculator(f)

t_y = t_y_calculator(p[0])

p_time = trouble_proof_work_time_probability(f, TROUBLE_PROOF_WORK_TIME)

intensity = intensity_trouble_on_time(f)

print("Середній наробіток до відмови:", t_cr)
print("Y-відсотковий наробіток на відмову при γ = {}: {}".format(Y_PERCENTAGE, t_y))
print("Ймовірність безвідмовної роботи на час {} годин: {}".format(TROUBLE_PROOF_WORK_TIME, p_time))
print("інтенсивність відмов на час {} годин: {}".format(DEPTH_TIME, intensity))
