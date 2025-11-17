import pytest
import Tests_unitaire.projet_pour_tests_unitaire.afficher_jours_examens as afficher_jours_examens
from Q2 import *


def test_afficher_jours_examens():
    # Arrange
    date = 17/11/2025
    examen = 20/11/2025
    resultat_atrendu = "jeudi"
    # Act
    resultat = afficher_jours_examens(horaire_examen: dict) -> list[str]

    # Assert
    assert resultat_atrendu == resultat