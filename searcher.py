import wikipedia

def searcher(request):
    request_wiki = wikipedia.page(request)
    global search_url
    global search_title
    global search_content
    search_url = request_wiki.url
    search_title = request_wiki.title
    search_content = request_wiki.content
    print("url: "+ search_url)
    print("title: "+ search_title)
    print("content: "+ search_content)
    return 

def length_article(search_url, search_title, search_content):
    print("length of url: "+ str(len(search_url)))
    print("length of title: "+ str(len(search_title)))
    print("length of the content: "+ str(len(search_content)))
    return
    
def article_saver():
    return


if __name__ == "__main__":
    request = "elon"
    searcher(request)
    length_article(search_url, search_title, search_content)