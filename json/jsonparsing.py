import json
with open("sample-data.json", "r") as file:
    data = json.load(file)
print("Interface Status")
print("=" * 60)
print("DN")
print("-" * 60)
for item in data["imdata"]:
    dn = item["l1PhysIf"]["attributes"]["dn"]
    print(dn)