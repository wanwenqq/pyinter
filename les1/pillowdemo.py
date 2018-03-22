# encoding = utf-8

from PIL import ImageGrab


if __name__ == '__main__':
    im = ImageGrab.grab()
    # im.save('a.jpg') 
    im.show()
    print('finished!')
        
