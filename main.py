import tkinter as tk
import networkx as nx
import random
import matplotlib.pyplot as plt
import numpy as np
from network2tikz import plot

def max_flow(flow_matrix):
    # Создание графа
    graph = nx.DiGraph()

    # Добавление ребер и пропускных способностей
    for i in range(flow_matrix.shape[0]):
        for j in range(flow_matrix.shape[1]):
            if flow_matrix[i, j] > 0:
                graph.add_edge(i + 1, j + 1, capacity=flow_matrix[i, j])

    # Нахождение максимального потока
    source = 1
    sink = flow_matrix.shape[0]
    max_flow_value = nx.maximum_flow_value(graph, source, sink)

    # Нахождение минимального разреза
    _, partition = nx.minimum_cut(graph, source, sink)
    min_raz = str(partition[1])
    min_raz = min_raz.strip("{}")

    # Возвращение максимального потока и минимального разреза
    return max_flow_value, min_raz


# макс поток
def max_potok():
    def gen_potok():
        def generate_flow_matrix():
            # Создание пустой матрицы 8x8
            flow_matrix = np.zeros((8, 8))

            # Установка обязательных ребер
            edges = [(1, 2), (2, 4), (4, 6), (6, 8), (7, 8), (5, 7), (3, 5), (1, 3)]
            for node1, node2 in edges:
                value = np.random.randint(10, 50)  # Генерация случайного значения от 10 до 30
                flow_matrix[node1 - 1, node2 - 1] = value
                flow_matrix[node2 - 1, node1 - 1] = value

            # Генерация случайного числа для определения количества дополнительных ребер
            num_extra_edges = np.random.randint(4, 6)

            # Добавление дополнительных ребер
            for _ in range(num_extra_edges):
                if np.random.randint(1, 10) < 4:
                    # Добавление ребер 2-5, 3-4, 4-7, 5-6
                    extra_edges = [(2, 5), (3, 4), (4, 7), (5, 6)]
                else:
                    # Добавление ребер 1-4, 1-5, 1-7, 1-6, 2-7, 3-6, 5-8, 4-8, 1-8
                    extra_edges = [(1, 4), (1, 5), (1, 7), (1, 6), (2, 7), (3, 6), (5, 8), (4, 8)]

                # Выбор случайного дополнительного ребра из списка
                extra_edge = random.choice(extra_edges)

                node1, node2 = extra_edge
                value = np.random.randint(10, 50)  # Генерация случайного значения от 10 до 30

                # Добавление маленького отличия к значению
                diff = np.random.uniform(0.05, 0.15)  # Генерация случайного множителя от 0.05 до 0.15
                value += value * diff

                flow_matrix[node1 - 1, node2 - 1] = value
                flow_matrix[node2 - 1, node1 - 1] = value

            return flow_matrix

        def generate_latex_code(flow_matrix, figure_number):
            latex_code = r'''
        \begin{center} 
        Исследование операций Ответ --  2023 
        \end{center}
        \newline 
        \begin{center}
        \textbf{Выполнил ................................................... группа .........   Задание по теме <<Поиск максимального потока в сети.>> }
        \end{center}
        \begin{flushleft} 
        \begin{center}     
        \textit{Найти максимальный поток в графе} 
        \end{center}
        \end{flushleft}  
        \begin{figure}[ht]
        \centering
        \begin{tikzpicture}[->,>=stealth',shorten >=1pt,auto,node distance=3cm,
                            thick,main node/.style={circle,fill=blue!20,draw,font=\sffamily\Large\bfseries}]
          \node[main node] (1) [left]{1};
          \node[main node] (2) [above right of=1] {2};
          \node[main node] (3) [below right of=1] {3};
          \node[main node] (4) [right of=2] {4};
          \node[main node] (5) [right of=3] {5};
          \node[main node] (6) [right of=4] {6};
          \node[main node] (7) [right of=5] {7};
          \node[main node] (8) [below right of=6] {8};

          % Вставка значений из матрицы
        '''

            num_nodes = flow_matrix.shape[0]
            edges = []
            for i in range(num_nodes):
                for j in range(i + 1, num_nodes):
                    if flow_matrix[i, j] != 0:
                        if i == 0 and j == 1:
                            edges.append((i + 1, j + 1, "x", "above=5", ""))
                        if i == 0 and j == 2:
                            edges.append((i + 1, j + 1, "x", "below=5", ""))
                        if i == 1 and j == 3:
                            edges.append((i + 1, j + 1, "x", "above=5", ""))
                        if i == 2 and j == 4:
                            edges.append((i + 1, j + 1, "x", "below=5", ""))
                        if i == 3 and j == 5:
                            edges.append((i + 1, j + 1, "x", "above=5", ""))
                        if i == 4 and j == 6:
                            edges.append((i + 1, j + 1, "x", "below=5", ""))
                        if i == 5 and j == 7:
                            edges.append((i + 1, j + 1, "x", "above=5", ""))
                        if i == 6 and j == 7:
                            edges.append((i + 1, j + 1, "x", "below=5", ""))

                        if i == 1 and j == 4:
                            edges.append((i + 1, j + 1, "x", "above=5", ""))
                        if i == 2 and j == 3:
                            edges.append((i + 1, j + 1, "x", "below=5", ""))
                        if i == 3 and j == 6:
                            edges.append((i + 1, j + 1, "x", "above=5", ""))
                        if i == 4 and j == 5:
                            edges.append((i + 1, j + 1, "x", "below=5", ""))

                        if i == 0 and j == 3:
                            edges.append((i + 1, j + 1, "x", "below", ""))
                        if i == 0 and j == 4:
                            edges.append((i + 1, j + 1, "x", "below", ""))
                        if i == 0 and j == 5:
                            edges.append((i + 1, j + 1, "x", "below", ""))
                        if i == 0 and j == 6:
                            edges.append((i + 1, j + 1, "x", "below", ""))
                        if i == 1 and j == 6:
                            edges.append((i + 1, j + 1, "x", "above", ""))
                        if i == 2 and j == 5:
                            edges.append((i + 1, j + 1, "x", "below", ""))

                        if i == 1 and j == 7:
                            edges.append((i + 1, j + 1, "x", "below", ""))
                        if i == 2 and j == 7:
                            edges.append((i + 1, j + 1, "x", "below", ""))
                        if i == 3 and j == 7:
                            edges.append((i + 1, j + 1, "x", "below", ""))
                        if i == 4 and j == 7:
                            edges.append((i + 1, j + 1, "x", "below", ""))

            for i, (node1, node2, label, p, r) in enumerate(edges):
                latex_code += f'  \draw ({node1}) -- node[label, {p}, {r}] {{{int(flow_matrix[node1 - 1, node2 - 1])}}} ({node2});\n'

            latex_code += f'''
        \end{{tikzpicture}}
        \caption{{}}
        \end{{figure}}
        '''
            gg = max_flow(flow_matrix)
            max_flow_value = int(gg[0])
            partition = gg[1]
            latex_code += "Максимальный поток: " + str(max_flow_value) + r"\\"
            latex_code += "Справа минимального разреза находятся вершины: " + str(partition) + r"\\"
            # min_cut = find_min_cut(flow_matrix)
            # latex_code += min_cut + r"\\"
            latex_code += f'''
            \end{{figure}}
            '''
            latex_code += r'''
                        \newpage
                        '''
            return latex_code

        def generate_latex_code_answer(flow_matrix, figure_number):
            latex_code = r'''
        \begin{center} 
        Исследование операций --  2023 
        \end{center}
        \newline 
        \begin{center}
        \textbf{Выполнил ................................................... группа .........   Задание по теме <<Поиск максимального потока в сети.>> }
        \end{center}
        \begin{flushleft} 
        \begin{center}     
        \textit{Найти максимальный поток в графе} 
        \end{center}
        \end{flushleft}  
        \begin{figure}[ht]
        \centering
        \begin{tikzpicture}[->,>=stealth',shorten >=1pt,auto,node distance=3cm,
                            thick,main node/.style={circle,fill=blue!20,draw,font=\sffamily\Large\bfseries}]
          \node[main node] (1) [left]{1};
          \node[main node] (2) [above right of=1] {2};
          \node[main node] (3) [below right of=1] {3};
          \node[main node] (4) [right of=2] {4};
          \node[main node] (5) [right of=3] {5};
          \node[main node] (6) [right of=4] {6};
          \node[main node] (7) [right of=5] {7};
          \node[main node] (8) [below right of=6] {8};

          % Вставка значений из матрицы
        '''

            num_nodes = flow_matrix.shape[0]
            edges = []
            for i in range(num_nodes):
                for j in range(i + 1, num_nodes):
                    if flow_matrix[i, j] != 0:
                        if i == 0 and j == 1:
                            edges.append((i + 1, j + 1, "x", "above=5", ""))
                        if i == 0 and j == 2:
                            edges.append((i + 1, j + 1, "x", "below=5", ""))
                        if i == 1 and j == 3:
                            edges.append((i + 1, j + 1, "x", "above=5", ""))
                        if i == 2 and j == 4:
                            edges.append((i + 1, j + 1, "x", "below=5", ""))
                        if i == 3 and j == 5:
                            edges.append((i + 1, j + 1, "x", "above=5", ""))
                        if i == 4 and j == 6:
                            edges.append((i + 1, j + 1, "x", "below=5", ""))
                        if i == 5 and j == 7:
                            edges.append((i + 1, j + 1, "x", "above=5", ""))
                        if i == 6 and j == 7:
                            edges.append((i + 1, j + 1, "x", "below=5", ""))

                        if i == 1 and j == 4:
                            edges.append((i + 1, j + 1, "x", "above=5", ""))
                        if i == 2 and j == 3:
                            edges.append((i + 1, j + 1, "x", "below=5", ""))
                        if i == 3 and j == 6:
                            edges.append((i + 1, j + 1, "x", "above=5", ""))
                        if i == 4 and j == 5:
                            edges.append((i + 1, j + 1, "x", "below=5", ""))

                        if i == 0 and j == 3:
                            edges.append((i + 1, j + 1, "x", "below", ""))
                        if i == 0 and j == 4:
                            edges.append((i + 1, j + 1, "x", "below", ""))
                        if i == 0 and j == 5:
                            edges.append((i + 1, j + 1, "x", "below", ""))
                        if i == 0 and j == 6:
                            edges.append((i + 1, j + 1, "x", "below", ""))
                        if i == 1 and j == 6:
                            edges.append((i + 1, j + 1, "x", "above", ""))
                        if i == 2 and j == 5:
                            edges.append((i + 1, j + 1, "x", "below", ""))

                        if i == 1 and j == 7:
                            edges.append((i + 1, j + 1, "x", "below", ""))
                        if i == 2 and j == 7:
                            edges.append((i + 1, j + 1, "x", "below", ""))
                        if i == 3 and j == 7:
                            edges.append((i + 1, j + 1, "x", "below", ""))
                        if i == 4 and j == 7:
                            edges.append((i + 1, j + 1, "x", "below", ""))

            for i, (node1, node2, label, p, r) in enumerate(edges):
                latex_code += f'  \draw ({node1}) -- node[label, {p}, {r}] {{{int(flow_matrix[node1 - 1, node2 - 1])}}} ({node2});\n'

            latex_code += f'''
        \end{{tikzpicture}}
        \caption{{}}
        \end{{figure}}
        '''
            latex_code += r'''
            \newpage
            '''

            return latex_code

        flow_matrix = generate_flow_matrix()
        figure_number = 1
        latex_code = generate_latex_code(flow_matrix, figure_number)
        answer_code = generate_latex_code(flow_matrix, figure_number)
        # Создание LaTeX-документа с графами
        latex_document = r'''
        \documentclass[a4paper,12pt]{article}

        \usepackage[utf8]{inputenc}
        \usepackage[T1]{fontenc}
        \usepackage[russian]{babel}
        \usepackage{amsmath}
        \usepackage{tikz}
        \usetikzlibrary{graphs,graphs.standard}

        \begin{document}
        '''
        answer_document = r'''
                \documentclass[a4paper,12pt]{article}

                \usepackage[utf8]{inputenc}
                \usepackage[T1]{fontenc}
                \usepackage[russian]{babel}
                \usepackage{amsmath}
                \usepackage{tikz}
                \usetikzlibrary{graphs,graphs.standard}

                \begin{document}
                '''

        # Генерация графов и добавление их LaTeX-кода в документ
        num_graphs = int(entry_count.get())
        graphs_per_page = 2
        current_page = 1
        graphs_on_page = 0

        for i in range(num_graphs):
            flow_matrix = generate_flow_matrix()
            figure_number = i + 1
            latex_code = generate_latex_code(flow_matrix, figure_number)
            anwer_code = generate_latex_code_answer(flow_matrix, figure_number)
            latex_document += latex_code
            answer_document += anwer_code

            graphs_on_page += 1
            if graphs_on_page == graphs_per_page:
                latex_document += r'\newpage'  # Добавление разрыва страницы
                answer_document += r'\newpage'  # Добавление разрыва страницы
                graphs_on_page = 0
                current_page += 1

        latex_document += r'''
        \end{document}
        '''
        answer_document += r'''
                \end{document}
                '''

        MO = open("answer.tex", "w+", encoding='utf-8')
        MO.write(latex_document)
        MO2 = open("file.tex", "w+", encoding='utf-8')
        MO2.write(answer_document)
        win3.destroy()

    win3 = tk.Toplevel()
    win3.title("Задача о поиске максимального потока")
    win3.geometry("500x300+150+150")
    label_count = tk.Label(win3, text="Кол-во задач")
    label_count.place(x=100, y=100)
    entry_count = tk.Entry(win3)
    entry_count.place(x=200, y=100)
    butt_gen = tk.Button(win3, text="Сгенерировать", command=gen_potok)
    butt_gen.place(x=150, y=150)


def greedy_color(graph):
    colors = {}
    for node in graph.nodes():
        used_colors = set(colors.get(neighbour) for neighbour in graph.neighbors(node))
        available_colors = set(range(len(graph))) - used_colors
        color = min(available_colors)
        colors[node] = color
    return colors


# хроматическое число
def chromatic_number_task():
    def generate():
        preab = r'''
        \documentclass[a4paper,12pt]{article}
        \usepackage[utf8]{inputenc}
        \usepackage[T1]{fontenc}
        \usepackage[russian]{babel}
        \usepackage{amsmath}
        \usepackage{tikz}
        \usepackage{tikz-network}
        \usetikzlibrary{graphs,graphs.standard}
        \begin{document}
        '''
        q = int(entry_ver.get())
        n = int(entry_dug.get())
        count = int(entry_task.get())
        MO = open("chromo.tex", "w+", encoding='utf-8')
        MO.write(preab)
        for j in range(count):
            latex_document = r'''
             \begin{center} 
             Исследование операций --  2023 
            \end{center}
            \newline 
            \begin{center}
            \textbf{Выполнил ................................................... группа .........   Задание по теме <<Хроматическое число графа.>> }
            \end{center}
            \begin{flushleft} 
            \begin{center}     
            \textit{Найти хроматическое число в графе} 
            \end{center}
            \end{flushleft}
            '''
            G = nx.Graph()
            G.add_nodes_from(range(q))
            while G.number_of_edges() < n:
                u = random.randint(0, q - 1)
                v = random.randint(0, q - 1)
                if u != v:
                    G.add_edge(u, v)
          #  colors = list(greedy_color(G).values())
          #  plt.figure(figsize=(8, 6))
          #  nx.draw(G, with_labels=True)
           # plt.show()
           # plt.figure(figsize=(8, 6))
           # nx.draw(G, node_color=colors, with_labels=True)
           # count = max(colors) + 1
           # text1 = f"Ответ: {count}"
           # plt.text(-0.9, -0.9, text1, fontsize=12)
            #plt.show()
            win2.destroy()
            MO.write(latex_document)
            vertex_style = {
                'draw': 'red',
                'fill': 'white',
                'shape': 'circle',
                'minimum size': '20pt',
                'inner sep': '0pt',
            }
            edge_style = {
                'draw': 'blue',
                'line width': '2pt',
            }
            plot(G, 'graf.tex', vertex_style=vertex_style, edge_style=edge_style)
            graf_code = ""
            with open('graf.tex', 'r') as input_file:
                    for _ in range(3):
                        next(input_file)
                    for line in input_file:
                        if line != "\end{document}":
                            graf_code += line
            MO.write(graf_code)
        MO.write("\end{document}")




    win2 = tk.Toplevel()
    win2.title("Задача поиска хроматического числа")
    win2.geometry("500x400+100+100")
    label_ver = tk.Label(win2, text="Кол-во вершин")
    label_dug = tk.Label(win2, text="Кол-во дуг")
    label_task = tk.Label(win2, text="Кол-во задач")
    label_ver.place(x=100, y=100)
    label_dug.place(x=100, y=200)
    label_task.place(x=100, y=300)
    entry_ver = tk.Entry(win2)
    entry_dug = tk.Entry(win2)
    entry_task = tk.Entry(win2)
    entry_ver.place(x=200, y=100)
    entry_dug.place(x=200, y=200)
    entry_task.place(x=200, y=300)
    but_generat = tk.Button(win2, text="Cгенерировать", command=generate)
    but_generat.place(x=180, y=350)


window = tk.Tk()
window.geometry("700x400+150+150")
window.title("Генератор задач ИСО")
button1 = tk.Button(text="Задача поиска макс. потока", command=max_potok)
button1.place(x=220, y=100, width=250, height=50)

button2 = tk.Button(text="Задача поиска хроматического числа", command=chromatic_number_task)
button2.place(x=220, y=200, width=250, height=50)

window.mainloop()
