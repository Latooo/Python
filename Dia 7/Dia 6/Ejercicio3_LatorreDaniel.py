import math
def Colision(bola1, bola2):
    x1, y1, r1 = bola1
    x2, y2, r2 = bola2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance <= r1 + r2

bola1 = (0,0,5)
bola2 = (8,0,3)

print(Colision(bola1, bola2))

#3D

def Colision(bola1, bola2):
    x1, y1, z1, r1 = bola1
    x2, y2, z2, r2 = bola2
    distance_euclides = math.sqrt((x2 - x1)**2 + (y2 - y1)) + (z2 - z1)**2
    print(distance_euclides)
    return distance_euclides <= r1 + r2