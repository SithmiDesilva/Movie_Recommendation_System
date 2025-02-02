function getRecommendations() {
    const emotion = document.getElementById('emotion').value;
    fetch('/recommend', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `emotion=${emotion}`
    })
    .then(response => response.json())
    .then(data => {
        const moviesList = document.getElementById('movies');
        moviesList.innerHTML = ''; // Clear previous results
        if (data.movies && data.movies.length > 0) {
            data.movies.forEach(movie => {
                const li = document.createElement('li');
                li.textContent = movie;
                moviesList.appendChild(li);
            });
        } else {
            const li = document.createElement('li');
            li.textContent = 'No movies found.';
            moviesList.appendChild(li);
        }
    })
    .catch(error => console.error('Error:', error));
}