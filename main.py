import scraper
import analyzer

def run_pipeline():
    print("=== MEMULAI AUTOMATED DATA PIPELINE ===")
    
    scraper.fetch_umkm_data()
    
    analyzer.analyze_and_clean_data()
    
    print("=== PIPELINE SELESAI ===")

if __name__ == "__main__":
    run_pipeline()