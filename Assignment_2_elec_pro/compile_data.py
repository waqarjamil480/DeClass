import requests
import json
import pandas as pd

years = [2008, 2013, 2018]
all_data = []

for year in years:
    url = f"https://api6.tplmaps.com/dawn_election_portal/assets/js/election_{year}.js"
    response = requests.get(url)

    if response.status_code == 200:
        raw_text = response.text
        
        # Remove JS variable part
        json_string = raw_text.split("=", 1)[1].strip().rstrip(";")
        
        data = json.loads(json_string)


        for record in data:
    
            record.pop("geom", None)   # remove geom
            
            record["year"] = year     # add year
            
            all_data.append(record)

        # for record in data:
        #     properties = record["properties"]
            
        #     properties.pop("geom", None)
        #     properties["year"] = year
            
        #     all_data.append(properties)


# Convert to DataFrame
df = pd.DataFrame(all_data)

# Save CSV
df.to_csv("election_dataset.csv", index=False)

print("Dataset Created Successfully!")
