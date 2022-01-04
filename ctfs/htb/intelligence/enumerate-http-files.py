import urllib.request

base_url = "http://some_host"

for year in range(0, 22):
    for month in range(1, 13):
        for day in range(1, 32):
            pdf_name = f"20{year:02}-{month:02}-{day:02}-upload.pdf"
            print(f"Downloading: {base_url}/documents/{pdf_name}")
            try:
                urllib.request.urlretrieve(f"{base_url}/documents/{pdf_name}", f"pdfs/{pdf_name}")
            except:
                print("Could not find file")
