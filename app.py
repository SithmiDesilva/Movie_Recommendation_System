from flask import Flask, request, jsonify, render_template
import requests
from bs4 import BeautifulSoup
import re
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Dictionary to map emotions to IMDb URLs
URLS = {
    "Drama": 'https://www.imdb.com/search/title/?title_type=feature&genres=drama',
    "Action": 'https://www.imdb.com/search/title/?title_type=feature&genres=action',
    "Comedy": 'https://www.imdb.com/search/title/?title_type=feature&genres=comedy',
    "Horror": 'https://www.imdb.com/search/title/?title_type=feature&genres=horror',
    "Crime": 'https://www.imdb.com/search/title/?title_type=feature&genres=crime',
    "Romance": 'https://www.imdb.com/search/title/?title_type=feature&genres=romance',
    "Adventure": 'https://www.imdb.com/search/title/?title_type=feature&genres=adventure',
    "Mystery": 'https://www.imdb.com/search/title/?title_type=feature&genres=mystery',
    "Animation": 'https://www.imdb.com/search/title/?title_type=feature&genres=animation',
    "Scientific Fiction": 'https://www.imdb.com/search/title/?title_type=feature&genres=sci-fi',
    "Thriller": 'https://www.imdb.com/search/title/?title_type=feature&genres=thriller',
    "Fantasy": 'https://www.imdb.com/search/title/?title_type=feature&genres=fantasy',
    "Biography": 'https://www.imdb.com/search/title/?title_type=feature&genres=biography',
    "Family": 'https://www.imdb.com/search/title/?title_type=feature&genres=family',
    "History": 'https://www.imdb.com/search/title/?title_type=feature&genres=history',
    "Music": 'https://www.imdb.com/search/title/?title_type=feature&genres=music',
}

def get_movies(emotion):
    url = URLS.get(emotion)
    if not url:
        return []

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Fetch the webpage content
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract movie titles
    titles = [a.get_text() for a in soup.find_all('a', href=re.compile(r'/title/tt\d+/'))]
    return titles[:40]  # Return only the first 20 titles

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def contact():
    return render_template('login.html')
    
@app.route('/recommend', methods=['POST'])
def recommend():
    emotion = request.form.get('emotion')
    if not emotion:
        return jsonify({"error": "Emotion not provided"}), 400

    movies = get_movies(emotion)
    return jsonify({"movies": movies})

if __name__ == '__main__':
    app.run(debug=True)