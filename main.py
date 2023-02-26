from modules import scrapper
from modules import chatgptBlogCreator
#from modules import image_generator
from modules import printer

preffered_url = "http://localhost:4173"
scrap = scrapper
chatAi = chatgptBlogCreator
#image = image_generator

def func():
    '''Scrap Headlines From Popular Blog Posts'''
    headline = scrap.scrapper(preffered_url)
    '''Create AI Generate Blog Content Using CHATGPT'''
    #blog_content = chatAi.blog_content_creator(headline)
    '''Creates Image Using An AI Sevice'''
    #header_image = image.genarate_image(headline)
    #context ={'blogcontent':blog_content, 'headerimage':header_image}
    name = "marcel"
    surname = "nazare"
    context = {'name':name,'surname':surname}
    return context[surname]

def superbase_db():
    context1 = "None"
    print("hello world")
    return context1


def runner ():
    try:
        printer.printer("Affiliate Blog Program Is Running")
        printer.printer(f"Connecting To URL: {preffered_url}")
        
        superbase_db()
        printer.printer(func())
        printer.printer(superbase_db())

    except Exception as err:
        printer.printer(f"{err}")
    

runner()
