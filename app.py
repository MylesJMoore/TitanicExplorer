from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# Load Titanic dataset
df = pd.read_csv("data/titanic.csv")

@app.route("/", methods=["GET", "POST"])
def home():
    # Get filter values from the request (defaults to empty if no value is selected)
    pclass = request.args.get("pclass", "")
    survived = request.args.get("survived", "")
    gender = request.args.get("gender", "")

    # Apply filters to the DataFrame if any filter is selected
    filtered_df = df

    if pclass:
        filtered_df = filtered_df[filtered_df["Pclass"] == int(pclass)]
    if survived:
        filtered_df = filtered_df[filtered_df["Survived"] == int(survived)]
    if gender:
        filtered_df = filtered_df[filtered_df["Sex"] == gender.lower()]

    # Round values for display
    summary_df = filtered_df.describe().round({"Age": 0, "PassengerId": 0, "SibSp": 0, "Parch": 0, "Fare": 2})

    # Ensure integer-like values do not have .0
    for col in ["Age", "PassengerId", "SibSp", "Parch"]:
        summary_df.loc[["min", "25%", "50%", "75%", "max"], col] = summary_df.loc[["min", "25%", "50%", "75%", "max"], col].astype(int)

    # Convert DataFrame to HTML manually (fixes .0 issue)
    summary = summary_df.to_html(classes="table table-bordered table-hover", float_format=lambda x: f"{int(x)}" if x == int(x) else f"{x:.2f}")

    survival_rate = filtered_df["Survived"].mean() * 100  # Keep as float

    # Generate the graph for filtered data
    fig, ax = plt.subplots(figsize=(8, 5))
    filtered_df["Age"].hist(bins=20, ax=ax, color="skyblue", edgecolor="black")
    ax.set_title("Age Distribution of Passengers")
    ax.set_xlabel("Age")
    ax.set_ylabel("Frequency")

    # Save the plot to a string buffer
    img_buf = io.BytesIO()
    plt.savefig(img_buf, format="png")
    img_buf.seek(0)
    img_base64 = base64.b64encode(img_buf.getvalue()).decode("utf-8")
    img_buf.close()

    return render_template("index.html", 
                           survival_rate=f"{survival_rate:.2f}", 
                           summary=summary,
                           img_base64=img_base64,
                           pclass=pclass, survived=survived, gender=gender)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)  # Bind to 0.0.0.0