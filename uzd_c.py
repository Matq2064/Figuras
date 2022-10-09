def float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(f'Ievades kļūda!')


def point_TLslitcircle_collision(point, circle):
    x, y = point
    cx, cy, r = circle

    rx = cx - x
    ry = cy - y

    dist = (rx**2 + ry**2) ** 0.5

    fx = 1 - rx
    if ry > fx or dist > r:
        return "Ārā"
    elif dist == r or ry == fx and dist <= r:
        return "Mala"
    elif dist < r:
        return "Iekšā"


x = float_input("Ievadiet x: ")
y = float_input("Ievadiet y: ")
TLSlitircle = (-2, -2, 1)

print(point_TLslitcircle_collision((x, y), TLSlitircle))
