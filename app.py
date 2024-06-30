from flask import Flask, request, make_response, render_template
import requests
from lxml import html
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fetch', methods=['POST'])
def fetch():
    url = request.form.get('url')
    if not url:
        return 'Invalid request. URL parameter is missing.', 400

    try:
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.text
    except requests.exceptions.RequestException:
        return 'Failed to fetch data from AO3.', 500

    doc = html.fromstring(html_content)
    pagination_links = doc.xpath("//ol[contains(@class, 'pagination')]/li[last()-1]/a")

    if pagination_links:
        total_pages = int(pagination_links[0].text)
    else:
        total_pages = 1

    random_page = random.randint(1, total_pages)

    if '?' in url:
        random_page_url = url.replace(f'page=\d+', f'page={random_page}')
    else:
        random_page_url = f"{url}?page={random_page}"

    try:
        response = requests.get(random_page_url)
        response.raise_for_status()
        random_page_html = response.text
    except requests.exceptions.RequestException:
        return 'Failed to fetch data from AO3.', 500

    response = make_response(random_page_html)
    response.headers.set('Content-Type', 'text/html; charset=utf-8')
    response.headers.set('Access-Control-Allow-Origin', '*')
    response.headers.set('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
    response.headers.set('Access-Control-Allow-Headers', 'Content-Type')
    return response

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)