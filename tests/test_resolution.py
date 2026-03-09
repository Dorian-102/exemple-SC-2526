"""Description.

Tests unitaire du module resolution
"""

from exemple_sc_2526.data import ProblemeTransport, SolutionTransport
from exemple_sc_2526.resolution import resolution


def test_resolution_simple():
    """Problème simplissime."""
    probleme = ProblemeTransport(
        entrepots=[2.0],
        clients=[1.0],
        couts_unitaires=[1.0],
    )
    attendue = SolutionTransport(
        probleme=probleme,
        solution=[1.0],
    )
    calculee = resolution(probleme=probleme)
    assert calculee == attendue


def test_resolution_niveau2():
    """Problème simplissime."""
    probleme = ProblemeTransport(
        entrepots=[1.0, 1.0],
        clients=[2.0],
        couts_unitaires=[1.0, 1.0],
    )
    attendue = SolutionTransport(
        probleme=probleme,
        solution=[1.0, 1.0],
    )
    calculee = resolution(probleme=probleme)
    assert calculee == attendue


def test_resolution_niveau2_dual():
    """Problème simplissime."""
    probleme = ProblemeTransport(
        entrepots=[2.0],
        clients=[1.0, 1.0],
        couts_unitaires=[1.0, 1.0],
    )
    attendue = SolutionTransport(
        probleme=probleme,
        solution=[1.0, 1.0],
    )
    calculee = resolution(probleme=probleme)
    assert calculee == attendue


def test_resolution_niveau3():
    """Problème simplissime."""
    probleme = ProblemeTransport(
        entrepots=[1.0, 1.0],
        clients=[1.0],
        couts_unitaires=[2.0, 1.0],
    )
    attendue = SolutionTransport(
        probleme=probleme,
        solution=[0.0, 1.0],
    )
    calculee = resolution(probleme=probleme)
    assert calculee == attendue
