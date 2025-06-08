import unittest
import numpy as np
import pandas as pd
import matplotlib
# Używamy backendu 'Agg' do generowania wykresów bez wywoływania interfejsu graficznego.
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from utils import rank_scores, compute_spearman_correlation, plot_results, validate_decision_matrix

class TestUtils(unittest.TestCase):
    def test_rank_scores_non_reverse(self):
        """
        Test funkcji rank_scores dla przypadku, gdy wyższa wartość jest lepsza (reverse domyślnie False).
        Dla przykładowych wyników [10, 20, 30] oczekujemy uzyskania rankingu [3, 2, 1].
        """
        scores = np.array([10, 20, 30])
        expected = np.array([3, 2, 1])
        result = rank_scores(scores)
        np.testing.assert_array_equal(result, expected,
                                      err_msg="Rank scores (bez odwracania) nie działa poprawnie.")

    def test_rank_scores_reverse(self):
        """
        Test funkcji rank_scores dla przypadku, gdy niższa wartość oznacza lepszą ocenę (reverse=True).
        Dla wyników [10, 20, 30] oczekiwany ranking to [1, 2, 3].
        """
        scores = np.array([10, 20, 30])
        expected = np.array([1, 2, 3])
        result = rank_scores(scores, reverse=True)
        np.testing.assert_array_equal(result, expected,
                                      err_msg="Rank scores (z odwracaniem) nie działa poprawnie.")

    def test_compute_spearman_correlation(self):
        """
        Testuje funkcję compute_spearman_correlation.
        Dla rankingów [1, 2, 3] i [1, 3, 2] oczekiwana korelacja to około 0.5.
        """
        rank1 = [1, 2, 3]
        rank2 = [1, 3, 2]
        correlation = compute_spearman_correlation(rank1, rank2)
        self.assertAlmostEqual(correlation, 0.5, places=2,
                               msg="Korelacja Spearmana nie jest obliczana poprawnie.")

    def test_plot_results(self):
        """
        Testuje działanie funkcji plot_results, która tworzy wykres słupkowy.
        Sprawdzamy, czy funkcja wykonuje się bez zgłoszenia wyjątku.
        """
        data = {
            'Alternatywa': ['A1', 'A2', 'A3'],
            'TOPSIS': [0.5, 0.3, 0.7],
            'VIKOR': [0.6, 0.2, 0.8]
        }
        df = pd.DataFrame(data)
        try:
            plot_results(df, methods=['TOPSIS', 'VIKOR'])
            # Zamykamy okna wykresów, aby nie blokowały testów
            plt.close('all')
        except Exception as e:
            self.fail(f"Funkcja plot_results zgłasza wyjątek: {e}")

    def test_validate_decision_matrix_valid(self):
        """
        Testuje, czy funkcja validate_decision_matrix poprawnie waliduje prawidłową macierz decyzyjną.
        """
        matrix = np.array([[1, 2], [3, 4]])
        result = validate_decision_matrix(matrix)
        self.assertTrue(result, "Walidacja poprawnej macierzy decyzyjnej nie powiodła się.")

    def test_validate_decision_matrix_invalid_type(self):
        """
        Sprawdza, czy funkcja validate_decision_matrix zgłasza ValueError,
        gdy przekazany obiekt nie jest typu numpy.array.
        """
        matrix = [[1, 2], [3, 4]]  # lista, a nie numpy.array
        with self.assertRaises(ValueError, msg="Funkcja powinna zgłosić ValueError dla niepoprawnego typu"):
            validate_decision_matrix(matrix)

    def test_validate_decision_matrix_invalid_dimension(self):
        """
        Sprawdza, czy funkcja validate_decision_matrix zgłasza ValueError
        dla macierzy o niepoprawnych wymiarach (np. jednowymiarowej).
        """
        matrix = np.array([1, 2, 3])  # macierz jednowymiarowa
        with self.assertRaises(ValueError, msg="Funkcja powinna zgłosić ValueError dla macierzy o niepoprawnych wymiarach"):
            validate_decision_matrix(matrix)

if __name__ == '__main__':
    unittest.main()
