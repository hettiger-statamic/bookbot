def get_book_text(file_path):
    with open(file_path, "r") as file:
        return file.read()

def num_words(text):
    return len(text.split())

def main():
    text = get_book_text("books/frankenstein.txt")
    print(f"{num_words(text)} words found in the document")

main()