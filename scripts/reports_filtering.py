import pandas as pd
import os

def read_ds():

    df = pd.read_csv("./TCGA_dataset.csv")

    filtered_df = df[(df['gender'] != 'MALE') & (df['sample_type'] != 'Solid Tissue Normal')]

    er_pos = filtered_df[(filtered_df['ER_Status_nature2012'] == 'Positive') &

              (filtered_df['HER2_Final_Status_nature2012'] == 'Negative')]

    others = filtered_df.drop(er_pos.index)

    return filtered_df, er_pos, others
 


data, _, _ = read_ds()

print(data.info())
patients = data['sample'].to_list()


docs = os.listdir('./reports')


for patient in patients:
    for doc in docs:
        p = doc.split('.')[0]
        if p in patient:
            f = open(f'./reports/{doc}','rb')
            f1 = open(f'./valid_documents/{doc}','wb')
            f1.write(f.read())
            f.close()
            f1.close()
            break
