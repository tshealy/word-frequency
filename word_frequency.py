import re
with open('sample.txt') as sample:
    file_text = sample.readlines()

def word_frequency():
    clean_text = re.sub(r'[^A-Za-z]','\n', (' '.join(file_text)).lower())
    text_ready = clean_text.split()
    frequency_dict = {}

    for word in text_ready:
        if word not in frequency_dict:
            frequency_dict[word] = 1
        else:
            frequency_dict[word] += 1

    for word, count in sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)[:20]:
        print(word, count)
word_frequency()
