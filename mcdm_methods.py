import numpy as np
from pymcdm.methods import TOPSIS, SPOTIS, VIKOR


def calculate_bounds(decision_matrix):
    """
    Oblicza zakresy wartości (min, max) dla każdego kryterium na podstawie macierzy decyzyjnej.

    Args:
        decision_matrix (np.ndarray): Macierz decyzyjna, gdzie wiersze to alternatywy, a kolumny to kryteria.

    Returns:
        List[tuple]: Lista krotek (min, max) dla każdego kryterium.
    """
    n_criteria = decision_matrix.shape[1]
    bounds = [(np.min(decision_matrix[:, i]), np.max(decision_matrix[:, i])) for i in range(n_criteria)]
    return bounds


def topsis_method(decision_matrix, weights, types):
    """
    Oblicza wyniki analizy MCDM z wykorzystaniem metody TOPSIS.

    Args:
        decision_matrix (np.ndarray): Macierz decyzyjna.
        weights (np.ndarray): Wagi przypisane poszczególnym kryteriom.
        types (array-like): Typy kryteriów (-1 dla minimalizacji, 1 dla maksymalizacji).

    Returns:
        np.ndarray: Wyniki (oceny) dla każdej alternatywy według TOPSIS.
    """
    topsis = TOPSIS()
    scores = topsis(decision_matrix, weights, types)
    return scores


def spotis_method(decision_matrix, weights, types, bounds=None):
    """
    Oblicza wyniki analizy MCDM z wykorzystaniem metody SPOTIS.

    Args:
        decision_matrix (np.ndarray): Macierz decyzyjna.
        weights (np.ndarray): Wagi dla poszczególnych kryteriów.
        types (array-like): Typy kryteriów (-1: minimalizacja, 1: maksymalizacja).
        bounds (List[tuple], optional): Lista krotek (min, max) dla kryteriów. Jeśli nie zostanie podana,
            zakresy są obliczane na podstawie macierzy decyzyjnej.

    Returns:
        np.ndarray: Wyniki (oceny) dla alternatyw według SPOTIS.
    """
    if bounds is None:
        bounds = calculate_bounds(decision_matrix)
    spotis = SPOTIS(bounds)
    scores = spotis(decision_matrix, weights, types)
    return scores


def vikor_method(decision_matrix, weights, types):
    """
    Oblicza wyniki analizy MCDM z wykorzystaniem metody VIKOR.

    Args:
        decision_matrix (np.ndarray): Macierz decyzyjna.
        weights (np.ndarray): Wagi przypisane kryteriom.
        types (array-like): Typy kryteriów (-1: minimalizacja, 1: maksymalizacja).

    Returns:
        np.ndarray: Wyniki (oceny) dla każdej alternatywy według VIKOR.
    """
    vikor = VIKOR()
    scores = vikor(decision_matrix, weights, types)
    return scores
