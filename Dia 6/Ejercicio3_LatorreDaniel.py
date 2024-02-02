def ball_collide(ball1, ball2):
    
    # Extraer coordenadas y radio de cada bola
    x1, y1, r1 = ball1
    x2, y2, r2 = ball2
    
    # Calcular la distancia entre los centros de las bolas
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    
    # Verificar si las bolas están colisionando
    if distance <= (r1 + r2):
        return True
    else:
        return False

# Ejemplo de uso
ball1 = (1, 2, 3)  # Bola 1 con centro en (1, 2) y radio 3
ball2 = (4, 5, 2)  # Bola 2 con centro en (4, 5) y radio 2
print(ball_collide(ball1, ball2))  # Output: False (las bolas no están colisionando)
