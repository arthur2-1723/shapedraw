def draw_rectangle(width, height):
    """Desenha um retângulo com largura e altura especificadas."""
    for _ in range(height):
        print('*' * width)

def draw_triangle(size):
    """Desenha um triângulo equilátero com o tamanho especificado."""
    for i in range(size):
        print(' ' * (size - i - 1) + '*' * (2 * i + 1))

def draw_circle(radius):
    """Desenha um círculo aproximado usando caracteres ASCII."""
    for i in range((2 * radius) + 1):
        for j in range((2 * radius) + 1):
            distance = ((i - radius) ** 2 + (j - radius) ** 2) ** 0.5
            if distance < radius + 0.5:
                print('*', end='')
            else:
                print(' ', end='')
        print()