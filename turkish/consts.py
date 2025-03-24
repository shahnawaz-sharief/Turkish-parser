"""Module for Turkish language constants."""

from enum import Enum


class PartsOfSpeech(str, Enum):
    """Represents the part of speech of a word."""

    NOUN = "Noun"
    VERB = "Verb"
    ADVERB = "Adverb"
    ADJECTIVE = "Adjective"
    PREPOSITION = "Preposition"


class NounCase(str, Enum):
    """Represents the case of a noun."""

    NOMINATIVE = "Nominative"
    ACCUSATIVE = "Accusative"
    DATIVE = "Dative"
    LOCATIVE = "Locative"
    ABLATIVE = "Ablative"
    GENITIVE = "Genitive"


class NounPlurality(str, Enum):
    """Represents the plurality of a noun."""

    SINGULAR = "Singular"
    PLURAL = "Plural"


class NounDefiniteness(str, Enum):
    """Represents the definiteness of a noun."""

    DEFINITE = "Definite"
    INDEFINITE = "Indefinite"


class VerbConjugation(str, Enum):
    """Represents the conjugation of a verb."""

    INFINITIVE = "Infinitive"
    PRESENT = "Present"
    PAST = "Past"
    FUTURE = "Future"
    IMPERATIVE = "Imperative"
