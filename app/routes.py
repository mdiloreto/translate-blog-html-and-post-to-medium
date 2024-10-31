from flask import Flask, request, jsonify, send_file
from core.scraper import Scraper
from core.translator_azureai import Translator_azure
from core.markdown_ft import Convertmarkdown
import os

app = Flask(__name__)

@app.route('/api/transcribe', methods=['POST'])
def transcribe_video():
    data = request.json
    url = data.get('url')
    if not url:
        return jsonify({"error": "URL is required"}), 400

    # Scrape content
    scraper = Scraper(url)
    scraper.fetch_content()
    content = scraper.html_process()

    # Translate content
    endpoint = os.getenv('AZUREAI_ENDPOINT')
    key = os.getenv('AZUREAI_KEY')
    translator = Translator_azure(endpoint, key)
    content_en = [{'type': el['type'], 'content': translator.translate(el['content'])} for el in content if el['type'] != 'image']

    # Convert to Markdown
    markdown_converter = Convertmarkdown(content_en, "output.md")
    markdown_content = markdown_converter.convert_to_markdown()
    file_path = markdown_converter.save_to_markdown_file(markdown_content)

    return send_file(file_path, as_attachment=True, download_name="transcription.md")
