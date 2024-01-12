from flask import Flask, render_template
import requests

app = Flask(__name__)

# Function to fetch a random joke from JokeAPI
def get_random_joke():
    url = "https://v2.jokeapi.dev/joke/Any"
    response = requests.get(url)
    joke_data = response.json()

    if 'joke' in joke_data:
        return joke_data['joke']
    elif 'setup' in joke_data and 'delivery' in joke_data:
        return f"{joke_data['setup']} {joke_data['delivery']}"
    else:
        return "Failed to fetch joke."

# Route to render the index page
@app.route('/')
def index():
    joke = get_random_joke()
    return render_template('index.html', joke=joke)

if __name__ == '__main__':
    app.run(debug=True)
