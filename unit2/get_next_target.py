# if start link not found return (None, 0) tuple
def get_next_target(s):
    start_link = s.find('<a href=')
    if start_link == -1:
        return None,0
    start_quote = s.find('"',start_link)
    end_quote = s.find('"',start_quote+1)
    url = s[start_quote+1:end_quote]
    return url, end_quote

s1 = 'is a private institution of <a href="http://www.wikipedia.org/wiki/Higher_education"> higher education founded by'
s2 = 'good day'
s3 = ''
print(get_next_target(s1))
print(get_next_target(s2))
print(get_next_target(s3))

print(20*'-')

def get_all_links(page):
    while True:
        url, endpos = get_next_target(page)
        if url:
            print(url)
            page = page[endpos:]
        else:
            break


p1 = '<div id="top_bin"><div class="udacity float-left"><a href="http://udacity.com"></div><a href="http://google.com"></div>'
get_all_links(p1)
print(get_all_links('http//xkcd.com'))
