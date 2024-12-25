def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        print(count_words(words))

def count_words(book):
    word_counter = 0
    for character in book:
        word_counter += 1
    return word_counter
    
main()