def float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(f'Ievades kļūda!')


def point_BLtriangle_collision(point, triangle):
    x, y = point
    rx1, ry1, rx2, ry2 = triangle

    in_x = not (x < rx1 or x > rx2)
    in_y = not (y < ry2 or y > ry1)

    if x == rx1 and in_y:
        return "Mala"
    elif y == ry2 and in_x:
        return "Mala"
    else:
        if in_x and in_y:
            w = rx2 - rx1
            h = ry1 - ry2
            ratio = -h / w
            fx = h + ratio * x
            if y == fx:
                return "Mala"
            elif y < fx:
                return "Iekšā"
            else:
                return "Ārā"
        else:
            return "Ārā"


x = float_input("Ievadiet x: ")
y = float_input("Ievadiet y: ")
BLTriangle = (0, 3, 2, 0)

print(point_BLtriangle_collision((x, y), BLTriangle))
