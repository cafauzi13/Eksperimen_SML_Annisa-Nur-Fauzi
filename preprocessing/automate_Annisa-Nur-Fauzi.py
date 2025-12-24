import pandas as pd
import os # Tambahkan library ini

def preprocess_data(input_path, output_path):
    # 1. Load Data
    df = pd.read_csv(input_path)
    
    # 2. Preprocessing Logic
    df['age'] = df['age'].fillna(df['age'].median())
    df_clean = df.drop(['deck', 'embark_town', 'alive'], axis=1, errors='ignore')
    
    # 3. Cek dan buat folder jika belum ada
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # 4. Save Clean Data
    df_clean.to_csv(output_path, index=False)
    print("Preprocessing Automate Success!")

if __name__ == "__main__":
    preprocess_data(
        'titanic_raw/train.csv', 
        'preprocessing/titanic_preprocessing/titanic_clean.csv'
    )

    