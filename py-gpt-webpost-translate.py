
"""
   Logical Description: 

  This algorithm will be design to: 
  1. Fetch Posts from the Spanish Blog, 
    a. Get the text. 
    b. get the images.
    c. get the code snippets. 
    d. get the hyperlinks
    e. order and format the content (bullets, indentation)
  2. Extract Text for Translation, 
  3. Translate the Text and download the images, 
  4. Save the post, 
  5. Quality Assurance, 
  6. Logging and Monitoring
  7. Connect to English Blog and 
  8. Upload the Post. 
  
"""
import requests
from bs4 import BeautifulSoup
from azure.core.credentials import AzureKeyCredential
from azure.ai.translation.document import DocumentTranslationClient


endpoint = "https://mb-translator-doc-app.cognitiveservices.azure.com/"
credential = AzureKeyCredential("d872d8ad6b8c404581fe3a31b849ff0b")
document_translation_client = DocumentTranslationClient(endpoint, credential)



def get_spanish_post(url):
    try:
        # Fetching the content from the URL
        response = requests.get(url)
        response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code

        # Parsing the content with Beautiful Soup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extracting text content
        # Assuming the main content is within <article> tags
        article = soup.find('div', class_='entry-content alignwide wp-block-post-content has-global-padding is-layout-constrained wp-block-post-content-is-layout-constrained')
        if article:
            text_content = article.get_text(separator="\n", strip=True)
        else:
            text_content = None

        # Extracting image URLs
        # Assuming images are within <img> tags in the article
        images = article.find_all('img') if article else []
        image_urls = [img['src'] for img in images if 'src' in img.attrs]

        return text_content, image_urls

    except requests.HTTPError as e:
        print(f"HTTP Error: {e}")
    except Exception as e:
        print(f"Error: {e}")




# Replace with your desired blog post URL
url = 'https://madsblog.net/2023/11/24/storage-persistente-en-gke/'
text, images = get_spanish_post(url)
print("Text Content:", text)
print("Image URLs:", images)
