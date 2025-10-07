# jain_2017.csv gathered names and sequences from Supplementary Dataset 2 and mapped it to corresponding ELISA counts from Supplementary Dataset 3.
# 
# Source: 
# Jain T, Sun T, Durand S, Hall A, Houston NR, Nett JH, Sharkey B, Bobrowicz B, Caffry I, Yu Y, Cao Y, Lynaugh H, Brown M, Baruah H, Gray LT,
# Krauland EM, Xu Y, Vásquez M, Wittrup KD. Biophysical properties of the clinical-stage antibody landscape. Proc Natl Acad Sci U S A. 2017 
# Jan 31;114(5):944-949. doi: 10.1073/pnas.1616408114. Epub 2017 Jan 17. PMID: 28096333; PMCID: PMC5293111.

import pandas as pd

# Read csv
df = pd.read_csv("jain_2017.csv")

# Rename sequence columns
df_for_json = df.rename(columns={'VH': 'PROT_fastaH_raw', 'VL': 'PROT_fastaL_raw'})

# Create json format
df_for_json.to_json('consolidated_data_jain_2017.json', orient='records', indent=4)