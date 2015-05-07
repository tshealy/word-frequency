import re


with open('sample.txt') as sample:
    file_text = sample.read()

def word_frequency():
    clean_text = re.sub(r'[^\w\s\']','', file_text).lower() #array
    clean_text = clean_text.split() #list

    frequency_dict = {}

    for word in clean_text:
        if word not in frequency_dict:
            frequency_dict[word] = 1
        else:
            frequency_dict[word] += 1

    for word, count in sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)[:20]:
        print(word, count)


word_frequency()
