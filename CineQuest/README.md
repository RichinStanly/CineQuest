# 🎬 CineQuest // X: The Next-Gen Movie Recommender

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn)
![API](https://img.shields.io/badge/TMDB-API-green?style=for-the-badge)

> **"Discover your next favorite film in a Cyberpunk-styled universe."**

**CineQuest // X** is an advanced Content-Based Recommendation Engine capable of suggesting movies based on plot similarity. Unlike standard recommenders, it features a **responsive "Neon Glassmorphism" UI**, real-time data fetching, and an immersive user experience.

---

## 📸 Screenshots

| **Home Interface** | **Recommendations Grid** |
|:---:|:---:|
| <img width="800" alt="Home Screen" src="[https://github.com/user-attachments/assets/2cce1fc0-518d-4f94-9a85-aea38942b57b](https://github.com/user-attachments/assets/2cce1fc0-518d-4f94-9a85-aea38942b57b)" /> | <img width="800" alt="Results Grid" src="[https://github.com/user-attachments/assets/bb3f28ed-91fe-4920-af6e-747af25e70db](https://github.com/user-attachments/assets/bb3f28ed-91fe-4920-af6e-747af25e70db)" /> |

---

## ⚡ Key Features

* **🧠 AI-Powered Engine:** Uses **Natural Language Processing (NLP)** and **Cosine Similarity** to analyze over 5,000 movie plots and find hidden connections.
* **🎨 Cyberpunk UI:** A custom-coded interface featuring animated gradients, floating glass cards, and neon hover effects.
* **📡 Real-Time Data:** Fetches the latest posters, ratings, and plot summaries via the **TMDB API**.
* **🛡️ Smart Error Handling:** Includes auto-retry logic to handle API rate limits smoothly.
* **📂 Interactive Data Chips:** "Decrypt" movie plots using a futuristic pop-over interaction.

---

## 🛠️ Installation & Setup Guide

### ⚡ Quick Start (Terminal Commands)
Run these commands in order to set up the project environment:

```bash
# 1. Clone the repository
git clone https://github.com/RichinStanly/CineQuest.git
cd CineQuest

# 2. Install required libraries
pip install -r requirements.txt

🛑 Manual Steps (Required)
Because of file size limits and security, you must do these 3 steps manually:

Step A: Download the Data

Download the TMDB 5000 Movie Dataset from Kaggle.

Place tmdb_5000_movies.csv and tmdb_5000_credits.csv inside this folder.

Step B: Generate the AI Model
Run this script to train the model on your machine: python setup_model.py

Step C: Add Your API Key

Get a free API Key from TheMovieDB.org.

Open app.py, find api_key = "..." (around line 45), and paste your key.

🚀 Run the App
streamlit run app.py

❓ FAQ / Troubleshooting
Q: Why do I have to download data manually?

A: GitHub has a 100MB file limit. The dataset and the generated model files (.pkl) are too large to upload directly, so you generate them locally.

Q: Why isn't the API Key included?

A: For security reasons, API keys should never be shared publicly. You must use your own free key from TMDB.

Q: I get a "Rate Limit" error?

A: The app includes auto-retry logic, but if you click too fast, TMDB might pause you. Just wait 5 seconds and try again.

<p align="center">
Built with ❤️ by Richin
</p>
