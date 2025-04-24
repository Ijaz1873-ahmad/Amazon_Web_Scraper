import json

def save_products(query, prds):
    file_name = f"{query.replace(' ', '_')}.json"
    with open(file_name, "w") as file:
        json.dump(prds, file, indent=2)
    print(f"Save {len(prds)} products to {file_name}")