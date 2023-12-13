import markdown

class Md_to_html:
    def __init__(self, file_path):
        self.file_path = file_path 
        
   # Function to read markdown file content and convert it to HTML
    def markdown_to_html(file_path):
        
        with open(file_path, 'r', encoding='utf-8') as file:
            markdown_content = file.read()
        html_content = markdown.markdown(markdown_content)
        return html_content