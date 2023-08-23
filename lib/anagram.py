class Anagram:
    def __init__(self, word):
        self.word = word
        self.letters_in_word = sorted([letter for letter in word])

    def match(self, list):
        anagrams_detected = []

        for word in list:
            if sorted([letter for letter in word]) == self.letters_in_word:
                anagrams_detected.append(word)

        return anagrams_detected
