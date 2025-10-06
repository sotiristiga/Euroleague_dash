from google.cloud import storage
import pandas as pd
import io

def load_dataset(bucket_name, file_path):
    # Create client (uses default credentials)
    client = storage.Client()
    
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(file_path)
    
    # Download file as bytes
    data = blob.download_as_bytes()
    
    # Load into pandas DataFrame
    df = pd.read_csv(io.BytesIO(data))
    return df

# Example use
bucket_name = "euroleague-backets"
file_path = "euroleague_2025_2026_playerstats.csv"

df = load_dataset(bucket_name, file_path)
st.write(df)
