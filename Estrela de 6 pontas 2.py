import tkinter as tk
import random

def draw_star(canvas, x, y, size, color):
    """Desenha uma estrela de seis pontas no canvas."""
    # Coordenadas do triângulo apontado para cima
    up_triangle = [
        x, y - size,  # Ponta superior
        x - size, y + size // 2,  # Canto inferior esquerdo
        x + size, y + size // 2   # Canto inferior direito
    ]

    # Coordenadas do triângulo apontado para baixo
    down_triangle = [
        x, y + size,  # Ponta inferior
        x - size, y - size // 2,  # Canto superior esquerdo
        x + size, y - size // 2   # Canto superior direito
    ]

    # Desenha os dois triângulos
    canvas.create_polygon(up_triangle, fill=color, outline="black")
    canvas.create_polygon(down_triangle, fill=color, outline="black")

def create_random_stars(canvas, num_stars):
    """Cria estrelas em posições e cores aleatórias no canvas."""
    for _ in range(num_stars):
        x = random.randint(50, 450)  # Posição X aleatória
        y = random.randint(50, 450)  # Posição Y aleatória
        size = random.randint(20, 50)  # Tamanho aleatório
        color = random.choice(["red", "green", "blue", "yellow", "purple", "orange", "cyan", "magenta"])
        draw_star(canvas, x, y, size, color)

# Configuração da janela principal
window = tk.Tk()
window.title("Estrelas de Davi")

# Configuração do canvas
canvas = tk.Canvas(window, width=500, height=500, bg="white")
canvas.pack()

# Quantidade aleatória de estrelas
num_stars = random.randint(5, 15)

# Desenhar as estrelas
create_random_stars(canvas, num_stars)

# Inicia o loop principal do tkinter
window.mainloop()
