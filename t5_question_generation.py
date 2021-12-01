# Tip: By now, install transformers from source

from transformers import AutoModelWithLMHead, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("mrm8488/t5-base-finetuned-question-generation-ap")
model = AutoModelWithLMHead.from_pretrained("mrm8488/t5-base-finetuned-question-generation-ap")


def get_question(answer, context, max_length=64):
    input_text = "answer: %s  context: %s </s>" % (answer, context)
    features = tokenizer([input_text], return_tensors='pt')

    output = model.generate(input_ids=features['input_ids'],
                          attention_mask=features['attention_mask'],
                          max_length=max_length)

    return tokenizer.decode(output[0])


context = input("Context: ")
answer = input("Answer: ")

question = get_question(answer, context)
print("Question: ", question)

