# Huangyunhua
基于ELMo的敏感信息检测
一、在线安装
	在线安装直接使用pip install paddlepaddle即可。
二、离线安装（Linux）
	离线安装采用的思路是将PaddlePaddle的安装包和需要的第三方依赖包在有网的环境提前下载好，再进行离线安装。
	离线安装的安装包存放在download2环境中，安装时将download文件考试所需安装的主机后，运行一下命令：
python3 -m pip install --no-index --find-links=路径 paddlepaddle
	路径值得是download2文件所在路径，比如该文件放在/usr/packages/下，路径应写为：
python3 -m pip install --no-index --find-links=/usr/packages/download2/ paddlepaddle
	注：若安装过程中出现某个依赖包显示某个依赖包未找到相应版本，则使用“python3 -m pip download 依赖包名称”在联网情况下下载该依赖包放入download2文件后再安装，出现该问题的原因是不同环境需要的依赖包版本不一样，目前download只下载了当时所测主机的所需安装包。
三、环境安装检验
	输入以下代码进行检验：如下图所示，显示Your Paddle Fluid is installed successfully! Let's start deep Learning with Paddle Fluid now，则说明PaddlePaddle环境已经安装成功。
python3
import paddle.fluid as fluid
fluid.install_check.run_check()

一、代码结构	
├── sentiment.py  # 情感倾向分析主函数，包括训练、预估、预测部分
├── nets.py   # 本例中涉及的各种网络结构均定义在此文件中
├── utils.py   # 定义通用的函数，例如加载词典，读入数据等
├── C-API   #模型预测C-API接口
二、简介
	情感倾向分析针对带有主观描述的中文文本，可自动判断该文本的情感极性类别并给出相应的置信度。情感类型分为积极、消极、中性。
三、模型概览
nets.py 中包含一下模型：
bow_net：Bow(Bag Of Words)模型，是一个非序列模型。使用基本的全连接结构。
cnn_net：浅层CNN模型，是一个基础的序列模型，能够处理变长的序列输入，提取一个局部区域之内的特征。
gru_net：单层GRU模型，序列模型，能够较好地解序列文本中长距离依赖的问题。
lstm_net：单层LSTM模型，序列模型，能够较好地解决序列文本中长距离依赖的问题。
bilstm_net：双向单层LSTM模型，序列模型，通过采用双向lstm结构，更好地捕获句子中的语义特征。AI平台上情感倾向分析模块采用此模型进行训练和预测。
四、数据准备
数据格式：每一行为一条样本，以`\t`分隔，第一列是类别标签，第二列是输入文本的内容，文本内容中的词语以空格间隔。以下是两条示例数据：

2   特 喜欢 这种 好看的 狗狗
2   这 真是 惊艳 世界 的 中国 黑科技
0	环境 特别 差 ，脏兮兮 的 ，再也 不去 了
代码中采用jieba对句子进行分词处理后，再作为模型的输入。
五、模型训练与预测
1.模型训练
python sentiment_classify.py \
--train_data_path ./data/train_data/corpus.train \ # 训练数据路径
--word_dict_path ./data/train.vocab \  # 词典路径
--mode train \ # train模式
--model_path ./models # 模型保存路径
2.模型评价
python sentiment_classify.py \
--test_data_path ./data/test_data/corpus.test \# 测试数据路径
--word_dict_path ./data/train.vocab \ # 词典路径
--mode eval \ # eval模式
--model_path ./models/epoch0/# 预测模型路径
3.模型预测
python sentiment_classify.py \
--test_data_path ./data/test_data/corpus.test \# 测试数据路径
 --word_dict_path ./data/train.vocab \ # 词典路径
--mode infer \ # infer模式
--model_path ./models/epoch0/# 预测模型路径

 
