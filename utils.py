from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "mrm8488/bert-small-finetuned-squadv2"

# a) Get predictions
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
# b) Load model & tokenizer
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

def QA_prediction(question, context):
    QA_input = {
        'question': question,
        'context': context
    }
    res = nlp(QA_input)
    return res