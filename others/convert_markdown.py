import pypandoc

# Convert HTML to Markdown
output = pypandoc.convert_file('formatted_html.html', 'md', outputfile="example.md")
