import torch
from transformers import BartForConditionalGeneration, BartTokenizer

# Load the pre-trained BART model and tokenizer
model_name = "facebook/bart-large-cnn"
model = BartForConditionalGeneration.from_pretrained(model_name)
tokenizer = BartTokenizer.from_pretrained(model_name)

# Define the text you want to summarize
input_text = """
Write or paste your input text here.
This can be a long document or a single paragraph.
"""

# Tokenize and encode the input text
inputs = tokenizer(input_text, return_tensors="pt", max_length=1024, truncation=True, padding=True)

# Generate the summary
summary_ids = model.generate(inputs["input_ids"], num_beams=4, min_length=30, max_length=200, early_stopping=True)

# Decode the generated summary
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

# Print the summary
print(summary)
