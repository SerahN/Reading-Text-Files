def read_file_content(filename):
    #reading the files
    with open(filename) as serah:
        read_file = serah.read()
        #print(read_file)
    return read_file

read_file_content("story.txt")

def count_words():
    text = read_file_content("./story.txt")
    split_text = text.split()
    #print(split_text)
    count ={}
    for i in split_text:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count
    
print(count_words())

