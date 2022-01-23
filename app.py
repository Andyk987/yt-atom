from flask import Flask
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

app = Flask(__name__)

@app.route('/')
def init():
    return "Hello Thanks"

driver = webdriver.Chrome()
url = 'https://www.google.com'
driver.get(url)


if __name__ == '__main__':
    app.run(debug=True)