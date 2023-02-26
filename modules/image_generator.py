from dalle2 import Dalle2

def genarate_image(prompt):
    dalle = Dalle2("")
    generations = dalle.generate(prompt,"+ website heading image")
    header_image_link = generaitons
    return header_image_link