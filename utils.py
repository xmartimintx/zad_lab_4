import numpy as np
import pandas as pd
from scipy.stats import spearmanr
import matplotlib.pyplot as plt

#Przyjmuje tablicę wyników oraz parametr reverse, który pozwala obsłużyć metody, w których mniejsza wartość oznacza lepszy wynik (np. SPOTIS, VIKOR). Funkcja przetwarza wyniki na ranking alternatyw.
def rank_scores(scores, reverse=False):
    """
    Konwertuje zestaw ocen alternatyw na ranking, w którym najlepsza ocena ma numer 1.

    Parametry:
      scores (np.ndarray): Tablica z wynikami oceny alternatyw.
      reverse (bool): Jeśli True, to mniejsza wartość oznacza lepszą ocenę (ranking odwrotny).
                       Domyślnie False (przyjmujemy, że wyższa ocena jest lepsza).

    Zwraca:
      np.ndarray: Tablica rankingów dla poszczególnych alternatyw.
    """
    # Przy wyższym wyniku lepsza alternatywa, odwracamy porządek, jeśli nie chcemy ranking odwrotny.
    order = scores if reverse else -scores
    return np.argsort(np.argsort(order)) + 1

#Umożliwia szybkie obliczenie korelacji Spearmana między dwoma rankingami, co jest przydatne przy porównywaniu różnych metod MCDM.
def compute_spearman_correlation(rank1, rank2):
    """
    Oblicza współczynnik korelacji rang Spearmana pomiędzy dwoma rankingami.

    Parametry:
      rank1 (array-like): Ranking alternatyw dla metody pierwszej.
      rank2 (array-like): Ranking alternatyw dla metody drugiej.

    Zwraca:
      float: Wartość współczynnika korelacji Spearmana.
    """
    correlation = spearmanr(rank1, rank2).correlation
    return correlation

#Do wizualizacji wyników stworzono funkcję, która generuje wykres słupkowy na podstawie DataFrame zawierającego wyniki danej metody. Dzięki temu łatwiej porównać oceny alternatyw.
def plot_results(df, methods, alternative_col='Alternatywa', figsize=(10, 6)):
    """
    Tworzy wykres słupkowy porównujący oceny alternatyw uzyskane w różnych metodach MCDM.

    Parametry:
      df (pd.DataFrame): DataFrame zawierający kolumnę z nazwami alternatyw oraz kolumny z ocenami.
      methods (list): Lista nazw kolumn (metod MCDM) do wizualizacji.
      alternative_col (str): Nazwa kolumny w df zawierającej nazwy alternatyw.
      figsize (tuple): Rozmiar wykresu.

    Nie zwraca żadnej wartości, jedynie wyświetla wykres.
    """
    labels = df[alternative_col]
    x = np.arange(len(labels))
    bar_width = 0.8 / len(methods)  # szerokość słupka w zależności od liczby metod

    fig, ax = plt.subplots(figsize=figsize)

    for idx, method in enumerate(methods):
        # Przesunięcie słupków aby nie nachodziły na siebie
        ax.bar(x + idx * bar_width - (bar_width * (len(methods) - 1) / 2),
               df[method],
               bar_width,
               label=method)

    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel('Ocena')
    ax.set_title('Porównanie ocen alternatyw metod MCDM')
    ax.legend()
    plt.tight_layout()
    plt.show()

#Funkcja zapewnia, że podana macierz decyzyjna jest poprawnego formatu, co pozwala uniknąć błędów już na etapie wejścia do obliczeń.
def validate_decision_matrix(decision_matrix):
    """
    Prosta walidacja macierzy decyzyjnej. Sprawdza, czy:
      - Jest to obiekt typu numpy.array.
      - Ma dwa wymiary.
      - Zawiera co najmniej jeden wiersz i jedną kolumnę.

    Parametry:
      decision_matrix (np.ndarray): Macierz decyzyjna.

    Zwraca:
      bool: True, jeśli walidacja przebiega pomyślnie.

    Podnosi:
      ValueError: Jeśli macierz nie spełnia wymagań.
    """
    if not isinstance(decision_matrix, np.ndarray):
        raise ValueError("Macierz decyzyjna musi być typu numpy.array.")
    if decision_matrix.ndim != 2:
        raise ValueError("Macierz decyzyjna musi być dwuwymiarowa.")
    if decision_matrix.shape[0] < 1 or decision_matrix.shape[1] < 1:
        raise ValueError("Macierz decyzyjna musi zawierać co najmniej jeden wiersz i jedną kolumnę.")
    return True
