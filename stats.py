def count_words(text):
    word=text.split()
    return len(word)

def num_words(text):
    dict={}
    for i in text.lower():
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    return dict

def sort_on(d):
    return d["num"]

def char_dict_to_sorted_list(num_char_dict):
    sortedlist=[]
    for ch in num_char_dict:
        sortedlist.append({"char":ch,"num":num_char_dict[ch]})
    sortedlist.sort(reverse=True,key=sort_on)
    return sortedlist