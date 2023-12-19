class AnagramChecker:
    def __init__(self, wordlist_file):
        self.wordlist = self.load_wordlist(wordlist_file)

    def load_wordlist(self, wordlist_file):
        try:
            with open(wordlist_file, 'r') as file:
                words = file.read().splitlines()
                return set(words)
        except FileNotFoundError:
            print("file not found")
            return set()
        
def is_valid_word(word):
