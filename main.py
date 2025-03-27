def get_book_text(file_path):
    with open(file_path, "r") as file:
        return file.read()

def main():
    print(get_book_text("books/frankenstein.txt"))

main()