import unittest
import numpy as np
from mcdm_methods import calculate_bounds, topsis_method, spotis_method, vikor_method


class TestMCDMMethods(unittest.TestCase):
    def setUp(self):
        """
        Przygotowanie przykładowej macierzy decyzyjnej, wag, typów kryteriów oraz oczekiwanych zakresów.
        """
        # Przykładowa macierz: wiersze – alternatywy, kolumny – kryteria
        self.decision_matrix = np.array([
            [500, 2000, 3],
            [680, 2300, 4],
            [600, 2200, 2]
        ])
        # Wagi dla kryteriów (np. 30%, 50%, 20%)
        self.weights = np.array([0.3, 0.5, 0.2])
        # Typy kryteriów: -1 = minimalizacja, 1 = maksymalizacja
        self.types = np.array([-1, 1, -1])
        # Oczekiwane zakresy (min, max) dla każdego kryterium
        self.bounds = [
            (np.min(self.decision_matrix[:, 0]), np.max(self.decision_matrix[:, 0])),
            (np.min(self.decision_matrix[:, 1]), np.max(self.decision_matrix[:, 1])),
            (np.min(self.decision_matrix[:, 2]), np.max(self.decision_matrix[:, 2]))
        ]

    def test_calculate_bounds(self):
        """
        Testuje funkcję calculate_bounds: sprawdza, czy obliczone zakresy zgadzają się z oczekiwanymi.
        """
        calculated_bounds = calculate_bounds(self.decision_matrix)
        # Testujemy równość listy krotek
        self.assertEqual(calculated_bounds, self.bounds, "Obliczone zakresy nie są zgodne z oczekiwanymi.")

    def test_topsis_method(self):
        """
        Przetestowanie metody TOPSIS: wynik powinien być tablicą numpy o rozmiarze równym liczbie alternatyw.
        """
        scores = topsis_method(self.decision_matrix, self.weights, self.types)
        self.assertIsInstance(scores, np.ndarray, "Wynik TOPSIS nie jest typu numpy.ndarray.")
        self.assertEqual(scores.shape[0], self.decision_matrix.shape[0],
                         "Liczba wyników TOPSIS nie odpowiada liczbie alternatyw.")

    def test_spotis_method(self):
        """
        Przetestowanie metody SPOTIS: wynik powinien być tablicą numpy o rozmiarze równym liczbie alternatyw.
        """
        scores = spotis_method(self.decision_matrix, self.weights, self.types, self.bounds)
        self.assertIsInstance(scores, np.ndarray, "Wynik SPOTIS nie jest typu numpy.ndarray.")
        self.assertEqual(scores.shape[0], self.decision_matrix.shape[0],
                         "Liczba wyników SPOTIS nie odpowiada liczbie alternatyw.")

    def test_vikor_method(self):
        """
        Przetestowanie metody VIKOR: wynik powinien być tablicą numpy o rozmiarze równym liczbie alternatyw.
        """
        scores = vikor_method(self.decision_matrix, self.weights, self.types)
        self.assertIsInstance(scores, np.ndarray, "Wynik VIKOR nie jest typu numpy.ndarray.")
        self.assertEqual(scores.shape[0], self.decision_matrix.shape[0],
                         "Liczba wyników VIKOR nie odpowiada liczbie alternatyw.")


if __name__ == '__main__':
    unittest.main()
