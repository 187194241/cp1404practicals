"""
Word Occurrences
Estimate: 20 minutes
Actual:   26 minutes
"""
def main():
    text = input("Text: ").lower()
    word_counts = {}
    words = text.split()
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    sorted_words = sorted(word_counts.keys())
    for word in word_counts:
        thing, width, other_thing = "first", 13, "second"
        print(f"{word:{width}} : {word_counts[word]}")
main()