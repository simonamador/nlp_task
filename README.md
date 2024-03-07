# nlp_task
Apply NLP model from HuggingFace for a text classification task related to a Peruvian company.

# Selected Data
Data from MercadoLibre.com was chosen,  specifically from  the listing of products under the Laptops category.
Data was scraped employing the BeautifulSoup library in Python.

# Data Pre-processing
Data was then turned to a Pandas Dataframe, were missing values were set to 0, and regex was employed to 
retrieve the brand from the title of the product pages.

# NLP model
The Text Classifier from MoritzLaurer from Huggingface.com was chosen due to its compatibility with the Spanish
language, as well as its training. It comes from the mDeBERTa-base model by Microsoft, 
which is the best performing multilingual base-sized transformer model as of 2021. It showed a more than 80% 
accuracy for NLI tasks on languages other than English.

Zero-shot classification was done for 2 categories: category and language. Category refers to the goal category
of the description (business, personal or videogame use), and language referred to the language style of the
description (technical or natural).

# Visualization
All visualization was performed employing the Seaborn library in Python.
