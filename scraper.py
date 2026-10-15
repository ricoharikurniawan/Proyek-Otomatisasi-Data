import requests
import json
import os

def fetch_umkm_data():
    print("Memulai ekstraksi data produk e-commerce/UMKM...")
    
   
    url = "https://dummyjson.com/products?limit=50"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        
        if not os.path.exists("data"):
            os.makedirs("data")
            
        
        file_path = "data/raw_umkm_data.json"
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)
            
        print(f"Sukses! Data katalog produk berhasil ditarik dan disimpan di {file_path}")
    else:
        print(f"Gagal menarik data. Kode error: {response.status_code}")

if __name__ == "__main__":
    fetch_umkm_data()