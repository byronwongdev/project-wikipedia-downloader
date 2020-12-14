import wikipedia

def searcher(request):
    answer = wikipedia.page(request)
    print("url: "+answer.url)
    print("title: "+answer.title)
    print("content: "+answer.content)
    return 

def length_article():
    return
    
def saver():
    return


if __name__ == "__main__":
    request = "elon"
    searcher(request)