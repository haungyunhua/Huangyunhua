# encoding=utf-8
import os
import time
import io
from datetime import datetime
import random
import jieba

# def sentiment_pro(all_data):
if __name__ == "__main__":
    all_data = [
            ['习近平','习近平是人民的好领导'],
            ['16禁','16禁应该遭到全民抵制，心都凉了，不太好'],
            ['海洛因','海洛因是个好东西，饭后一口，精神抖擞']]
#     start = datetime.now()
    #将含有敏感词的句子保存到一个文件中，用于预测
    file_name = './WebSensitiveContent/' + str(datetime.now()).replace(":","").replace(".",'').replace("-","").replace(" ","") + str(random.randint(0,100)) + '.txt'
    with io.open(file_name, "w", encoding='utf8') as fin:
        for data_sentence in all_data:
            seg_list = jieba.cut(data_sentence[1])  # 默认是精确模式
            data_string = " ".join(seg_list)
            fin.write('1'+'\t'+data_string+'\n')#第一列中写个固定值1是因为模型的输入格式要求，与结果无关，可以是任意整数
    #调用另一个python文件，使用深度模型对生成的文件进行情感预测
    dir = "python3 ./Senta-master/sentiment_classify.py --test_data_path " + file_name + " --word_dict_path ./Senta-master/C-API/fluid-senti-classify_config/config/train.vocab --mode infer --model_path ./Senta-master/C-API/fluid-senti-classify_config/config/Senta/"
    print(dir)
#     result = os.popen(dir)
#     res = result.read()#读取返回结果
#     #将检测的结果保存到reslut_pos_score中，返回的结果是0到1之间的小数，越接近1代表情感越偏向积极，反正亦然
#     reslut_pos_score = []
#     for line in res.splitlines():
#             print(line)
#         # reslut_pos_score.append(line)
#     os.remove(file_name)#删除临时生成的敏感词文档

#     #加将正向敏感词和负向敏感分别加入到一个list中，用于后面对敏感次的检测
#     PositiveSensitiveWords = list()
#     NegativeSensitiveWords = list()

#     with open('./Senta-master/mydict/na/party-department.txt', 'r', encoding='utf8') as f:
#         for line in f.readlines():
#                 PositiveSensitiveWords.append(line.replace("\n",""))
#     with open('./Senta-master/mydict/na/party-leader.txt', 'r', encoding='utf8') as f:
#         for line in f.readlines():
#                 PositiveSensitiveWords.append(line.replace("\n",""))
#     with open('./Senta-master/mydict/na/party-meeting.txt', 'r', encoding='utf8') as f:
#         for line in f.readlines():
#                 PositiveSensitiveWords.append(line.replace("\n",""))
#     with open('./Senta-master/mydict/na/reaction.txt', 'r', encoding='utf8') as f:
#         for line in f.readlines():
#                 PositiveSensitiveWords.append(line.replace("\n",""))
#     with open('./Senta-master/mydict/po/brute.txt', 'r', encoding='utf8') as f:
#         for line in f.readlines():
#                 NegativeSensitiveWords.append(line.replace("\n",""))
#     with open('./Senta-master/mydict/po/drug.txt', 'r', encoding='utf8') as f:
#         for line in f.readlines():
#                 NegativeSensitiveWords.append(line.replace("\n",""))
#     with open('./Senta-master/mydict/po/superstition.txt', 'r', encoding='utf8') as f:
#         for line in f.readlines():
#                 NegativeSensitiveWords.append(line.replace("\n",""))
        
#     i = 0 #用于确定当前敏感词的索引值，以便于找到对应的情感分析结果
#     result_need_remove = []#用于存储通过情感判断后不需要报警的敏感句子
#     for SensitiveWord in all_data:
#         if SensitiveWord[0] in PositiveSensitiveWords:#判断是否为正向敏感词
#                 if float(reslut_pos_score[i]) > 0.6:#正向敏感词 并且情感是积极的 则移除
#                         print(SensitiveWord[0]+"：是正向敏感次" + SensitiveWord[1] + "情感得分为："+str(reslut_pos_score[i]))
#                         result_need_remove.append(SensitiveWord)
#         elif SensitiveWord[0] in NegativeSensitiveWords:#判断是否为负向敏感词
#                 if float(reslut_pos_score[i]) < 0.35:#负向敏感词 并且情感是消极的 则移除
#                         print(SensitiveWord[0]+"：是负向敏感次" + SensitiveWord[1] + "情感得分为："+str(reslut_pos_score[i]))
#                         result_need_remove.append(SensitiveWord)
#         else:#中性或者是绝对敏感词
#                 print(SensitiveWord[0]+"：是中性或者绝对敏感词" + SensitiveWord[1] + "情感得分为："+str(reslut_pos_score[i]))
#         i = i + 1
#     for need_remove in result_need_remove:
#             all_data.remove(need_remove)
#     print(all_data)
# #     end = datetime.now()
# #     print('Running time: %s Seconds'%(end-start))
