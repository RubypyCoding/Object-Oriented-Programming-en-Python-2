import unittest
from bird import Bird


class BirdTests(unittest.TestCase):

	def setUp(self):
		self.func = Bird("Billy")

	def test_name_returns_name_of_bird(self):
		self.assertEqual(self.func.name, "Billy")

	def test_jump_sends_message_when_jump(self):
		self.assertEqual(self.func.jump(), "Saltando...")

	def test_flying_when_distance_to_fly_is_Zero(self):
		self.assertEqual(self.func.flying(), 'Volando 0 mts...')

	def test_flying_when_distance_to_fly_has_increased_10_mts(self):
		self.assertEqual(self.func.flying(10), 'Volando 10 mts...')

	def test_flying_when_distance_to_fly_has_increased_20_mts(self):
		self.func.flying(10)
		self.assertEqual(self.func.flying(20), 'Volando 30 mts...')

	def test_who_am_i_sends_message_soy_un_pajaro(self):
		self.assertEqual(Bird.who_am_i(), "Soy un pájaro")


if __name__=="__main__":
    unittest.main()