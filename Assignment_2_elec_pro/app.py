from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("election_dataset.csv")

# -----------------------------------------
# 1️⃣ Province Endpoint
# -----------------------------------------
@app.route("/province")
def province_data():
    province = request.args.get("province")

    if province:
        filtered = df[df["province"] == province]
        return jsonify(filtered.to_dict(orient="records"))
    else:
        return jsonify(df.to_dict(orient="records"))

# -----------------------------------------
# 2️⃣ History Endpoint
# -----------------------------------------
@app.route("/history")
def history_data():
    year = request.args.get("year")
    province = request.args.get("province")

    filtered = df

    if year:
        filtered = filtered[filtered["year"] == int(year)]

    if province:
        filtered = filtered[filtered["province"] == province]

    return jsonify(filtered.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
