def count_letters(text):
    text = text.lower()
    text_dict = {}
    for l in text:
        if l in text_dict:
            text_dict[l] += 1
        else:
            text_dict[l] = 1
    return text_dict

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.split()
    total_words = 0
    for word in words:
        total_words +=1
    print(f"{total_words} words found in the document")
    file_dict = count_letters(file_contents)
    for key, value in file_dict.items():
        print(f"The '{key}' character was found {value} time")

