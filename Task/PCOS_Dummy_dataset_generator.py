import pandas as pd
import random

n=200  #number of rows

weight_gain_levels = ['None', 'Mild', 'Severe']
cycle_delay_levels = ['Regular', 'Irregular', 'Absent']
acne_levels = ['None', 'Mild', 'Moderate', 'Severe']
hair_growth_levels = ['None', 'Mild', 'Severe']

def assign_likely_PCOS(row):
    score = 0
    if row['Pain'] == 1: 
        score += 1
    if row['Weight Gain'] == 'Mild':
        score += 1
    if row['Weight Gain'] == 'Severe':
        score += 2
    if row['Cycle Delay'] == 'Absent': 
        score += 2
    elif row['Cycle Delay'] == 'Irregular': 
        score += 1
    if row['Acne'] in ['Moderate', 'Severe']: 
        score += 1
    if row['Polycystic Ovaries'] == 1: 
        score += 2
    if row['Excessive Hair Growth'] == 'Severe': 
        score += 2
    if row['Scalp Hair Loss'] == 1: 
        score += 1
    if row['Infertility'] == 1: 
        score += 1
    if row['Dark Skin Patches'] == 1: 
        score += 1

    return 1 if score >=5 else 0
    
data = []
for i in range (n):
        row = {
        'Pain': random.randint(0, 1),
        'Weight Gain': random.choice(weight_gain_levels),
        'Cycle Delay': random.choice(cycle_delay_levels),
        'Acne': random.choice(acne_levels),
        'Polycystic Ovaries': random.randint(0, 1),
        'Excessive Hair Growth': random.choice(hair_growth_levels),
        'Scalp Hair Loss': random.randint(0, 1),
        'Infertility': random.randint(0, 1),
        'Dark Skin Patches': random.randint(0, 1)
         }
        row['Likely PCOS?'] = assign_likely_PCOS(row)
        data.append(row)

             
         
df= pd.DataFrame(data)      

df.to_csv("dummy_dataset.csv", index=True)

print('Dataset created')