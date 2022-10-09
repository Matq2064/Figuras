def float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(f'Ievades kļūda!')


def point_rect_collision(point, rect):
    x, y = point
    rx1, ry1, rx2, ry2 = rect

    in_x = not (x < rx1 or x > rx2)
    in_y = not (y < ry2 or y > ry1)

    if (x == rx1 or x == rx2) and in_y or (y == ry1 or y == ry2) and in_x:
        return "Mala"
    elif in_x and in_y:
        return "Iekšā"
    else:
        return "Ārā"


x = float_input("Ievadiet x: ")
y = float_input("Ievadiet y: ")
Rect = (-1, 1, 3, -3)

print(point_rect_collision((x, y), Rect))
