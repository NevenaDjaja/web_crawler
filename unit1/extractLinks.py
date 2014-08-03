# script that extracts links from the webpage
# assume format: <a href="link.com">some text</a>

# page is the web page file with content in the form of strings

page = ('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')

start_link = page.find('<a href=')
page_url = page[start_link:]
start_quote = page_url.find('"') + 1
end_quote = page_url.find('"',start_quote)
url = page_url[start_quote:end_quote]
print(url)

