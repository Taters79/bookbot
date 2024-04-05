def wordCount(text):
    words = text.split()
        
    return len(words)

def letterCount(text):
    words = text.split()
    letters = {}

    for word in words:
        lower = word.lower()
        for c in lower:
            if c in letters: letters[c] += 1
            else:
                letters[c] = 1

    return letters

def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
    
    print(f"--- Begin report of {path} ---")
    print(f"{wordCount(file_contents)} words found in the document")
    
    letter_count_dict = letterCount(file_contents)
    # convert to a list of dictionaries and then sort
    dict_list = []
    for item in letter_count_dict:
        if item.isalpha():
            temp = {'letter': item, 'num': letter_count_dict[item]}        
            dict_list.append(temp)

    dict_list.sort(reverse = True, key = lambda d: d['num'])
    for dict in dict_list:
        print(f"The '{dict['letter']}' character was found {dict['num']} times")

    print("--- End report ---")


main()