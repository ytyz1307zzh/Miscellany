# Contents
Ciba_scratch.py: 爬取金山词霸网页进行大批量单词翻译（英译汉），需要concepts.json文件，文件内容是一个待翻译单词列表

wiki_retrieval.py: 根据TF-IDF从wiki中检索和query最相关的page或paragraph，需要dump下来的wiki database

bert_sent_embed.py: 通过计算几个样例句子的embedding similarity，比较不同预训练模型生成的sentence embedding的差异

get_wiki_text.py: 获取wiki page中的文本（正文中的``<p>``结点）

t5_question_generation.py: 在SQUAD上fine-tune过的T5 answer-aware question generation模型，以IO交互的方式给定context和answer，输出一个答案

allennlp_srl.py: 用allennlp的bert sequence role labeller对一个段落的每句话做SRL

spacy_tokenize.py: 用spacy的tokenizer将一个段落中的每句话进行tokenize，所有的token用空格分隔