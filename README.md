<h1 style="font-family:Arial, sans-serif; color:#2C3E50;">EthioMart Telegram E-Commerce NER System</h1>

<p style="font-family:Verdana, sans-serif; font-size:14px; line-height:1.6;">
Welcome to the <strong>EthioMart Week 5 Challenge</strong> repository! This project is part of the 
<strong>10 Academy Artificial Intelligence Mastery Week 5 Challenge</strong>. The goal of this challenge is 
to develop a Named Entity Recognition (NER) system to extract key business entities from Amharic Telegram messages for the Ethiopian e-commerce context.
</p>

<h2 style="font-family:Arial, sans-serif; color:#34495E;">Overview</h2>

<p style="font-family:Verdana, sans-serif; font-size:14px; line-height:1.6;">
With the rise of Telegram-based e-commerce in Ethiopia, both vendors and customers struggle with managing scattered 
information across various channels. This project addresses these challenges by building a system that extracts structured 
data (such as product names, prices, and locations) from unstructured Amharic Telegram messages.
</p>

<h2 style="font-family:Arial, sans-serif; color:#34495E;">Objectives</h2>
<ul style="font-family:Verdana, sans-serif; font-size:14px; line-height:1.6;">
  <li>Telegram Scraping: Collect messages from targeted e-commerce Telegram channels.</li>
  <li>Data Preprocessing and Labeling: Clean the scraped data and label entities in the CoNLL format.</li>
  <li>NER Model Training: Fine-tune pre-trained models (e.g., AfroXLM-R, BERT, and RoBERTa) for Amharic NER tasks.</li>
  <li>Model Evaluation: Compare model performance and select the best-performing one for production.</li>
  <li>Model Interpretability: Leverage tools like SHAP and LIME to enhance model explainability.</li>
</ul>

<h2 style="font-family:Arial, sans-serif; color:#34495E;">Repository Structure</h2>

<pre style="font-family:Courier New, monospace; font-size:13px; background-color:#F4F6F7; padding:10px; border-radius:5px;">
├── notebooks                   # Jupyter notebooks for fine-tuning and experimentation
│   ├── __init__.py
│   ├── afroxmlr_fine_tune.ipynb    # Fine-tuning AfroXLM-R for NER tasks
│   ├── bert_fine_tuning.ipynb      # Fine-tuning BERT-tiny for NER tasks
│   └── roberta_fine_tune.ipynb    # Fine-tuning RoBERTa for NER tasks
│
├── scripts                     # Scripts for data scraping and labeling
│   ├── __init__.py
│   ├── collin_labler.py         # Annotates data in CoNLL format
│   └── telegram_scraper.py      # Scrapes messages from Telegram channels
│
├── src                         # Source files and datasets
│   ├── __init__.py
│   └── data                     # Raw and labeled datasets
│       ├── first_draft.conll      # Draft labeled data for testing
│       ├── labeled_ner_data.conll # Final labeled dataset in CoNLL format
│       ├── telegram_messages_preprocessed.csv # Preprocessed scraped data
│       └── telegram_messages_raw.csv          # Raw scraped data
│
├── tests                       # Placeholder for testing scripts
│   ├── __init__.py
│
├── .env                        # Environment variables (API credentials)
├── .gitignore                  # Ignored files and directories
├── README.md                   # Project documentation
├── requirements.txt            # Dependencies for the project
</pre>

<h2 style="font-family:Arial, sans-serif; color:#34495E;">Getting Started</h2>

<h3 style="font-family:Arial, sans-serif; color:#2E86C1;">Prerequisites</h3>
<ul style="font-family:Verdana, sans-serif; font-size:14px; line-height:1.6;">
  <li>Python 3.8 or higher</li>
  <li>Telegram API credentials (API ID and API Hash)</li>
  <li>Dependencies listed in <code>requirements.txt</code></li>
</ul>

<h3 style="font-family:Arial, sans-serif; color:#2E86C1;">Installation</h3>
<ol style="font-family:Verdana, sans-serif; font-size:14px; line-height:1.6;">
  <li>Clone the repository:
    <pre style="font-family:Courier New, monospace; background-color:#F4F6F7; padding:10px; border-radius:5px;">
git clone https://github.com/Yayerad/Ethiomart-W5.git
cd Ethiomart-W5
    </pre>
  </li>
  <li>Install dependencies:
    <pre style="font-family:Courier New, monospace; background-color:#F4F6F7; padding:10px; border-radius:5px;">
pip install -r requirements.txt
    </pre>
  </li>
  <li>Configure the <code>.env</code> file with your Telegram API credentials:
    <pre style="font-family:Courier New, monospace; background-color:#F4F6F7; padding:10px; border-radius:5px;">
API_ID=your_api_id
API_HASH=your_api_hash
    </pre>
  </li>
</ol>

<h2 style="font-family:Arial, sans-serif; color:#34495E;">Results</h2>

<p style="font-family:Verdana, sans-serif; font-size:14px; line-height:1.6;">
- Fine-tuned multiple NER models for Amharic with high accuracy.  
- Extracted key business entities from Telegram messages (e.g., product names, prices, and locations).  
- Selected the best-performing model after evaluation and comparison.  
</p>

<h2 style="font-family:Arial, sans-serif; color:#34495E;">Contributing</h2>

<p style="font-family:Verdana, sans-serif; font-size:14px; line-height:1.6;">
Contributions are welcome! Feel free to fork this repository, create a feature branch, and submit a pull request.
</p>

<h2 style="font-family:Arial, sans-serif; color:#34495E;">License</h2>

<p style="font-family:Verdana, sans-serif; font-size:14px; line-height:1.6;">
This project is licensed under the MIT License. See the <code>LICENSE</code> file for details.
</p>
