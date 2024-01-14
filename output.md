# Use GCP Cloud Translation API in Python


We continue exploring AI services in different Cloud Providers as our “multi-cloud” mission demands.

In this case we will be calling the GCP translation API “Cloud Translation API” using Python.
![Image](https://madsblog.net/wp-content/uploads/2024/01/GCP_Pyt.png)

## Cloud Translation API


Google Cloud Platform (GCP) Cloud Translation API is a service that allows developers to integrate automatic text translation. It uses Google's machine learning technology to deliver fast and accurate translations between thousands of language pairs.

Versions:

* Cloud Translation API Basic (v2): This is the most established version and offers basic machine translation functionalities. It is ideal for applications that need simple text translations. This version uses Google's machine learning and statistical translation model.
* Cloud Translation API Advanced (v3): This version is newer and offers additional features compared to Basic. It includes automatic language detection, the ability to translate text in formats like HTML while preserving the original formatting, and improved translation quality using Google's latest deep learning models. It also provides features to customize translations and optimize them for specific domains or vocabularies.



## Demo


We will be using the Cloud Translation API in its Advanced version. We will use it to incorporate it into a Python application that will translate the posts using web scraping.
## Enable the API


Firstly, as with all GCP services, we must enable the API.

For this:

* We will search for “translation api” in the general search engine.
* Then we will click on “Cloud Translation API”.



![Image](https://madsblog.net/wp-content/uploads/2024/01/image-29.png)


* If it is not activated, instead of “manage” it will say “Enable” and we must click on this option.
* In our case, it is already enabled.



![Image](https://madsblog.net/wp-content/uploads/2024/01/image-30.png)


* Then we will click on Manage.



## Create Application Default Credentials (ADC)


Now we will create the credentials for the authorization of our API:

* After clicking on Manage, it will take us to the APIs & Services section.
* We will go to the “Credentials” section.
* We will click on “+ Create Credentials”.



![Image](https://madsblog.net/wp-content/uploads/2024/01/image-31.png)


* We will select “Service Account”.



![Image](https://madsblog.net/wp-content/uploads/2024/01/image-32.png)


* We'll give it a name, the ID will autofill, and we'll enter a description.



![Image](https://madsblog.net/wp-content/uploads/2024/01/image-33.png)


* We will give the necessary permissions.
* In this case the minimum permission that we must give will be “Cloud Translation API User”



![Image](https://madsblog.net/wp-content/uploads/2024/01/image-34.png)


* We will not give access to any user to impersonate the SA.



![Image](https://madsblog.net/wp-content/uploads/2024/01/image-35.png)

## Creation of SA Key


Now we will create the Authentication Key for our Service Account:

* We will continue in “APIs & Services”, in the credentials section, we will click on the newly created SA.



![Image](https://madsblog.net/wp-content/uploads/2024/01/image-36-1024x690.png)


* Once in our SA, we will go to the “Keys” section.
* Then, we will click on “Add Key”



![Image](https://madsblog.net/wp-content/uploads/2024/01/image-37.png)


* We will create the KEY in JSON format.



![Image](https://madsblog.net/wp-content/uploads/2024/01/image-38.png)


* The credentials file will download.



![Image](https://madsblog.net/wp-content/uploads/2024/01/image-39.png)


* We must store this file safely.
* In this case we will send it to the repository folder and exclude it from git using the gitignore file.
* This is not recommended for production, it should be stored in a secrets repository.



![Image](https://madsblog.net/wp-content/uploads/2024/01/image-40.png)


* The JSON file of our SA will be the fundamental parameter for the login.



## Login configuration for our code


The GCP connection client will look for the “GOOGLE_APPLICATION_CREDENTIALS” environment variable.

* In this case, we will add it as an environment variable in PowerShell.




```
$env:GCP_PROJECT_ID="<project_id>"
$env:GOOGLE_APPLICATION_CREDENTIALS="<path/to/file.json>"
```
## Python packages


For our code to work we must install the packages required by the libraries to be used.

We install the following PIP packages:




```
pip install google-cloud-translate==2.0.1
pip install --upgrade google-cloud-translate
```

* The step of upgrading the package is essential for its correct functioning.



![Image](https://madsblog.net/wp-content/uploads/2024/01/image-43-1024x318.png)


* If we do not perform the upgrade, the code will not work as expected.



![Image](https://madsblog.net/wp-content/uploads/2024/01/image-44-1024x277.png)

## Python code for the request


We use the following code in our translation module to call the GCP API via Python:

```
from google.cloud import translate

class Translator_gcp:
    def __init__(self, text, project_id):
        self.text = text
        self.project_id = project_id

    def translate_text(self):
        """Translating Text."""

        client = translate.TranslationServiceClient()

        location="global"

        parent = f"projects/{self.project_id}/locations/{location}"

        response = client.translate_text(
            request={
                "parent": parent,
                "contents": [self.text],
                "mime_type": "text/plain", # mime types: text/plain, text/html
                "source_language_code": "en",
                "target_language_code": "en-US",
            }
        )

        # Display the translation for each input text provided
        for translation in response.translations:
            print(f"Translated text: {translation.translated_text}")

        return response.translations[0].translated_text
```

* In this case, in the Return I am using the extraction of the plain translated text of the response. I do this for the purposes of my application.



## Module call in main.py file


To call this module from main.py I use the following block of code:

```
project_id = os.getenv('GCP_PROJECT_ID')
GOOGLE_APPLICATION_CREDENTIALS = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

    content_en = []
    print("2. Translation in progress...")
    for element in content:
        if element['type'] != 'image': # Skip translation for images
            # translated_text = Translator_azure.translate(element['content']) ##Translate Azure AI
            translator_gcp = Translator_gcp(element['content'], project_id) ## Translate with GCP Translation API
            translated_text = translator_gcp.translate_text()
            content_en.append({'type': element['type'], 'content': translated_text})
        else:
            content_en.append(element) # Add images as-is
    print("2. Translation finished...")
```

You can see the complete code at https://github.com/mdiloreto/translate-blog-html-and-post-to-medium
## Code test


Now we test our app:
![Image](https://madsblog.net/wp-content/uploads/2024/01/image-46.png)


The text is translated correctly using the GCP Cloud Transaltion Advanced API :)

Mateo Di Loreto
