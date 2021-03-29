def parallel_calculator(p_first_el, p_second_el):
    return round(1 - (1 - p_first_el) * (1 - p_second_el), 6)


#  Ймовірність безвідмовної роботи кожного елемента
P = [0.59, 0.84, 0.5, 0.27, 0.59, 0.61]

#  перетворимо трикутник з Р2, Р3 і Р4 в зірку Р2*, Р3* та Р4*
p2 = parallel_calculator(P[1], P[2])
p3 = parallel_calculator(P[2], P[3])
p4 = parallel_calculator(P[1], P[3])

#  з'єдноємо Р1 та Р2, Р3 та Р6, Р4 та Р5
p1 = P[0] * p2
p3 *= P[5]
p4 *= P[4]

#  з'єднаю дві паралельні Р, а саме Р3 та Р4
p2 = parallel_calculator(p3, p4)
p_all = round(p1 * p2, 5)
print(p_all)
