from flask import Flask, render_template
import pandas as pd
import folium
from folium.plugins import MarkerCluster
import plotly.express as px

app = Flask(__name__)

# Load dataset
df = pd.read_csv("cleaned_covid_trials.csv")

@app.route("/")
def index():
    # ---------------- MAP ----------------
    m = folium.Map(location=[20, 0], zoom_start=2)
    marker_cluster = MarkerCluster().add_to(m)

    # If latitude/longitude exists, plot markers
    if "Latitude" in df.columns and "Longitude" in df.columns:
        for _, row in df.dropna(subset=["Latitude", "Longitude"]).iterrows():
            popup_text = f"""
            <b>{row.get('Trial ID', 'N/A')}</b><br>
            Phase: {row.get('Phases', 'N/A')}<br>
            Status: {row.get('Status', 'N/A')}<br>
            Type: {row.get('Study Type', 'N/A')}
            """
            folium.Marker(
                location=[row["Latitude"], row["Longitude"]],
                popup=popup_text,
                icon=folium.Icon(color="blue", icon="info-sign"),
            ).add_to(marker_cluster)
    map_html = m._repr_html_()

    # ---------------- CHARTS ----------------
    # 1. Trials by Phase
    if "Phases" in df.columns:
        phase_counts = df["Phases"].value_counts().reset_index()
        phase_counts.columns = ["Phase", "Count"]
        fig_phase = px.bar(phase_counts, x="Phase", y="Count", title="Trials by Phase")
        phase_chart = fig_phase.to_html(full_html=False)
    else:
        phase_chart = None

    # 2. Study Type distribution
    if "Study Type" in df.columns:
        fig_type = px.pie(df, names="Study Type", title="Distribution of Study Types")
        type_chart = fig_type.to_html(full_html=False)
    else:
        type_chart = None

    # 3. Trials started over time
    if "Start Date" in df.columns:
        df["Start Date"] = pd.to_datetime(df["Start Date"], errors="coerce")
        df_time = df.dropna(subset=["Start Date"])
        time_counts = (
            df_time["Start Date"]
            .dt.to_period("M")
            .value_counts()
            .sort_index()
            .reset_index()
        )
        time_counts.columns = ["Month", "Count"]
        time_counts["Month"] = time_counts["Month"].astype(str)

        fig_time = px.line(time_counts, x="Month", y="Count", title="Trials Started Over Time")
        time_chart = fig_time.to_html(full_html=False)
    else:
        time_chart = None

    return render_template(
        "index.html",
        map_html=map_html,
        phase_chart=phase_chart,
        type_chart=type_chart,
        time_chart=time_chart
    )

if __name__ == "__main__":
    app.run(debug=True)
