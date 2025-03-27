from stats import get_num_words, get_char_counts, get_report_data


def get_book_text(file_path):
    with open(file_path, "r") as file:
        return file.read()


def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_counts = get_char_counts(text)
    report_data = get_report_data(char_counts)
    for stat in report_data:
        if not stat["char"].isalpha():
            continue
        print(f"{stat['char']}: {stat['count']}")
    print("============= END ===============")

main()