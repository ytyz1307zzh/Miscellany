"""
A script to compare different models in generating sentence embedding.
"""

import torch
from transformers import BertModel, BertTokenizer
torch.set_printoptions(precision=3, edgeitems=20, sci_mode=False, threshold=100)
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased', output_hidden_states=True)
sentences = ['steam has relation with heat',
             'heating can cause high temperature',
             'explosion is able to create heat',
             'heat is a type of what makes temperature rise',
             'heat can be generated in explosion']
embed_list = []
for sent in sentences:
    input_ids = torch.tensor([tokenizer.encode(sent, add_special_tokens=True)])
    with torch.no_grad():
        outputs = model(input_ids)
    sent_embed = outputs[2][-2].squeeze()
    mean_embed = sent_embed.mean(dim=0)
    embed_list.append(mean_embed)

for i in range(len(embed_list)):
    sim_list = []
    for j in range(len(embed_list)):
        sim_list.append(torch.nn.functional.cosine_similarity(embed_list[i], embed_list[j], dim=-1))
    print(sim_list)
print()

embed_list = []
for sent in sentences:
    input_ids = torch.tensor([tokenizer.encode(sent, add_special_tokens=True)])
    with torch.no_grad():
        outputs = model(input_ids)
    sent_embed = outputs[2][-1].squeeze()
    mean_embed = sent_embed.mean(dim=0)
    embed_list.append(mean_embed)

for i in range(len(embed_list)):
    sim_list = []
    for j in range(len(embed_list)):
        sim_list.append(torch.nn.functional.cosine_similarity(embed_list[i], embed_list[j], dim=-1))
    print(sim_list)
print()

from allennlp.modules.elmo import Elmo, batch_to_ids
elmo = Elmo('./elmo/elmo_2x4096_512_2048cnn_2xhighway_options.json', './elmo/elmo_2x4096_512_2048cnn_2xhighway_weights.hdf5',
            num_output_representations=1, requires_grad=False, do_layer_norm=False, dropout=0)
embed_list = []
for sent in sentences:
    char_paragraph = batch_to_ids([sent.split()])
    with torch.no_grad():
        elmo_embeddings = elmo(char_paragraph)['elmo_representations'][0]
    mean_embed = elmo_embeddings.squeeze().mean(dim=0)
    embed_list.append(mean_embed)

for i in range(len(embed_list)):
    sim_list = []
    for j in range(len(embed_list)):
        sim_list.append(torch.nn.functional.cosine_similarity(embed_list[i], embed_list[j], dim=-1))
    print(sim_list)
print()

from sentence_transformers import SentenceTransformer
model = SentenceTransformer('bert-base-nli-mean-tokens')
embed_list = []
for sent in sentences:
    with torch.no_grad():
        outputs = model.encode([sent])
    sent_embed = torch.tensor(outputs[0])
    embed_list.append(sent_embed)

for i in range(len(embed_list)):
    sim_list = []
    for j in range(len(embed_list)):
        sim_list.append(torch.nn.functional.cosine_similarity(embed_list[i], embed_list[j], dim=-1))
    print(sim_list)
