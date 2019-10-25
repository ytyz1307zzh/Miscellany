import requests
from bs4 import BeautifulSoup
import re
import json
import os
from tqdm import tqdm
import traceback

concepts = json.load(open('concepts.json','r',encoding='utf-8'))

if os.path.exists('concept_translate_backup.json'):
    trans_res = json.load(open('concept_translate_backup.json','r',encoding='utf-8'))
else:
    trans_res = {}

word_cnt=0
for word in tqdm(concepts):

    if word_cnt % 1000 == 0 and word_cnt>0:
        print('[INFO] saving json file...')
        json.dump(trans_res, open('concept_translate_backup.json', 'w', encoding='utf-8'), indent=4, ensure_ascii=False)

    if word in trans_res:
        if len(trans_res[word])>0:
            word_cnt+=1
        continue

    try:
        r=requests.get('http://www.iciba.com/{}'.format(word),allow_redirects=False)
    except:
        json.dump(trans_res, open('concept_translate_backup.json', 'w', encoding='utf-8'), indent=4, ensure_ascii=False)
        print('[ERROR] Internet error while scratching from iciba.com')
        print('[INFO] saving json file...')
        traceback.print_exc()
        quit()

    content=r.text
    soup=BeautifulSoup(content,'lxml')

    if re.search(r'301',str(soup.find('h1'))):
        print('[ERROR]301 Moved Permanently')
        print('[INFO] saving json file...')
        json.dump(trans_res, open('concept_translate_backup.json', 'w', encoding='utf-8'), indent=4, ensure_ascii=False)
        quit()

    try:
        translation=soup.find(class_='base-list switch_part').find_all('p') # find dictionary result

        for i in range(len(translation)): # remove the labels
            translation[i]=re.sub(r'<span>','',str(translation[i]))
            translation[i]=re.sub(r'</span>','',str(translation[i]))
            translation[i]=re.sub(r'<p>','',str(translation[i]))
            translation[i]=re.sub(r'</p>','',str(translation[i]))
            translation[i]=re.sub(r'\n','',str(translation[i]))
        trans_res[word]=', '.join(translation)
        word_cnt+=1
    except:
        try:  # no dictionary result, try to find translation result
            translation=soup.find(class_='in-base-top clearfix').find('div')
            translation=re.sub(r'<div style=".*">','',str(translation))
            translation=re.sub(r'</div>','',str(translation))
            if not re.match(r'[a-zA-Z]+',translation) and not re.search(r'亲，你要找的是不是',translation):
                trans_res[word]=translation
                word_cnt+=1
            else:  # the word is implicitly transformed to a similar word
                print('[ERROR] word {} cannot be translated'.format(word))
                trans_res[word]=''
        except:
            print('[ERROR] word {} cannot be translated'.format(word))
            trans_res[word]=''

trans_res = json.dumps(trans_res,ensure_ascii=False)
json.dump(eval(trans_res), open('concept_translate.json', 'w', encoding='utf-8'), indent=4, ensure_ascii=False)
print('[INFO] {} words translated succesfully'.format(word_cnt))


