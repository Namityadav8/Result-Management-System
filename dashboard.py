from flask import Flask, render_template
import plotly.express as px
import pandas as pd

app = Flask(__name__)

@app.route("/")
def dashboard():
    data = {"Subjects": ["Electronics", "Programming", "Database", "Data Science", "Mathematics", "DSA"],
            "Average Marks": [75, 80, 70, 85, 78, 74]}
    df = pd.DataFrame(data)
    fig = px.bar(df, x="Subjects", y="Average Marks", title="Average Marks per Subject")
    graph = fig.to_html(full_html=False)
    return render_template("dashboard.html", graph=graph)

if __name__ == "__main__":
    app.run(debug=True)