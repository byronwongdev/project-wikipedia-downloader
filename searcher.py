import wikipedia


# search function
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

# calculate article length function
def length_article(search_url, search_title, search_content):
    print("length of url: "+ str(len(search_url)))
    print("length of title: "+ str(len(search_title)))
    print("length of the content: "+ str(len(search_content)))
    return

# a function to save the article as txt
def article_saver():
    file_object  = open(search_title + ".txt", "w+" , encoding="utf-8") 
    file_object.write(search_content)


requests = ["Calculus", "Deep Learning", "Programmer", "Computer programming"]

def main():
    for request in requests:
        searcher(request)
        length_article(search_url, search_title, search_content)
        article_saver()

if __name__ == "__main__":
    main()