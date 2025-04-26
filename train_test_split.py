from sklearn.model_selection import train_test_split
import pandas as pd

dataframe = pd.read_csv('prescription_data/summary_prescription_data.csv', encoding='utf-8')
train_df, temp_df = train_test_split(dataframe, test_size=0.2, random_state=42)
test_df, eval_df = train_test_split(temp_df, test_size=0.5, random_state=42)

train_df.to_csv('prescription_data/train.csv', index=False, encoding='utf-8')
test_df.to_csv('prescription_data/test.csv', index=False, encoding='utf-8')
eval_df.to_csv('prescription_data/eval.csv', index=False, encoding='utf-8')

print(f"Train set size: {train_df.shape}")
print(f"Test set size: {test_df.shape}")
print(f"Evaluation set size: {eval_df.shape}")