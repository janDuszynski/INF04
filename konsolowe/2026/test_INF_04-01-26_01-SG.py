import unittest
from kosc import Kosc


class TestKosc(unittest.TestCase):
    def test_rzut_zwraca_wartosc_z_zakresu_od_1_do_6(self):
        kosc = Kosc()
        for _ in range(1000):
            kosc.rzut()
            self.assertGreaterEqual(kosc.liczba_oczek, 1)
            self.assertLessEqual(kosc.liczba_oczek, 6)

    def test_rzut_nie_zmienia_wartosci_gdy_kosc_niedostepna(self):
        kosc = Kosc(4)
        kosc.blokuj()
        for _ in range(1000):
            kosc.rzut()
            self.assertEqual(kosc.liczba_oczek, 4)
            self.assertEqual(kosc.id_pliku, 4)


if __name__ == "__main__":
    unittest.main()
