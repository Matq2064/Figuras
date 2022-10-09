def float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(f'Ievades kļūda!')


def point_circle_collision(point, circle):
    x, y = point
    cx, cy, r = circle

    dist = ((x-cx)**2 + (y-cy)**2) ** 0.5

    if dist == r:
        return "Mala"
    elif dist < r:
        return "Iekšā"
    else:
        return "Ārā"


x = float_input("Ievadiet x: ")
y = float_input("Ievadiet y: ")
Circle = (0, 0, 1)

print(point_circle_collision((x, y), Circle))
