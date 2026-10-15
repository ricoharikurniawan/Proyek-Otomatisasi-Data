import pandas as pd
import json

def analyze_and_clean_data():
    print("Memulai pembersihan dan analisis data...")
    
   
    with open("data/raw_umkm_data.json", "r") as file:
        raw_data = json.load(file)
        
   
    df = pd.DataFrame(raw_data['products'])
    
   
    df_clean = df[['id', 'title', 'category', 'price', 'discountPercentage', 'stock']]
    
    
    df_clean.loc[:, 'final_price'] = df_clean['price'] - (df_clean['price'] * df_clean['discountPercentage'] / 100)
    
   
    csv_path = "data/clean_umkm_data.csv"
    df_clean.to_csv(csv_path, index=False)
    
    print(f"Sukses! Data dibersihkan dan disimpan di {csv_path}")
    
    
    low_stock = df_clean[df_clean['stock'] < 20]
    print("\n--- RINGKASAN WAWASAN BISNIS ---")
    print(f"Total Produk Dianalisis: {len(df_clean)} item")
    print(f"Rata-rata Harga Final: ${df_clean['final_price'].mean():.2f}")
    print(f"Peringatan: Ada {len(low_stock)} produk dengan stok menipis (di bawah 20)!")

if __name__ == "__main__":
    analyze_and_clean_data()