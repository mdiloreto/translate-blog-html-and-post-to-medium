
"""
   Logical Description: 

  This algorithm will be design to: 
  1. Fetch Posts from the Spanish Blog, 
    a. Get the text. 
    b. get the images.
    c. get the code snippets. 
    d. get the hyperlinks ## NOT this time
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
from googletrans import Translator
import markdown 
import requests
import storage


endpoint = "https://mb-translator-doc-app.cognitiveservices.azure.com/"
credential = AzureKeyCredential("d872d8ad6b8c404581fe3a31b849ff0b")
document_translation_client = DocumentTranslationClient(endpoint, credential)


def get_title(soup):
    try:
        # Find the <main> element with the specified class
        main_tag = soup.find('main', class_='wp-block-group is-layout-flow wp-block-group-is-layout-flow')

        # From the <main> tag, find the <div> with the specific class
        div_tag = main_tag.find('div', class_='wp-block-group has-global-padding is-layout-constrained wp-block-group-is-layout-constrained') if main_tag else None
        # From the <div> tag, find the <h1> with the specific class
        h1_tag = div_tag.find('h1', class_='has-text-align-center alignwide wp-block-post-title') if div_tag else None

        # Extract the text from the <h1> tag
        title_text = h1_tag.get_text(strip=True) if h1_tag else 'Title not found'
        
        return title_text
            
    except requests.HTTPError as e:
        print(f"HTTP Error: {e}")
    except Exception as e:
        print(f"Error: {e}")


def get_headings(soup):
    try:
        h1_tags = soup.find_all(class_='wp-block-heading')

        # List to hold extracted headings
        headings = []

        for h1_tag in h1_tags:
            # Extract text, ignoring text within <span> tags
            heading_text = ''.join(child for child in h1_tag if isinstance(child, str)).strip()
            headings.append(heading_text)

        return headings
                
    except requests.HTTPError as e:
        print(f"HTTP Error: {e}")
    except Exception as e:
        print(f"Error: {e}")


def get_text(soup):
    try:
        main_tag = soup.find('main', class_='wp-block-group is-layout-flow wp-block-group-is-layout-flow')

        # Find all <p> elements
        paragraphs = main_tag.find_all('p')
        # Concatenate the text from each paragraph
        all_text = '\n'.join(paragraph.get_text(strip=True) for paragraph in paragraphs)
        return all_text
    except requests.HTTPError as e:
        print(f"HTTP Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

    
           
def get_img(soup):
    try:

        images = soup.find_all('img')
        image_urls = [img['src'] for img in images if 'src' in img.attrs]

        return image_urls

    except requests.HTTPError as e:
        print(f"HTTP Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
        

def get_code(soup):
    try:
        #get code content
        code_snippet = soup.find_all('code')
          
        return code_snippet
            
    except requests.HTTPError as e:
        print(f"HTTP Error: {e}")
    except Exception as e:
        print(f"Error: {e}")


def publish_to_medium(data):
    token = ""
    user_info = requests.get(f"https://api.medium.com/v1/me?accessToken={token}")
    user_json_info = user_info.json()

    header = {
        "Authorization": f"Bearer {token}"
    }

    article = {
        "title": data["article_name"],
        "contentFormat": "html",
        "content": markdown.markdown(data["article_content"]),
        "canonicalUrl": "",
        "tags": data["article_tags"].split(", "),
        "publishStatus": "draft"
    }

    post_request = requests.post(f"https://api.medium.com/v1/users/{user_json_info['data']['id']}/posts", headers = header, data = article)

    if post_request.status_code == requests.codes.created:
        storage.update_article_publishers(data)


######################## >>>>>>>>> RUN <<<<<<<<<<<< ###############################

                ####### GET URL

# Replace with your desired blog post URL
url = 'https://madsblog.net/2023/11/24/storage-persistente-en-gke/'

                ###### GET CONTENT 

# Fetching the content from the URL
response = requests.get(url)
response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code

                ###### PARSE BS4 CONTENT
                
# Parsing the content with Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

                #### GET ALL FUNCS 

title = get_title(soup)
text = get_text(soup)
images = get_img(soup)
code = get_code(soup)
headings = get_headings(soup)

# print("Text headings:", headings)
print("Text Content:", text)

                ###### TITLE #########

print('Title:', title)

                ###### IMAGES ########

print("Image URLs:", images)

                ###### CODE ##########
                
for code in code:
    lines = code.find_all('span', class_='line')
    code_snippet = '\n'.join(line.get_text() for line in lines)
    print(code_snippet)

                ##### HEADINGS #######
                
# Print all extracted headings
for heading in headings:
    print("Heading:", heading)
