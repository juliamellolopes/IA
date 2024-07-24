import numpy as np
import matplotlib.pyplot as plt

def fill_matriz(number, m, n): #preenche a matriz com numeros aleatorios de 0 ou 1
    matriz = np.zeros((m, n), dtype=int)
    indices = np.random.choice(m*n, number, replace=False)
    np.put(matriz, indices, 1) 
    return matriz

def first_random_position(m, n): #retorna uma posicao aleatoria na matriz
    return [np.random.randint(0, m), np.random.randint(0, n)]

def random_movement(): #retorna uma direcao aleatoria
    return np.random.choice(["up", "down", "left", "right"])

def walk_randomly(matriz, position):
    # Cria uma lista para armazenar os ultimos 3 movimentos
    last_three_moves = []

    # Define as direcoes possiveis
    directions = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
    inverse = {"up": "down", "down": "up", "left": "right", "right": "left"}

    # Obtem o tamanho da matriz
    rows, cols = matriz.shape

    points = 0
    count = 0

    while True and count < ((m*n)**2)/2:
        valid_move = False
       
        # Verifica se a localizacao atual esta suja ou limpa
        if matriz[position[0], position[1]] == 1:
            # Se estiver suja, limpa
            matriz[position[0], position[1]] = 0
            points += 3

        while not valid_move:
            count += 1
            # Gera um movimento aleatorio
            move = random_movement()

            # Verifica se o movimento e um dos ultimos tres movimentos
            if move in last_three_moves:
                continue

            # Atualiza a posicao
            new_position = position.copy()
            new_position[0] += directions[move][0]
            new_position[1] += directions[move][1]

            # Verifica se a nova posicao esta dentro dos limites da matriz
            if 0 <= new_position[0] < rows and 0 <= new_position[1] < cols:
                points -= 1
                valid_move = True
                position = new_position
            else:
                #print(new_position)
                #print("Invalid move")
                last_three_moves.append(move)
                if len(last_three_moves) > 3:
                    last_three_moves.pop(0)  

        #print(position, move, count, points)
        #print(matriz)
        #print()

        last_three_moves.append(inverse[move])
        if len(last_three_moves) > 3:
            last_three_moves.pop(0)

    return points

# Funcao para verificar se a matriz esta suja e retornar a pontuacao correspondente
def check_dirty(matriz):
    dirt = np.count_nonzero(matriz)
    return dirt*(-20)

# Lista de quantidades de sujeira
dirt = [4, 8, 12, 16]

data = [] # Lista para armazenar os pontos
average = []  # Lista para armazenar as medias dos pontos

for d in dirt:
    print(f"Number of dirty cells: {d}\n")
    points = []
    for _ in range(10):
        m = n = 4
        matriz = fill_matriz(d, m, n)
        first = first_random_position(m, n)
        #print(first, matriz[first[0]][first[1]])
        point = walk_randomly(matriz, first)
        point += check_dirty(matriz)
        points.append(point)

    data.append(points)
    average.append(sum(points)/len(points))

    print("Points:", points)
    print("Average:", sum(points)/len(points))
    print("Max:", max(points))
    print("Min:", min(points))
    print("Standard Deviation:", round(np.std(points),2))
    print()