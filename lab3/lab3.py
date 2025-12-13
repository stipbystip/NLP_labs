from transformers import BertForMaskedLM, BertTokenizer
import torch

model_name = "DeepPavlov/rubert-base-cased"
model = BertForMaskedLM.from_pretrained(model_name)
tokenizer = BertTokenizer.from_pretrained(model_name)


sentence = "Он [MASK] проблемой, он сам виноват."

inputs = tokenizer(sentence, return_tensors="pt")
with torch.no_grad():
    logits = model(**inputs).logits[0]

mask_idx = (
    (inputs.input_ids[0] == tokenizer.mask_token_id).nonzero(as_tuple=True)[0].item()
)
top_ids = torch.topk(logits[mask_idx], 10).indices

words = [
    tokenizer.convert_ids_to_tokens(int(i)).replace("##", "").lower() for i in top_ids
]
if "перед" in words and "«является»" in words:
    print("Ура\n")
print(words)
