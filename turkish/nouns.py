"""Module for Turkish Noun."""

from .vowels import TurkishVowels, Vowel


class Noun:
    """Represents a Turkish noun. It can pluralize and negate the base word."""

    def __init__(self, word: str) -> None:
        """Initalise a Noun object with a base word.

        Args:
            word (str): The base word

        """
        self.base_word = word
        self._last_vowel: Vowel | None = None
        self._turkish_vowels: TurkishVowels = TurkishVowels()

    @property
    def base(self) -> str:
        """Return the base word.

        Returns:
            str: The base word.

        """
        return self.base_word

    @property
    def last_vowel(self) -> Vowel:
        """Returns the last vowel in the base word.

        This property calculates and returns the last vowel in the base word.
        It first checks if the `_last_vowel`attribute is `None`.
        If it is, it creates a list comprehension that iterates over each character
        in the `base` word and checks if it is in the `turkish_vowels` dictionary.
        It then takes the last element of this list and assigns it to
        the `_last_vowel` attribute. Finally, it returns the `_last_vowel` attribute.

        Returns:
            Vowel: The last vowel in the base word.

        """
        if self._last_vowel is None:
            last_vowel = [v for v in self.base if v in str(self._turkish_vowels)][-1]
            self._last_vowel = self._turkish_vowels.get_vowel(vowel=last_vowel)
        return self._last_vowel

    def pluralize(self) -> str:
        """Pluralize the base word.

        Returns:
            str: The plural form of the base word.

        """
        harmonised_vowel = "".join(
            str(v)
            for v in self._turkish_vowels.get_plural_vowels()
            if self.last_vowel == v
        )

        return f"{self.base}l{harmonised_vowel}r"

    def negative(self) -> str:
        """Negate the base word.

        Returns:
            str: The negative form of the base word.

        """
        harmonised_vowel = "".join(
            str(v)
            for v in self._turkish_vowels.get_negative_vowels()
            if self.last_vowel == v
        )
        return f"{self.base}l{harmonised_vowel}r"
