import os
import requests
import pandas as pd



labs="2,3,9,15"
main = 'https://www.marham.pk/api/lab/tests-optimized'
diff_labs = labs.split(",")

all_records = []

for labs in diff_labs:
    params = {"lab_id": labs}
    response = requests.get(main, params=params)
    # status = response.status_code
    #all_data = response.json()
    #final_data = all_data['lab_tests']
    

    if response.status_code != 200:
        print(f"some thing went wrong")
        break

    data = response.json()
    tests = data.get("lab_tests", [])   #from that list of lab_tests

    # all required result from  keys
    for test in tests:
        all_records.append({
            "discount": test.get("discount"),
            "discountPercentage": test.get("discountPercentage"),
            "discountedFee": test.get("discountedFee"),
            "fee": test.get("fee"),
            "id": test.get("id"),
            "lab_id": test.get("lab_id"),
            "test_name": test.get("name"),
            "test_type": test.get("type"),
            "lab_name": data.get("name")
        })

# saving data to  csv --took help for pandas
df = pd.DataFrame(all_records)
df.to_csv("wahab_data.csv", index=False)
print(f"Saved {len(df)} all data to marham_data.csv")