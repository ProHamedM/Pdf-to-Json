import pymupdf
import json

PDF_PATH = r"D:\Projects\Python\PDF_to_JSON\Shahname Ferdosi.pdf"
JSON_PATH = r"D:\Projects\Python\PDF_to_JSON\Shahname Ferdosi.json"

pages_data = []

# Open PDF
doc = pymupdf.open(PDF_PATH)
print ("Log: opening file;")

# Store PDF content in a Python list
for page_num, page in enumerate(doc, start=1):

    print (f"Log: reading page {page_num};")

    lines = [
        line.strip()
        for line in page.get_text().splitlines()
        if line.strip()
    ]

    pages_data.append({
        "page": page_num,
        "content": [
            {
                "line": idx + 1,
                "text": line
            }
            for idx, line in enumerate(lines)
        ]
    })


# Format to & Save JSON locally
print("Log: formating to JSON;")
with open(JSON_PATH, "w", encoding="utf-8") as json_file:
    json.dump(
        pages_data,
        json_file,
        ensure_ascii=False,
        indent=4
    )

print(f"JSON saved to: {JSON_PATH}")
