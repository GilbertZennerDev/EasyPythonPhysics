"""
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/test')
def test():
    return "The test has worked!"

app.run()
"""
"""
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
app.run()
"""
"""
import requests
response = requests.get("https://profile-v3.intra.42.fr/")
print(response.status_code)
"""
from bs4 import BeautifulSoup
html = "<html><title>Test</title><body><p>Website<p><div>bla</div></body></html>"
soup = BeautifulSoup(html, 'html.parser')
print(soup.p.text)  # Output: Test
