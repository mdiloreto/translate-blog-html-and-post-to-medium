from translator_azureai import Translator
from scraper import Scraper
from markdown_ft import Convertmarkdown
from publish_medium import MediumPublisher
import os
# from md_to_html import Md_to_html

## Text Translator

endpoint = os.getenv('AZUREAI_ENDPOINT')
credential = os.getenv('AZUREAI_CREDENTIAL')
# client = TextTranslateionClient(endpoint,credential)


if __name__ == "__main__":
    print("Starting scraping process...")

    scraper = Scraper('https://madsblog.net/2023/11/24/storage-persistente-en-gke/')
    scraper.fetch_content()
    content = scraper.html_process()
       
  # GET content
   
    # for element in content:
    #     if element['type'] == "bullet-list": 
    #         print(f"{element['type']}: {element['content']}\n")

    # Initialize Translator
    translator = Translator(endpoint, credential)
        
    # Translate Content
    content_en = []
    for element in content:
        if element['type'] != 'image':  # Skip translation for images
            translated_text = translator.translate(element['content'])
            content_en.append({'type': element['type'], 'content': translated_text})
        else:
            content_en.append(element)  # Add images as-is
        
    for element in content_en:
        print(f"{element['type']}: {element['content']}\n")
    
  # Convert to Markdown
    markdownfile = "output.md"
    converter = Convertmarkdown(content_en, markdownfile)
    markdown_content = converter.convert_to_markdown()
    converter.save_to_markdown_file(markdown_content)  # Pass the generated markdown content to the method
    
  # Medium publish
    access_token = os.getenv('MEDIUM_ACCESS_TOKEN')
    if not access_token:
        raise ValueError("No Medium access token found in environment variables")

    Medium_publisher = MediumPublisher(access_token)
    
  # Get content for the file  
    with open("C:\\Users\\mateo\\OneDrive\\vscode\\py-chatgpt-translate-webpost\\output.md", "r", encoding="utf-8") as file:
        file_content = file.read()
    
        markdown_file_path = 'C:\\Users\\mateo\\OneDrive\\vscode\\py-chatgpt-translate-webpost\\output.md'
    
#     # Create an instance of the converter class
#     converter = Md_to_html(markdown_file_path)
    
#     # Convert Markdown to HTML
#     html_content = converter.markdown_to_html()
    
#     # Now you can use html_content as needed
#     print(html_content)
        
    user_id = Medium_publisher.get_user_id()
    title = ""
    for element in content_en:
        if element['type'] == 'title':
            title = element['content']
            break 

    post = Medium_publisher.create_post(user_id, title, file_content)
    