import streamlit as st
import pandas as pd
import pickle
import requests
import time

# -------------------------------------------------------------------------
# 1. SETUP
# -------------------------------------------------------------------------
st.set_page_config(page_title="CINEQUEST//X", page_icon="⚡", layout="wide")

# -------------------------------------------------------------------------
# 2. THE "HYPE" UI (ADVANCED CSS)
# -------------------------------------------------------------------------
st.markdown("""
<style>
    /* IMPORT TRENDY FONT */
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;500;700&family=JetBrains+Mono:wght@400;700&display=swap');

    /* UNIVERSAL FONT OVERRIDE */
    html, body, [class*="css"] {
        font-family: 'Space Grotesk', sans-serif !important;
    }

    /* ANIMATED AURORA BACKGROUND */
    .stApp {
        background-color: #000000;
        background-image: 
            radial-gradient(at 0% 0%, hsla(253,16%,7%,1) 0, transparent 50%), 
            radial-gradient(at 50% 0%, hsla(225,39%,30%,1) 0, transparent 50%), 
            radial-gradient(at 100% 0%, hsla(339,49%,30%,1) 0, transparent 50%);
        background-size: 200% 200%;
        animation: aurora 10s ease infinite;
        color: #fff;
    }
    @keyframes aurora {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    /* TITLES */
    h1 {
        font-size: 5rem !important;
        font-weight: 700 !important;
        letter-spacing: -3px !important;
        background: linear-gradient(to right, #b5179e, #7209b7, #4cc9f0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0px 0px 30px rgba(181, 23, 158, 0.5);
        margin-bottom: 0 !important;
    }
    
    h3 {
        font-weight: 300 !important;
        color: rgba(255, 255, 255, 0.7) !important;
        letter-spacing: 2px;
        text-transform: uppercase;
        font-size: 1rem !important;
    }

    /* MOVIE CARDS HOVER */
    div[data-testid="stImage"] {
        border-radius: 15px;
        overflow: hidden;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    div[data-testid="stImage"]:hover {
        transform: scale(1.05) rotate(1deg);
        box-shadow: 0 10px 40px -10px rgba(76, 201, 240, 0.6);
        border: 1px solid rgba(76, 201, 240, 0.5);
    }
    
    /* MAIN SEARCH BUTTON */
    .stButton > button {
        width: 100%;
        border-radius: 12px;
        background: white;
        color: black;
        font-weight: 800;
        text-transform: uppercase;
        border: none;
        height: 50px;
        transition: all 0.2s;
    }
    .stButton > button:hover {
        background: #4cc9f0;
        color: white;
        box-shadow: 0 0 20px #4cc9f0;
        transform: translateY(-2px);
    }
    
    /* THE "COOL" POPOVER BUTTON (DATA CHIP) */
    div[data-testid="stPopover"] > button {
        background-color: transparent !important;
        border: 1px solid #4cc9f0 !important;
        color: #4cc9f0 !important;
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 12px !important;
        border-radius: 4px !important;
        height: 35px !important;
        transition: all 0.3s ease !important;
    }
    div[data-testid="stPopover"] > button:hover {
        background-color: #4cc9f0 !important;
        color: #000 !important;
        box-shadow: 0 0 10px #4cc9f0 !important;
    }

    /* RATING BADGE */
    .rating-badge {
        background: #f72585;
        color: white;
        padding: 5px 10px;
        border-radius: 8px;
        font-weight: bold;
        font-size: 14px;
        box-shadow: 0 0 10px #f72585;
    }

    /* HIDE JUNK */
    #MainMenu, footer, header {visibility: hidden;}
    
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------------
# 3. BACKEND LOGIC
# -------------------------------------------------------------------------
@st.cache_data
def load_data():
    movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    return movies, similarity

movies, similarity = load_data()

def fetch_details(movie_id):
    
    # ------------------------------------------------------------------
    # ⚠️ INSTRUCTIONS FOR USERS: 
    # 1. Get a free API Key at https://www.themoviedb.org/
    # 2. Paste it inside the quotes below
    # ------------------------------------------------------------------
    api_key = "INSERT_YOUR_TMDB_API_KEY_HERE" 
    
    # Check if the user hasn't inserted their key yet
    if api_key == "INSERT_YOUR_TMDB_API_KEY_HERE":
        # Return a dummy list so the app doesn't crash
        return "https://via.placeholder.com/500x750?text=Insert+API+Key", "Please insert your API Key in app.py", 0, "N/A"

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommendations = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        poster, title, rating, overview = fetch_details(movie_id)
        recommendations.append({
            "poster": poster, 
            "title": title, 
            "rating": rating, 
            "overview": overview
        })
        
    return recommendations

# -------------------------------------------------------------------------
# 4. THE LAYOUT
# -------------------------------------------------------------------------

# HEADER
col1, col2 = st.columns([1, 4])
with col2:
    st.markdown("<h1>CINEQUEST<span style='color:#4cc9f0'>//</span>X</h1>", unsafe_allow_html=True)
    st.markdown("<h3>The Next-Gen Recommendation Engine</h3>", unsafe_allow_html=True)

st.write("")
st.write("")

# SEARCH BAR
with st.container():
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        selected_movie = st.selectbox("SEARCH DATABASE", movies['title'].values)
        if st.button("INITIATE SCAN ⚡"):
            with st.spinner("Decentralizing nodes..."):
                results = recommend(selected_movie)
                
            st.write("")
            st.markdown(f"<div style='text-align:center; font-size:20px; color:#aaa; margin-bottom:20px'>MATCHES FOR <span style='color:white; font-weight:bold'>{selected_movie.upper()}</span></div>", unsafe_allow_html=True)

            # RESULTS GRID
            cols = st.columns(5)
            for idx, col in enumerate(cols):
                with col:
                    # Poster
                    st.image(results[idx]['poster'], use_container_width=True)
                    
                    # Title & Rating Badge
                    st.markdown(f"""
                    <div style="margin-top: 10px; margin-bottom: 10px; display: flex; justify-content: space-between; align-items: center;">
                        <div style="font-weight:bold; font-size:15px; color: white;">{results[idx]['title']}</div>
                        <div class="rating-badge">★ {results[idx]['rating']}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # THE COOL BUTTON (POPOVER)
                    with st.popover("📂 DECRYPT DATA", use_container_width=True):
                        st.markdown(f"### 🎞️ {results[idx]['title']}")
                        st.caption("CONFIDENTIAL PLOT SUMMARY:")
                        st.write(results[idx]['overview'])

# FOOTER
st.markdown("<div style='text-align:center; color:#333; margin-top:50px; font-size:12px'>SYSTEM VERSION 4.2 // CONNECTED</div>", unsafe_allow_html=True)