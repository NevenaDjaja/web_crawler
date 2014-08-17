# Finds urls in given html string
# Input:  
# s - string containing href (anchor element)
#
# Output:
# url - string, link inside of the href
# end_quote - number, position of the end of the link
#if start link not found return (None, 0) tuple
def get_next_target(s):
    start_link = s.find('<a href=')
    if start_link == -1:
        return None,0
    start_quote = s.find('"',start_link)
    end_quote = s.find('"',start_quote+1)
    url = s[start_quote+1:end_quote]
    return url, end_quote

def get_all_links(page):
    urls = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            urls.append(url)
            page = page[endpos:]
        else:
            break
    return urls
