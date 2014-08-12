import string
import re
from collections import Counter

def level_0():
    return 2**38

def level_1(encry_str, offset=2):
    leet = string.maketrans(string.ascii_lowercase, string.ascii_lowercase[offset:] + string.ascii_lowercase[:offset])
    return encry_str.translate(leet)

def level_2(input_file):
    '''get the least number of characters, get the answer: equality.html'''
    fd = open(input_file)
    lines = fd.readlines();
    fd.close()
    # counter each character's frequency
    counter = Counter(''.join(lines))

    # the following is another method, just notice that there are alpha and non-alpha
    filter(lambda x: x in string.letters, ''.join(lines))

def level_3(input_file):
    fd = open(input_file)
    lines = fd.readlines();
    fd.close()
    text = ''.join(lines)
    print ''.join(x[4:5] for x in re.findall("[^A-Z][A-Z]{3}[a-z]{1}[A-Z]{3}[^A-Z]", text))

def level_4():
    import urllib
    query_args = {"nothing":63579}
    for x in xrange(1,410):
        encoded_args = urllib.urlencode(query_args)
        url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?' + encoded_args
        response = urllib.urlopen(url).read()
        print response
        match = re.search("[0-9]+",response)
        if match:
            query_args["nothing"] = response[match.start():match.end()]

    return "peak.html"

def level_5(input_file):
    import cPickle as pickle
    with open(input_file) as in_s:
        obj = pickle.load(in_s)
    for item in obj:
        for it in item:
            print it[0] * it[1],
        print

def level_6():

    import zipfile
    nextFile = "90052"
    with zipfile.ZipFile('C:/Users/Administrator/Downloads/channel.zip') as zf:
        comments = []
        while nextFile:
            comments.append(zf.getinfo(nextFile+'.txt').comment)
            line = zf.read(nextFile+".txt")
            match = re.search("[0-9]+",line)
            nextFile = line[match.start():match.end()] if match else ""

    print ''.join(comments)


def level_8():
    import bz2
    # un: 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
    # pw: 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
    def inflate(data):
        inflated = bz2.decompress(data)
        return inflated
    print inflate('BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')
    print inflate('BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')

def level_9():
    def count(index, num):
        cnt = 1
        while index < len(num) and num[index] == num[index+1]:
            cnt += 1
            index += 1
        return (index+1, str(cnt)+num[index])

    a = ["1"]
    next="1"
    while len(a) < 31:
        current = next
        index = 0
        next = ""
        while index < len(current):
            index, part = count(index, current+"a")
            next += part
        a.append(next)
        current = next
    print len(a[30])
        

if __name__ == '__main__':
    pass