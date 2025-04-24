import json

def load_search_queries(file_name = "user_queries.json"):
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except Exception as err:
        print(f"ERROR!!! Failed to load: {err}")
        return []