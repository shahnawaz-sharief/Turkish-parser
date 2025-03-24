import pytest
from src.main import Noun


@pytest.fixture
def nominal_words_bare():
    return ["gül", "yer", "yan", "söz", "son", "zil", "kıl", "kuş", "köprü", "köpek"]


@pytest.fixture
def nominal_words_bare_pluralized():
    return [
        "güller",
        "yerler",
        "yanlar",
        "sözler",
        "sonlar",
        "ziller",
        "kıllar",
        "kuşlar",
        "köprüler",
        "köpekler",
    ]


@pytest.fixture
def nominal_words_as_noun_objects(nominal_words_bare):
    return [Noun(word) for word in nominal_words_bare]


def test_is_noun_base_matching(nominal_words_bare, nominal_words_as_noun_objects):
    nominal_words_as_noun_objects = [
        noun.base for noun in nominal_words_as_noun_objects
    ]
    nominal_words_bare == nominal_words_as_noun_objects


def test_is_noun_plural(nominal_words_bare_pluralized, nominal_words_as_noun_objects):
    nominal_words = [word.pluralize() for word in nominal_words_as_noun_objects]
    assert nominal_words == nominal_words_bare_pluralized
