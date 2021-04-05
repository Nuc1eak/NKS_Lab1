import itertools


def paths(first_state, last_state, graph_of_paths, curr_path=None):
    if curr_path is None:
        curr_path = []
    curr_path = curr_path + [first_state]
    all_graph_paths = []
    if first_state == last_state:
        return [curr_path]
    if first_state not in graph_of_paths:
        return []
    for y in graph_of_paths[first_state]:
        if y not in curr_path:
            create_paths = paths(y, last_state, graph_of_paths, curr_path)
            for u in create_paths:
                all_graph_paths.append(u)
    return all_graph_paths


def all_states_finder(graph_of_paths, all_paths_list):
    comb = []
    full_list_comb = []
    all_graph_system_states = []
    all_states = graph_of_paths.keys()
    for state in range(1, len(graph_of_paths.keys()) + 1):
        comb.append(list(itertools.combinations(all_states, state)))
    for combination in comb:
        for state in combination:
            full_list_comb.append(state)

    for list_comb in full_list_comb:
        for path in all_paths_list:
            if set(path).issubset(set(list_comb)):
                all_graph_system_states.append(list_comb)
    return all_graph_system_states


def all_probs_calculator(system_graph, system_probabilities, system_states):
    all_probabilities = []
    string = ""
    for state in system_states:
        probability = 1
        for key in system_graph.keys():
            if key in state and key != "end" and key != "start":
                string += "+  "
                probability *= system_probabilities[key]
            elif key not in state and key != "end" and key != "start":
                string += "-  "
                probability *= 1 - system_probabilities[key]
        string += str(round(probability, 6)) + "\n"
        all_probabilities.append(probability)
    return string, all_probabilities


if __name__ == "__main__":
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

    title = ""
    for i in range(len(graph) - 2):
        title += "E" + str(i + 1) + " "

    print("Таблиця зв'язків системи")
    print("  ", title)
    matrix = ""
    for i in range(1, len(graph) - 1):
        matrix += "E" + str(i) + " "
        for j in range(1, len(graph) - 1):
            if str(j) in graph[str(i)]:
                matrix += " 1 "
            else:
                matrix += " 0 "
        matrix += "\n"
    print(matrix)

    print("Усі можливі шляхи")
    path_string = ""
    for i in all_paths:
        for j in i:
            if str(j).isdecimal():
                path_string += "E" + str(j) + "->"
        path_string = path_string[:-2]
        path_string += "\n"
    print(path_string)

    print("Таблиця працездатних станів системи")
    print(title + "P_state")
    print(string_of_all_states)

    P = sum(all_states_probabilities)
    print("Ймовірність безвідмовної роботи системи: ", round(P, 6))
