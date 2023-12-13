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
