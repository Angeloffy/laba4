from main import Line, LinearSystem
import unittest

class TestLinearSystem(unittest.TestCase):
    def test_equivalent_partitions(self):
        line1 = Line(2, 3, 4)
        line2 = Line(-4, 6, -8)
        system = LinearSystem(line1, line2)
        result = system.solve()
        self.assertEqual(result, "Прямые находятся в общем положении.\nТочка пересечения: (-2.0, 0.0)")

    def test_boundary_analysis(self):
        line1 = Line(2, 3, 4)
        line2 = Line(0, 0, 0)
        system = LinearSystem(line1, line2)
        result = system.solve()
        self.assertEqual(result, "Прямые не существуют.")

    def test_cause_effect_relationship(self):
        line1 = Line(1, 1, 2)
        line2 = Line(-2, -2, -4)
        system = LinearSystem(line1, line2)
        result = system.solve()
        self.assertEqual(result, "Прямые параллельны.")

    def test_error_assumption(self):
        line1 = Line(0, 0, 0)
        line2 = Line(0, 0, 0)
        system = LinearSystem(line1, line2)
        result = system.solve()
        self.assertEqual(result, "Прямые не существуют.")

if __name__ == "__main__":
    unittest.main()
