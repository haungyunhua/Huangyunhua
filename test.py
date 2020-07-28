from SentimentSentence import sentiment_pro
import io
import time
from datetime import datetime

all_sentence = []
start = datetime.now()
with io.open('./Senta-master/data/test_data/corpus.test', "r", encoding='utf8') as fin:
    for line in fin:
        cols = line.strip().split("\t")
        label = int(cols[0])
        # context = cols[1].replace(" ","")
        # print(cols[1] +":"+str(label))
        all_sentence.append(cols[1])
res = sentiment_pro("\n".join(all_sentence))

end = datetime.now()
print('Running time: %s Seconds'%(end-start))

for data in res:
    print(data)
