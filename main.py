class Line:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def is_valid(self):
        return self.A != 0 or self.B != 0

    def is_horizontal(self):
        return self.B == 0 and self.A != 0

    def is_vertical(self):
        return self.A == 0 and self.B != 0

    def slope(self):
        if self.is_vertical():
            return None
        return -self.A / self.B

class LinearSystem:
    def __init__(self, line1, line2):
        self.line1 = line1
        self.line2 = line2

    def solve(self):
        det = self.line1.A * self.line2.B - self.line1.B * self.line2.A
        det_x = self.line1.C * self.line2.B - self.line1.B * self.line2.C
        det_y = self.line1.A * self.line2.C - self.line1.C * self.line2.A

        if det != 0:
            x = -det_x / det  # Изменен знак
            y = -det_y / det  # Изменен знак
            result = "Прямые находятся в общем положении.\n"
            result += f"Точка пересечения: ({x}, {y})"
        elif self.line1.is_valid() and self.line2.is_valid():
            result = "Прямые параллельны."
        else:
            result = "Прямые не существуют."
        return result


if __name__ == "__main__":
    A1 = float(input("Введите коэффициент A первого уравнения: "))
    B1 = float(input("Введите коэффициент B первого уравнения: "))
    C1 = float(input("Введите коэффициент C первого уравнения: "))
    A2 = float(input("Введите коэффициент A второго уравнения: "))
    B2 = float(input("Введите коэффициент B второго уравнения: "))
    C2 = float(input("Введите коэффициент C второго уравнения: "))

    line1 = Line(A1, B1, C1)
    line2 = Line(A2, B2, C2)

    system = LinearSystem(line1, line2)
    system.solve()
