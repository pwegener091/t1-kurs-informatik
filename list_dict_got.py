personen = [
    {"Name": "Arya", "Haus": "Stark", "Waffe": "Schwert"},
    {"Name": "Cersei", "Haus": "Lannister", "Waffe": None},
    {"Name": "Daenerys", "Haus": "Targaryen", "Waffe": "Drachen"},
    {"Name": "Jaime", "Haus": "Lannister", "Waffe": "Schwert"},
]

for p in personen:
    if p["Waffe"] != None:
        print(f"{p["Name"]} aus dem Haus {p["Haus"]} mit der Waffe {p["Waffe"]}")
    else:
        print(f"{p["Name"]} aus dem Haus {p["Haus"]} ist unbewaffnet.")


