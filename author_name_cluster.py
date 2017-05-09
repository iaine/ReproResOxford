import csv
import re
import numpy as np
from collections import defaultdict
import  matplotlib.pyplot as plt

author = defaultdict(int)
mention = defaultdict(int)

author_term = defaultdict(int)
mention_term = defaultdict(int)

raw = open("../git/Texts/TCP.csv", 'r')
reader = csv.reader(raw, delimiter=",", quotechar='"')
x = list(reader)
data = np.array(x).astype('string')

def _search_string(search_field):
    '''
      Find Martin Luther 
    '''
    #(M.*)?\s+(Luthe\w+)
    # look forwards and backwards for a pattern. 
    match = re.search('(M\w+)?(\s+)?(Luthe\w+)(\W+)?(M\w+)?', search_field, re.S)
    if match:  return match.group()


def _remove_punctuation(result_str):
    '''
       Remove trailing punctuation
    '''
    return result_str.strip().rstrip('\'\"-,.:;!?]/)')

def _count_terms(title):
    '''
       Count the individual terms in the title. 
       Returns list of terms against counts
    '''
    global allwords
    count = defaultdict(int)

    for word in title.split():
        allwords[_remove_punctuation(word).strip()] += 1
        if _remove_punctuation(word).lower().strip() not in stopwords:
            count[_remove_punctuation(word).strip()] += 1

    return count


for d in data:
    #if "Luther" in d[5]: # the brute force approach
    if _search_string(d[5]):
        name = None
        if ',' in _remove_punctuation(_search_string(d[5])):
            dt = _remove_punctuation(_search_string(d[5])).split(',')
            name = dt[1] + " " + dt[0]
        else:
            name = _remove_punctuation(_search_string(d[5]))

        #author[_remove_punctuation(_search_string(d[5]))] += 1
        #author_term[d[0]] = _count_terms(d[7])
    #if "Luther" in d[7] and "Luther" not in d[5]: # brute force approach
    #if _search_string(d[7]) and not _search_string(d[5]):
        #_tmp = _remove_punctuation(_search_string(d[7]))
        #mention[_tmp.strip()] += 1
        #print (d[5])
        #mention_term[d[0]] = _count_terms(d[7])

#print sorted(allwords.items(), key=lambda (k,v): (v,k))
#print author
#print "-------------------------"
#print mention

#zero pad the array so that they are the correct shape
#print ('Term | Count')
#aut_date = [k for k,v in author.iteritems()]
#for k,v in author.iteritems():
#    print(k + '|' + str(v))

#print ('Term | Count')
#for k,v in mention.iteritems():
#    print(k + '|' + str(v))
#men_date = [k for k,v in mention.iteritems()]

#now to plot the publications against date
#plt.figure(figsize=(16,8))
#plt.plot(dates, aut_date, 'r.', dates, men_date, 'b.')
#plt.ylabel('Number of individual titles')
#plt.xlabel('Year')
#plt.title('Publications by Martin Luther or mentioning him')
#plt.axvline(x=1546)
#plt.show()
