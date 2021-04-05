from lr2 import *
import math


def reservation_quality_criteria(Q_reserve, P_reserve, T_reserve, Q_main, P_main, T_main):
    G_q = round(Q_reserve / Q_main, 2)
    G_p = round(P_reserve / P_main, 2)
    G_t = round(T_reserve / T_main, 2)

    return G_q, G_p, G_t


def t_system_calculator(P_system):
    return round(-T / math.log1p(P_system - 1), 4)


def general_unloaded(q, K):
    return round(1 / math.factorial(K + 1) * q, 6)


def separate_loaded(p, K):
    return round((1 - p) ** (K + 1), 6)


# start - початок, end - кінець
graph = {
    "start": ["1"],
    "1": ["2", "3"],
    "2": ["4", "5"],
    "3": ["4", "6"],
    "4": ["5", "6"],
    "5": ["end"],
    "6": ["end"],
    "end": []
}

# ймовірності кожного стану
probabilities = {"start": 0.0, "1": 0.59, "2": 0.84, "3": 0.5, "4": 0.27, "5": 0.59, "6": 0.61, "end": 0.0}

# Знаходимо всі шляхи за допомогою функції
all_paths = paths("start", "end", graph)

# Знайдемо усі можливі стани системи
all_system_states = set(all_states_finder(graph, all_paths))

# Розрахуємо ймовірності для кожного стану
string_of_all_states, all_states_probabilities = all_probs_calculator(graph, probabilities, all_system_states)

P = round(sum(all_states_probabilities), 6)  # ймовірність відмови
T = 1951  # час
K1, K2 = 1, 3  # кратності резервування
Q = 1 - P

T_system = t_system_calculator(P)

print("Результи попередньої роботи\n"
      "P_system({}) = {}\n"
      "Q_system({}) = {}\n"
      "T_system = {}".format(T, P, T, Q, T_system))

probabilities_reserved = probabilities.copy()
for i in probabilities.keys():
    probabilities_reserved.update({i: round(1 - separate_loaded(probabilities[i], K1), 4)})
str_p, all_reserved_probabilities = all_probs_calculator(graph, probabilities_reserved, all_system_states)

print("Ймовірністі безвідмовної роботи кожного елемента до і після роздільного резервування:\n"
      "{}\n"
      "{}".format(probabilities, probabilities_reserved))

P_separate_reserved = round(sum(all_reserved_probabilities), 6)
Q_separate_reserved = round(1 - P_separate_reserved, 6)
T_separate_reserved = t_system_calculator(P_separate_reserved)

print("Ймовірність безвідмовної роботи, відмови та значення середнього наробітку на час {} годин системи з розділеним "
      "навантаженням і кратністю {}\n"
      "P_reserved({}) = {}\n"
      "Q_reserved({}) = {}\n"
      "T_reserved = {}".format(T, K1, T, P_separate_reserved, T, Q_separate_reserved, T_separate_reserved))

Gq, Gp, Gt = reservation_quality_criteria(Q_separate_reserved, P_separate_reserved, T_separate_reserved, Q, P, T_system)

print("Виграш надійності протягом часу {} годин за ймовірностю відмов:\nGq = {}\n"
      "Виграш надійності протягом часу {} годин за ймовірностю безвідмовної роботи:\nGp = {}\n"
      "Виграш надійності за середнім часом безвідмовної роботи:\nGt = {}".format(T, Gq, T, Gp, Gt))

Q_general_reserved = general_unloaded(Q, K2)
P_general_reserved = round(1 - Q_general_reserved, 6)
T_general_reserved = t_system_calculator(P_general_reserved)

print("Ймовірність безвідмовної роботи, відмови та значення середнього наробітку на час {} годин системи з загальним "
      "ненавантаженням і кратністю {}\n"
      "P_reserved({}) = {}\n"
      "Q_reserved({}) = {}\n"
      "T_reserved = {}".format(T, K2, T, P_general_reserved, T, Q_general_reserved, T_general_reserved))

Gq, Gp, Gt = reservation_quality_criteria(Q_general_reserved, P_general_reserved, T_general_reserved, Q, P, T_system)

print("Виграш надійності протягом часу {} годин за ймовірностю відмов:\nGq = {}\n"
      "Виграш надійності протягом часу {} годин за ймовірностю безвідмовної роботи:\nGp = {}\n"
      "Виграш надійності за середнім часом безвідмовної роботи:\nGt = {}".format(T, Gq, T, Gp, Gt))
