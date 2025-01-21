import pandas as pd
import re

# Load the CSV dataset
df = pd.read_csv("../src/data/telegram_messages_preprocessed.csv")  # Replace with your file name

# Function to detect if a text is Amharic
def is_amharic(text):
    # Check if the text contains Amharic characters
    return bool(re.search(r'[\u1200-\u137F]', text))

# Function to tokenize and label each message
def label_entities(text):
    # Define the entity types and patterns (you can expand these as needed)
    product_keywords = ["Playpen", "Teether", "Silicone", "Rattle", "Baby", "Ball"]
    location_keywords = ["Addis Ababa", "Bole", "Sinayel", "ሀበሻ", "ገርጂ"]
    price_keywords = ["ብር", "birr", "ዋጋ"]

    # Tokenize the text
    tokens = text.split()
    labeled_tokens = []

    # Process each token and label it
    for token in tokens:
        # Ignore English text except numbers
        if is_amharic(token):
            # Label entities
            if any(keyword in token for keyword in product_keywords):
                if not labeled_tokens or labeled_tokens[-1][1] != "B-Product":
                    labeled_tokens.append((token, "B-Product"))
                else:
                    labeled_tokens.append((token, "I-Product"))
            elif any(keyword in token for keyword in location_keywords):
                if not labeled_tokens or labeled_tokens[-1][1] != "B-LOC":
                    labeled_tokens.append((token, "B-LOC"))
                else:
                    labeled_tokens.append((token, "I-LOC"))
            elif any(keyword in token for keyword in price_keywords):
                if not labeled_tokens or labeled_tokens[-1][1] != "B-PRICE":
                    labeled_tokens.append((token, "B-PRICE"))
                else:
                    labeled_tokens.append((token, "I-PRICE"))
            else:
                labeled_tokens.append((token, "O"))
        else:
            # Handle English and numbers
            if token.isdigit():
                labeled_tokens.append((token, "O"))  # Treat numbers as 'O' for outside of entities
            else:
                labeled_tokens.append((token, "O"))

    return labeled_tokens

# Function to convert the dataset to CoNLL format
def to_conll_format(df):
    conll_data = []

    for index, row in df.iterrows():
        message = row['cleaned_content']
        labeled_tokens = label_entities(message)

        # Add labeled tokens to the CoNLL formatted output
        for token, label in labeled_tokens:
            conll_data.append(f"{token}\t{label}")
        
        # Add a blank line to separate messages
        conll_data.append("")

    return "\n".join(conll_data)

# Convert the dataset to CoNLL format
conll_format_text = to_conll_format(df)

# Save to a file
with open("first_draft.conll", "w", encoding="utf-8") as f:
    f.write(conll_format_text)

print("CoNLL formatted file has been saved.")
