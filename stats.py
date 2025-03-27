def get_num_words(text):
    return len(text.split())


def get_char_counts(text):
    text = text.lower()
    char_counts = {}
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts


def get_report_data(char_counts):
    report_data = []
    for char, count in char_counts.items():
        report_data.append({"char": char, "count": count})
    report_data.sort(key=lambda d: d["count"], reverse=True)
    return report_data

def test_get_report_data():
    sample_data = {"a": 3, "b": 1, "c": 4}
    expected_report = [
        {"char": "c", "count": 4},
        {"char": "a", "count": 3},
        {"char": "b", "count": 1}]
    assert get_report_data(sample_data) == expected_report
