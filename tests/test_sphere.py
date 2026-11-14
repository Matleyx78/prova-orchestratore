import math
import unittest

from src.sphere import sphere_volume


class SphereVolumeTest(unittest.TestCase):
    def test_zero_radius(self) -> None:
        self.assertEqual(sphere_volume(0), 0.0)

    def test_unit_radius(self) -> None:
        self.assertAlmostEqual(sphere_volume(1), 4 / 3 * math.pi)

    def test_scales_with_cube_of_radius(self) -> None:
        self.assertAlmostEqual(sphere_volume(2), 8 * sphere_volume(1))
        self.assertAlmostEqual(sphere_volume(3), 36 * math.pi)


if __name__ == "__main__":
    unittest.main()
