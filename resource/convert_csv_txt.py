import pandas as pd

df = pd.read_csv('../data/dataset.csv')

txt_file = '../addvocab3.txt'

# with open(txt_file, 'w', encoding='utf-8') as f:
#     for column in ["DRUG_NAME","DOSAGE","FORM","DRUG_REG_NO","MFG_DATE","EXP_DATE","WARNINGS","INDICATIONS","USAGE_INSTRUCTIONS"]:
#         for row in df[column]:
#             f.write(row+'\n')

with open(txt_file, 'w', encoding='utf-8') as f:
    for column in ["DRUG_NAME"]:
        for row in df[column]:
            f.write('_' + row+'\n')