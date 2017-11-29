# coding = utf-8

import requests
import os



if __name__ == '__main__':
    print ('enter')
    # url = 'http://e.hiphotos.baidu.com/image/pic/item/f603918fa0ec08faa572156d50ee3d6d54fbda8e.jpg'
    url = 'https://python123.io/ws/demo.html'
    root = 'E://project//pic//'
    path = root + url.split('/')[-1]
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url)
            with open(path,'wb') as f:
                f.write(r.content)
                f.close()
                print('save file ok')
        else:
            print('save exits')

    except:
        print('file except')


