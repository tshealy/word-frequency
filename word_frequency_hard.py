import re
import sys

#file = input('What file do you want to run? ')

def clean_words():
    with open('sample.txt') as sample: #put in file_name in sample.txt spot
        file_text = sample.read()

    clean_text = re.sub(r'[^\w\s\']','', file_text).lower() #array
    clean_text = clean_text.split() #list
    return clean_text


def common_words():
    common_words = """
a,able,about,across,after,all,almost,also,am,among,an,and,any,are,as,at,be,
because,been,but,by,can,cannot,could,dear,did,do,does,either,else,ever,every,
for,from,get,got,had,has,have,he,her,hers,him,his,how,however,i,if,in,into,is,
it,its,just,least,let,like,likely,may,me,might,most,must,my,neither,no,nor,
not,of,off,often,on,only,or,other,our,own,rather,said,say,says,she,should,
since,so,some,than,that,the,their,them,then,there,these,they,this,tis,to,too,
twas,us,wants,was,we,were,what,when,where,which,while,who,whom,why,will,with,
would,yet,you,your"""
    common_words_string = ''.join(common_words.split('\n'))
    return common_words_string.split(',')

def remove_common_words():
    uncommon_words_list = []
    sorted_list = clean_words()
    common_words_list = common_words()

    for word in sorted_list:
        if word not in common_words_list:
            uncommon_words_list.append(word)
    return uncommon_words_list

def word_frequency():
    frequency_dict = {}
    uncommon_words_list = remove_common_words()
    for word in uncommon_words_list:
        if word not in frequency_dict:
            frequency_dict[word] = 1
        else:
            frequency_dict[word] += 1
    return frequency_dict



def print_hist(word_dict):
    for word, count in sorted(word_dict.items(), key=lambda x: x[1], reverse=True)[:20]:
        print(word + "#"*int(count/10))



def top_20(word_dict):

    for word, count in sorted(word_dict.items(), key=lambda x: x[1], reverse=True)[:20]:
        print(word, count)


frequency_dict = word_frequency()
top_20(frequency_dict)
print_hist(frequency_dict)
