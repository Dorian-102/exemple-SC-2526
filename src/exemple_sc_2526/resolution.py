"""Description.

Implémentation de la résolution d'un problème de transport.
"""

from scipy import optimize
import numpy as np
from .data import ProblemeTransport, SolutionTransport


def construction_matrices(
    probleme: ProblemeTransport,
) -> tuple[np.typing.ArrayLike, np.typing.ArrayLike]:
    """Construction des matrices de contraintes de la programmation linéaire."""
    n, m = len(probleme.entrepots), len(probleme.clients)
    return np.fromfunction(
        lambda i, k: 1.0 if (1 <= (k - (i - 1) * m) <= m) else 0.0, shape=(m, m * n)
    ), np.fromfunction(
        lambda j, k: 1.0 if 1 <= (1 + (k - j) // m) <= n else 0.0, shape=(n, n * m)
    )


def resolution(probleme: ProblemeTransport) -> SolutionTransport:
    c = np.array(probleme.couts_unitaires)
    beq = np.array(probleme.clients)
    bub = np.array(probleme.entrepots)
    Aeq, Aub = construction_matrices(probleme=probleme)
    solution_abstraite = optimize.linprog(
        c=c, A_eq=Aeq, b_eq=beq, A_ub=Aub, b_ub=bub, bounds=(0, None)
    )
    return SolutionTransport(
        probleme=probleme,
        solution=solution_abstraite.x,
    )
