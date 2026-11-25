import pandas as pd

from pipeline import (
    agreger_par_categorie,
    agreger_par_ville,
    transformer,
)


def donnees_exemple():
    return pd.DataFrame({
        "quantite": [2, 2, None, -1, 3],
        "prix_unitaire": [10.0, 10.0, 5.0, 5.0, 20.0],
        "ville": ["paris", "paris", "Lyon", "Lyon", " lyon"],
    })


def test_supprime_les_doublons_et_lignes_invalides():
    resultat = transformer(donnees_exemple())
    assert len(resultat) == 2


def test_normalise_les_villes():
    resultat = transformer(donnees_exemple())
    assert sorted(resultat["ville"]) == ["Lyon", "Paris"]


def test_calcule_le_montant():
    resultat = transformer(donnees_exemple())
    assert resultat["montant"].sum() == 80.0
#   Voir test echouer
#   assert resultat["montant"].sum() == 90.0


def test_agregation_par_ville():
    resultat = agreger_par_ville(transformer(donnees_exemple()))
    assert resultat.iloc[0]["ville"] == "Lyon"
    assert resultat.iloc[0]["montant"] == 60.0


def test_agregation_par_categorie():
    donnees = pd.DataFrame({
        "categorie": ["Informatique", "Mobilier", "Informatique"],
        "montant": [20.0, 60.0, 10.0],
    })

    resultat = agreger_par_categorie(donnees)

    assert resultat.iloc[0]["categorie"] == "Mobilier"
    assert resultat.iloc[0]["montant"] == 60.0
    assert resultat.iloc[1]["categorie"] == "Informatique"
    assert resultat.iloc[1]["montant"] == 30.0