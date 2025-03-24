"""Module for Turkish vowels and their properties."""

from collections.abc import Iterator
from enum import Enum
from typing import Literal

from pydantic import BaseModel, Field  # type: ignore

TurkishVowelLiterals = Literal["a", "e", "ü", "o", "u", "ı", "ö", "i"]


class TonguePosition(str, Enum):
    """Represents the position of the tongue."""

    FRONT = "front"
    BACK = "BACK"


class PitchLevel(str, Enum):
    """Represents the pitch level of the vowel."""

    HIGH = "high"
    LOW = "low"


class Roundness(str, Enum):
    """Represents the roundness of the vowel."""

    ROUNDED = "rounded"
    UNROUNDED = "unrounded"


class VowelProperty(BaseModel):
    """Represents the properties of a Turkish vowel."""

    tongue_position: TonguePosition = Field(
        description="Position of the tongue (front/back)",
    )
    pitch_level: PitchLevel = Field(description="Vowel height (high/low)")
    roundness: Roundness = Field(description="Lip rounding (rounded/unrounded)")


class Vowel(BaseModel):
    """Represents a Turkish vowel."""

    char: TurkishVowelLiterals = Field(
        description="The Turkish vowel. The literal character",
    )
    property: VowelProperty = Field(description="The properties of the Turkish vowel")

    def __eq__(self, other: object) -> bool:
        """Check if two vowels are equal based on their properties."""
        if not isinstance(other, Vowel):
            raise TypeError("Cannot compare Vowel with non-Vowel object")
        return Vowel.can_harmonize(self, other)

    def __repr__(self) -> str:
        return f"Vowel(char={self.char}, property={self.property})"

    def __str__(self):
        return self.char

    @staticmethod
    def can_harmonize(previous: "Vowel", forward: "Vowel") -> bool:
        """Determine if two turkish vowels can harmonize.

        Args:
            previous (str): The previous vowel in the same word
            forward (str): The next vowe appear after the previous vowel

        Returns:
            (bool): True if they can harmonise

        """
        previous_vowel = previous.property
        forward_vowel = forward.property

        # Rule 1: Must have the same tongue position (front/back)
        if previous_vowel.tongue_position != forward_vowel.tongue_position:
            return False

        # Rule 2: If the forward vowel is high, the previous vowel must
        # have the same roundness
        if (
            forward_vowel.pitch_level == PitchLevel.HIGH
            and previous_vowel.roundness == forward_vowel.roundness
        ):
            return True

        # Rule 3: If the forward vowel is low, it must be unrounded
        return (
            forward_vowel.pitch_level == PitchLevel.LOW
            and forward_vowel.roundness == Roundness.UNROUNDED
        )


class TurkishVowels:
    """Represents the Turkish vowels and their properties."""

    vowels: tuple = (
        Vowel(
            char="a",
            property=VowelProperty(
                tongue_position=TonguePosition.BACK,
                pitch_level=PitchLevel.LOW,
                roundness=Roundness.UNROUNDED,
            ),
        ),
        Vowel(
            char="e",
            property=VowelProperty(
                tongue_position=TonguePosition.FRONT,
                pitch_level=PitchLevel.LOW,
                roundness=Roundness.UNROUNDED,
            ),
        ),
        Vowel(
            char="ü",
            property=VowelProperty(
                tongue_position=TonguePosition.FRONT,
                pitch_level=PitchLevel.HIGH,
                roundness=Roundness.ROUNDED,
            ),
        ),
        Vowel(
            char="o",
            property=VowelProperty(
                tongue_position=TonguePosition.BACK,
                pitch_level=PitchLevel.LOW,
                roundness=Roundness.ROUNDED,
            ),
        ),
        Vowel(
            char="u",
            property=VowelProperty(
                tongue_position=TonguePosition.BACK,
                pitch_level=PitchLevel.HIGH,
                roundness=Roundness.ROUNDED,
            ),
        ),
        Vowel(
            char="ı",
            property=VowelProperty(
                tongue_position=TonguePosition.BACK,
                pitch_level=PitchLevel.HIGH,
                roundness=Roundness.UNROUNDED,
            ),
        ),
        Vowel(
            char="ö",
            property=VowelProperty(
                tongue_position=TonguePosition.FRONT,
                pitch_level=PitchLevel.LOW,
                roundness=Roundness.ROUNDED,
            ),
        ),
        Vowel(
            char="i",
            property=VowelProperty(
                tongue_position=TonguePosition.FRONT,
                pitch_level=PitchLevel.HIGH,
                roundness=Roundness.UNROUNDED,
            ),
        ),
    )

    def __iter__(self) -> Iterator[list[Vowel]]:
        return iter(self.vowels)

    def __len__(self) -> int:
        return len(self.vowels)

    def __getitem__(self, item: Vowel) -> Vowel:
        if not isinstance(item, Vowel):
            raise TypeError(f"{item} should be of type Vowel")
        for v in self.vowels:
            if v.char == item:
                return v
        raise ValueError(f"{item} is not a valid Turkish vowel")

    def __contains__(self, item: Vowel) -> bool:
        if not isinstance(item, Vowel):
            raise TypeError(f"{item} should be of Type Vowel")
        return item in self.vowels

    def __str__(self) -> str:
        """Returns all the turkish vowels as chars"""
        return "".join(v.char for v in self.vowels)

    @classmethod
    def get_plural_vowels(cls) -> tuple[Vowel, Vowel]:
        """Return two plural vowels.

        Returns:
            tuple[Vowel, Vowel]: Two plural vowels "a" and "e"

        """
        return cls.get_vowel("a"), cls.get_vowel("e")

    @classmethod
    def get_negative_vowels(cls) -> tuple[Vowel, Vowel, Vowel, Vowel]:
        """Return four negative vowels.

        Returns:
            tuple[Vowel, Vowel, Vowel, Vowel]: Four negative vowels

        """
        return (
            cls.get_vowel("ı"),
            cls.get_vowel("i"),
            cls.get_vowel("u"),
            cls.get_vowel("ü"),
        )

    @classmethod
    def get_vowel(cls, vowel: str) -> Vowel:
        """Return the properties of a Turkish vowel.

        Args:
            vowel (str): The Turkish vowel.

        Returns:
            VowelProperty: The properties of the Turkish vowel.

        Raises:
            ValueError: If the vowel is not a valid Turkish

        """
        for v in cls.vowels:
            if v.char == vowel:
                return v
        raise ValueError(f"{vowel} is not a valid Turkish vowel")
