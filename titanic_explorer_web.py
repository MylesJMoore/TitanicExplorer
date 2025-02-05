from flask import Flask, render_template, request
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Set the backend to Agg
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# Load the dataset
data = pd.read_csv("data/titanic.csv")

# Function to predict survival
def predict_survival(age, gender, pclass):
    if gender == "female" and pclass == 1:
        return "High chance of survival."
    elif age < 10:
        return "High chance of survival."
    else:
        return "Low chance of survival."

# Function to visualize age distribution
def plot_age_distribution():
    plt.figure()
    data['Age'].hist(bins=20)
    plt.title("Age Distribution of Passengers")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()  # Close the figure to free up memory
    return base64.b64encode(img.getvalue()).decode()

@app.route("/")
def home():
    # Plot age distribution
    age_plot = plot_age_distribution()
    return render_template("index.html", age_plot=age_plot)

@app.route("/predict", methods=["POST"])
def predict():
    age = int(request.form["age"])
    gender = request.form["gender"].lower()
    pclass = int(request.form["pclass"])
    prediction = predict_survival(age, gender, pclass)
    return render_template("result.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)