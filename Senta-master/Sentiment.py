import os
import time
import io
from datetime import datetime
import random
import jieba
# import sentiment_classify


if __name__ == "__main__":
        all_data = [
                ['习近平','习近平是人民的好领导'],
                ['台湾独立','支持台湾独立会受到人民的谴责，害国害民'],
                ['冰毒','病毒是个害人害己，应该全名抵制'],
                ['海洛因','海洛因是个好东西，饭后一口，精神抖擞']]
        basedir = os.path.abspath(os.path.dirname(__file__))
        file_name = basedir + '\\WebSensitiveContent\\' + str(datetime.now()).replace(":","").replace(".",'').replace("-","").replace(" ","") + str(random.randint(0,100)) + '.txt'
        with io.open(file_name, "w", encoding='utf8') as fin:
                for data_sentence in all_data:
                        seg_list = jieba.cut(data_sentence[1])  # 默认是精确模式
                        data_string = " ".join(seg_list)
                        fin.write(data_sentence[0]+'\t'+data_string+'\n')        
        # dir = "python sentiment_classify.py --test_data_path " + file_name + " --word_dict_path ./C-API/fluid-senti-classify_config/config/train.vocab --mode infer --model_path ./C-API/fluid-senti-classify_config/config/Senta/"
        # start = datetime.now()
        # result = os.popen(dir)
        # res = result.read()
        # end = datetime.now()
        # print('Running time: %s Seconds'%(end-start))
        # for line in res.splitlines():
        #         print(line)