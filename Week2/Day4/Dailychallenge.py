class Text:
    def __init__(self, text_str) -> None:
        self.text_str = re.sub("[^a-zA-Z0-9]"," ",text_str

    def frequency(self, word):
        list_words = self.text_str.split
        frequency = list_words.count(word)
        return f'The frequency of {word} is {frequency}'
    

    def frequency(self):
        pass
    def frequency(self):
        pass

text1 = Text("Hello this a long and long string really fun")
text1.frequency('long')
