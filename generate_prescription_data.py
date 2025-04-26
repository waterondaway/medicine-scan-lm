import random
import pandas as pd
from faker import Faker
fake = Faker('th_TH')

def format_thai_date(date):
    thai_months = [
        "มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", 
        "มิถุนายน", "กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", 
        "พฤศจิกายน", "ธันวาคม"
    ]
    day = date.day
    month = thai_months[date.month - 1]
    year = date.year + 543
    return f"{day} {month} {year}"

medicine = pd.read_csv('prescription_data/medicine.csv', encoding='utf-8')
dosage = pd.read_csv('prescription_data/dosage.csv', encoding='utf-8')
form = pd.read_csv('prescription_data/form.csv', encoding='utf-8')
indications = pd.read_csv('prescription_data/indications.csv', encoding='utf-8')
usage = pd.read_csv('prescription_data/usage.csv', encoding='utf-8')
warnings = pd.read_csv('prescription_data/warnings.csv', encoding='utf-8')

record_array = []
for _ in range(15000):
    patient_name = fake.name()
    patient_id = fake.random_int(min=100000, max=999999)
    patient_birthdate = fake.date_of_birth(minimum_age=0, maximum_age=100)
    thai_birthdate = format_thai_date(patient_birthdate) 
    mfg_date = fake.date_between(start_date="-1y", end_date="today")
    exp_date = fake.date_between(start_date="+1y", end_date="+3y")
    record = {
        "patient_name": patient_name,
        "patient_id": patient_id,
        "patient_birthdate": thai_birthdate, 
        "drug_name": random.choice(medicine['medicine'].tolist()),
        "dosage": random.choice(dosage['dosage'].tolist()),
        "form": random.choice(form['form'].tolist()),
        "drug_reg_no": '#' + str(fake.random_int(min=000, max=999)),
        "mfg_date": mfg_date,
        "exp_date": exp_date,
        "warnings": random.choice(warnings['warnings'].tolist()),
        "indications": random.choice(indications['indications'].tolist()),
        "usage_instructions": random.choice(usage['usage'].tolist()),
    }
    record_array.append(record)

df = pd.DataFrame(record_array)
df.to_csv("prescription_data/summary_prescription_data.csv", index=False, encoding="utf-8-sig")
print("finish work : prescription_data.csv")