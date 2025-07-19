import json
import sys

def search_key_or_value_paths(obj, target, path=None, results=None):
    if path is None:
        path = []
    if results is None:
        results = []

    if isinstance(obj, dict):
        for k, v in obj.items():
            new_path = path + [k]
            # Match su chiave
            if k == target:
                results.append(new_path)
            # Match su valore
            if isinstance(v, str) and v == target:
                results.append(new_path)
            search_key_or_value_paths(v, target, new_path, results)

    elif isinstance(obj, list):
        for idx, item in enumerate(obj):
            new_path = path + [f"[{idx}]"]
            search_key_or_value_paths(item, target, new_path, results)

    return results

def format_path(p):
    if p and isinstance(p[0], str) and p[0].startswith("ansible_"):
        p = [p[0][len("ansible_"):]] + p[1:]
    return ''.join([f"[{repr(x)}]" if not str(x).startswith('[') else x for x in p])

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 search_facts.py <facts.json> <key_or_value_to_search>")
        sys.exit(1)

    facts_file = sys.argv[1]
    target = sys.argv[2]

    with open(facts_file) as f:
        data = json.load(f)

    facts = data.get("ansible_facts", data)

    matches = search_key_or_value_paths(facts, target)

    if matches:
        print(f"🔍 Found {len(matches)} match(es) for '{target}':\n")
        for m in matches:
            print(f"ansible_facts{format_path(m)}")
    else:
        print(f"❌ No matches found for '{target}'.")

if __name__ == "__main__":
    main()
