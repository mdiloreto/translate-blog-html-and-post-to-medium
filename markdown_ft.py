
class Convertmarkdown:
    def __init__(self, content, filename):
        self.content = content
        self.filename = filename
    
    
    def process_bullets(self, bullet_content):
        bullet_points = bullet_content.split('\n')
        markdown_bullets = ""
        l = 0
        for point in bullet_points:
            if l == 0:
                markdown_bullets += f"* {point}"
            # Determine the indentation level (assumes 2 spaces per indent level)
                l = l+1
            else:
                indentation_level = '   ' * (point.count("   "))  # Counting double spaces for each indent level
                formatted_point = point.strip()
                if formatted_point:
                    markdown_bullets += f"{indentation_level}- {formatted_point}\n" # <---- Here we set the bullet type. 
                l = l+1
            l = l+1
        return markdown_bullets
    
    # def process_bullets(self, bullet_content):
    #     bullet_points = bullet_content.split('\n')
    #     markdown_bullets = ""
    #     l = 0
    #     for point in bullet_points:
    #         # Count leading spaces to determine the level of indentation
    #         indentation_level = (len(point) - len(point.lstrip(' '))) // 2
    #         formatted_point = point.lstrip()
    #         if formatted_point:
    #             markdown_bullets += f"{'  ' * indentation_level}- {formatted_point}\n"
    #     return markdown_bullets

        
    def convert_to_markdown(self):
        
        markdown_content = ""
        for element in self.content:
            if element['type'] == 'heading':
                markdown_content += f"# {element['content']}\n\n"
            elif element['type'] == 'paragraph':
                markdown_content += f"\n{element['content']}\n"
            elif element['type'] == 'image':
                markdown_content += f"![Image]({element['content']})\n\n"
            elif element['type'] == 'code':
                markdown_content += f"\n```\n{element['content']}\n```\n"
            elif element['type'] == 'bullet-list':
                markdown_content += self.process_bullets(element['content']) + "\n"
                markdown_content += "\n"
                
        return markdown_content
    


    def save_to_markdown_file(self, markdown_content):
        with open(self.filename, 'w', encoding='utf-8') as file:
            file.write(markdown_content)