from turkish.nouns import Noun

if __name__ == "__main__":
    turkish_words = [
        "gül",
        "yer",
        "yan",
        "söz",
        "son",
        "zil",
        "kıl",
        "kuş",
        "köprü",
        "köpek",
    ]
    turkish_nouns = [Noun(word) for word in turkish_words]
    plural_nouns = [noun.pluralize() for noun in turkish_nouns]
    print(plural_nouns)
