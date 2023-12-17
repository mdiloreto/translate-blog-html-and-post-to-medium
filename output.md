# Azure AI and Python: Automate HTML Translation and Medium Publishing


This blog post was created automatically using Python and the power of Azure AI Text Translator.
![Image](https://madsblog.net/wp-content/uploads/2023/12/DALL·E-2023-12-16-01.05.38-A-digital-artwork-showcasing-the-Python-logo-and-the-Azure-logo-of-equal-size-with-a-dark-background.-The-logos-are-prominently-displayed-side-by-sid.png)


Translating and publishing content on different platforms can be a tedious and time-consuming process. However, thanks to advances in artificial intelligence and software development, this process can be automated. In this article, we'll explore how Azure AI integration for text translation and post automation in Medium with Python.

This stems from a personal need, as I am currently publishing IT content in both Spanish (on this blog) and English (enen.multiclouds.tech, my Medium blog). After doing this process manually, I sometimes started thinking about automating it. For this, I started exploring a solution using Python and Azure AI.

Although it is a Work In Progress, the Work In Progress has come up with a fairly solid solution to automate almost 100% of the process.

Here's the repository: (you don't have the automatic passage of Links configured yet, ha!, I'll incorporate this functionality soon).

https://github.com/mdiloreto/translate-blog-html-and-post-to-medium
# The Repo


This project, called "translate-blog-html-and-post-to-medium," automates the translation of blog posts into HTML and their publication on Medium. It aims to help bloggers and content creators reach a wider audience by translating and publishing their blogs in different languages.
# Characteristics


* Extracts HTML content from a specified blog post.
* Translate your content using Azure AI Translation services.
* Convert translated content to Markdown format.
* Publish the translated entry on Medium as a draft.



# Translating Blog HTML and Publishing on Medium

# Description


This project, called "translate-blog-html-and-post-to-medium," automates the translation of blog posts into HTML and their publication on Medium. It aims to help bloggers and content creators reach a wider audience by translating and publishing their blogs in different languages.
# Characteristics


* Extracts HTML content from a specified blog post.
* Translate your content using Azure AI Translation services.
* Convert translated content to Markdown format.
* Publish the translated entry on Medium as a draft.



# Prerequisites


* Python 3.x
* Azure AI Translation API Key and Endpoint
* Medium API Access Token



# Installation


Clone the repository:

```
git clone https://github.com/mdiloreto/translate-blog-html-and-post-to-medium
```

Navigate to directory:

```
cd translate-blog-html-and-post-to-medium
```

Install the dependencies:

```
pip install -r requirements.txt
```
# Use


Set the URL in the 'main.py' file on line #16:

```
main.py
```

```
scraper = Scraper('https://madsblog.net/2023/11/24/storage-persistente-en-gke/') # <<<<< <<<<<<<<< SET THE URL
```

Sets the required environment variables for Azure AI and Medium API tokens.

```
$env:AZUREAI_ENDPOINT='' $env:AZUREAI_CREDENTIAL='' <TU_ENDPOINT_AZUREAI><TU_CREDENCIAL_AZUREAI>$env:MEDIUM_ACCESS_TOKEN='<TU_TOKEN_ACCESSO_MEDIUM>'
```

Then, run the scriptmain.py:

```
main.py
```

```
Python main.py
```
# Translate with Azure Text Translator


In this post, we won't focus on each of the parts of the code, but we will take a look at the code used to perform the translation with Azure Text Translator:

```
from azure.ai.translation.document import DocumentTranslationClient
from azure.core.credentials import AzureKeyCredential
import requests, uuid, json

class Translator:
    def __init__(self, endpoint, key):
        self.endpoint = endpoint # Store the endpoint as an instance variable
        self.key = key # Store the key as an instance variable
        self.client = DocumentTranslationClient(endpoint, AzureKeyCredential(key))

def translate(self, text):
        # Your code to translate text
        location = "eastus"
        path = '/translate'
        constructed_url = self.endpoint + path

params = {
            'api-version': '3.0',
            'from': 'is',
            'to': ['en']
        }

headers = {
            'Ocp-Apim-Subscription-Key': self.key,
            'Ocp-Apim-Subscription-Region': location,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

# You can pass more than one object in body.
        body = [{
            'text': text
        }]

try:
            request = requests.post(constructed_url, params=params, headers=headers, json=body)
            request.raise_for_status() # Raise exception for HTTP errors
            response = request.json()

# Assuming response contains the translated text
            return response[0]['translations'][0]['text']
        
except Exception as e:
            print(f"Error during translation: {e}")
            return None
```

1.ClassTranslator: Defines a class in Python to handle text translation.

```
Translator
```

2.Azure AI Imports and Utilities: Uses Azure AI libraries (DocumentTranslationClient,AzureKeyCredential) and standard Python modules (requests,uuid,json) to perform network operations and data handling.

```
DocumentTranslationClient
```

```
AzureKeyCredential
```

```
Requests
```

```
uuid
```

```
json
```

3.Constructor__init__: Initializes the class with variables for the endpoint and Azure AI key, and creates an instance of the DocumentTranslationClient for interaction with Azure AI.

```
__Init__
```

```
DocumentTranslationClient
```

4.Translate Method:

```
Translate
```

* Build the URL for the Azure AI API.
* It prepares the parameters and headers of the HTTP request, includes the API version, the source and target languages, the subscription key, and a unique identifier for the client trace.
* Make a POST request to translate the text, handling the response and possible errors.




5. Response and Exception Handling: Converts the JSON response into translated text and handles exceptions to ensure code robustness.

This class is called from the principalmain.py file:

```
main.py
```

```
from translator_azureai import Translator

## ...
## ...... rest of the code ....# 
## ...

# Check Enviroment Variables
    if not endpoint:
        raise ValueError("No endpoint found in environment variables")
      
if not credential:
        raise ValueError("No credential found in environment variables")
  # Initialize Translator
    translator = Translator(endpoint, credential)
    
# Translate Content
    content_en = []
    print("Translation in progress...") 
    for element in content:
        if element['type'] != 'image': # Skip translation for images
            translated_text = translator.translate(element['content'])
            content_en.append({'type': element['type'], 'content': translated_text})
        else:
            content_en.append(element) # Add images as-is
    print("Translation finished...") 
    
print("Showing translation...") 
    
for element in content_en:
        print(f"{element['type']}: {element['content']}\n")
```

This code snippet performs the following operations:

1.Environment Variable Check: Check if the endpointycredential variables are defined. If they are not present, an error is raised.

```
Endpoint
```

```
credential
```

2.Translator Initialization: Instantiates the Translator class using the endpointycredential variables.

```
Translator
```

```
Endpoint
```

```
credential
```

3. Content Translation: Scroll through a list of content items, translate each element that is not an image using the created translator, and add the results to a new list (content_en).

```
Content
```

```
content_en
```

4. Display of Results: Prints the translated content, showing both the type of element and its translated content.
# Publication to Medium


For publishing to Medium we use the Medium API.

```
import requests

class MediumPublisher:
    def __init__(self, access_token):
        self.base_url = "https://api.medium.com/v1"
        self.headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

def create_post(self, user_id, title, content,):
        url = f"{self.base_url}/users/{user_id}/posts"
        data = {
            "title": title,
            "contentFormat": "markdown",
            "content": content,
            "tags": [],
            "publishStatus": "draft"
        }
        response = requests.post(url, json=data, headers=self.headers)
        return response.json()

def get_user_id(self):
        url = f"{self.base_url}/me"
        response = requests.get(url, headers=self.headers)
        return response.json().get("data").get("id")

```

The code defines the MediumPublisher class to publish content to Medium using its API:

```
MediumPublisher
```

1.Initialization: The class is initialized with an access token and prepares the necessary headers for HTTP requests to the Medium API.

2. Publication of Content:

* create_post: Publish a new article on Medium. It takes the user ID, title, and content of the article, and sends it to Medium using a POST request.
* The post is created in Markdown format and set as a draft.




```
create_post
```

3. Obtaining User ID:

* get_user_id: Obtains the Medium user ID through a GET request to the API.




```
get_user_id
```

This class is called from the principalmain.py file:

```
main.py
```

```
from publish_medium import MediumPublisher

## ...
## ...... rest of the code ....# 
## ...

# Medium publish
    print("Initializing Medium posting...")  
    access_token = os.getenv('MEDIUM_ACCESS_TOKEN')
    if not access_token:
        raise ValueError("No Medium access token found in environment variables")

Medium_publisher = MediumPublisher(access_token)
    
# Get content for the file  
    with open("C:\\Users\\mateo\\OneDrive\\vscode\\py-chatgpt-translate-webpost\\output.md", "r", encoding="utf-8") as file:
        file_content = file.read()
    
markdown_file_path = 'C:\\Users\\mateo\\OneDrive\\vscode\\py-chatgpt-translate-webpost\\output.md'
  # Prepare Medium publish        
    user_id = Medium_publisher.get_user_id()
    title = ""
    for element in content_en:
        if element['type'] == 'title':
            title = element['content']
            break 
    print("Posting content to Medium as Draft...")  
  # Publish
    post = Medium_publisher.create_post(user_id, title, file_content)
    print("Medium post draft was created sucessfully!") 
    
```

1.Initializing the Publication on Medium: Begins with a message indicating that the publication on Medium is being initialized.

2.Obtaining the Access Token: Retrieves the Medium access token from the environment variables. If it can't find the token, it generates an error.

3. Create an Instance to Publish to Medium: Create an instance of MediumPublisher using the access token.

```
MediumPublisher
```

4.Read File Content: Open and read the contents of the Markdown (output.md) file to be published.

```
output.md
```

5. Obtaining the User ID on Medium: Use the instance created to obtain the User ID on Medium.

6. Determining the Title of the Article: Go through the elements of the translated content (content_en) to find and assign the title of the article.

```
content_en
```

7. Publishing to Medium: Call the métodocreate_postde the MediumPublisher instance to publish the read content as a draft on Medium, using the user ID and title obtained.

```
create_post
```

```
MediumPublisher
```

8. Publication Confirmation: Prints a message indicating that the draft publication was successfully created on Medium.

Mateo Di Loreto
