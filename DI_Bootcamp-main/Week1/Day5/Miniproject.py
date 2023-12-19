#Challenge 1 

def sort_words(input_string):
    words = [word.strip() for word in input_string.split(",")]
    sorted_words = sorted(words)
    sorted_sequence =", ".join(sorted_words)

    return sorted_sequence
input_sequence = input("Enter a comma-separated sequence of words: ")

sorted_sequence = sort_words(input_sequence)
print("Sorted words:", sorted_sequence)

#Challenge 2 Longest Word


def longest_word(sentence):
    words = sentence.split()

    longest = ""
    longest_length = 0

    for word in words:
        word_length = len(word)

        if word_length > longest_length:
            longest = word
            longest_length = word_length

    return longest

print(longest_word("Margaret's toy is a pretty doll."))  


