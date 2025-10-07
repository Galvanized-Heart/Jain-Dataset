# jain_2017.csv gathered names and sequences from Supplementary Dataset 2 and mapped it to corresponding ELISA counts from Supplementary Dataset 3.
# 
# Source: 
# Jain T, Sun T, Durand S, Hall A, Houston NR, Nett JH, Sharkey B, Bobrowicz B, Caffry I, Yu Y, Cao Y, Lynaugh H, Brown M, Baruah H, Gray LT,
# Krauland EM, Xu Y, Vásquez M, Wittrup KD. Biophysical properties of the clinical-stage antibody landscape. Proc Natl Acad Sci U S A. 2017 
# Jan 31;114(5):944-949. doi: 10.1073/pnas.1616408114. Epub 2017 Jan 17. PMID: 28096333; PMCID: PMC5293111.

import pandas as pd
from datasets import Dataset, DatasetDict, load_dataset

# Read csv
df = pd.read_csv("jain_2017.csv")

# Rename sequence columns
df_prepared = df.rename(columns={'VH': 'PROT_fastaH_raw', 'VL': 'PROT_fastaL_raw'})

# Instatiate huggingface Dataset
hf_dataset = Dataset.from_pandas(df_prepared)
hf_dataset_dict = DatasetDict({'train': hf_dataset})
print("")
print(hf_dataset_dict)

# Push Dataset to huggingface
repo_name = "GalvanizedHeart/jain-2017"
print(f"Pushing dataset to the Hub at repository: {repo_name}")
hf_dataset_dict.push_to_hub(repo_name)

print("Uploaded Jain Dataset")

# Pull Dataset from hugginface
pulled_dataset = load_dataset(repo_name)
print(f"Test: Pulling dataset from the Hub at repository: {repo_name}")
print(pulled_dataset)