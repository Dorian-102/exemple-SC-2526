"""Description.

Tests unitaires du module data
"""

import pytest
from pydantic import ValidationError
from exemple_sc_2526.data import ProblemeTransport, SolutionTransport


def test_verifications_probleme_transport_entrepots():
    with pytest.raises(ValidationError):
        ProblemeTransport(entrepots=[], clients=[1.0], couts_unitaires=[1.0])


def test_verifications_probleme_transport_clients():
    with pytest.raises(ValidationError):
        ProblemeTransport(entrepots=[1.0], clients=[], couts_unitaires=[1.0])


def test_verifications_probleme_transport_couts():
    with pytest.raises(ValidationError):
        ProblemeTransport(entrepots=[1.0, 2.0], clients=[1.0], couts_unitaires=[1.0])


def test_verifications_probleme_transport_quantites():
    with pytest.raises(ValidationError):
        ProblemeTransport(entrepots=[1.0], clients=[2.0], couts_unitaires=[1.0])
