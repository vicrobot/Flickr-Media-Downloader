import flickrapi
import flickr_api
import urllib.request
import requests
import urllib
import time, magic
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
from PIL import Image
from PIL.ImageQt import ImageQt
import os, sys, time
from error import *


### see this:- ###############################
"""
If EOF error in violation of protocol error occurs:-
https://stackoverflow.com/q/33410577/9134528:- This suggests to do this:- $ pip install ndg-httpsclient
"""
class multithread(QThread):
    def __init__(self, obj):
        self.obj = obj
        super().__init__()
    def run(self):
        self.obj()

def caller(x):
    global y            #this and below
    y = multithread(x)  #prevented from garbage collection
    y.start()

def url_list_maker(flickr_obj, uiv):
    """
    Returns a list of urls of all public photos a user has uploaded on flickr.
    User is identified through user id value(uiv) in argument.
    """
    count = 0
    photos = flickr_obj.walk_user(user_id = uiv, per_page = 100, extras = 'url_o')
    url_list = []
    for photo in photos:
        try:
            url_list.append(photo.get('url_o')) # o ->original size; other vars may not have all images.
        except: pass
    return url_list

def preview(img, k1):
    #k1 is the place to visualize the image. 
    filename = img
    pixmap = QtGui.QPixmap(filename)
    pixmap = pixmap.scaled(k1.width(), k1.height(), QtCore.Qt.KeepAspectRatio)
    k1.setPixmap(pixmap)
    k1.setAlignment(QtCore.Qt.AlignCenter)

def message(message, k1):
    k1.setText(message)

def mkname(name):
    """
    Returns a possible non-conflicting name able to be created in current directory.
    """
    num = 0
    name = str(name)
    new_n = name[:]
    old_n = new_n
    while os.path.exists(new_n):
        old_n = new_n
        num += 1
        new_n = name + str(num)
    return(new_n, old_n)

def checkIds(akv, skv, print_M = 0):
    """
    Checks whether the provided keys are correct or not.
    akv is access key, skv is secret key.
    print_M is used for showing a message if keys were wrong.
    """
    flickr_api.set_keys(api_key = akv, api_secret = skv)
    try: flickr_api.Person.findByUserName('vicro_bot').id
    except flickr_api.flickrerrors.FlickrAPIError:
        if print_M: anim_write("Wrong Keys!!", "Try again")
        return 0
    except requests.exceptions.ConnectionError:
        raise NetworkError
    return 1

def anim_write(*string, t = 0.02):
    "AnimationWriter:- Prints iterable in fashion"
    for i in string:
        for j in i:
            print(j, end = '', flush = True)
            time.sleep(t)
        print('')
        time.sleep(0.02)

def input_anim(string, t=0.05):
    anim_write(string)
    return input()

def is_img(st):
    if magic.from_file(os.path.abspath(st), mime = 1).startswith('image'): return True
    else: return False

def download(urls, filename, progressBarObj, imagepreview, cwo, choice = 0, imagecount = 0):
    """
    Downloads files from url and uses filename as starting name for files.
    choice : it is the way of accessing photos(like through tags, user name etc).
    cwo : centralwidgetobject needed for preview
    """
    pgo = progressBarObj
    if choice == 1:
        with open('.temp-logs', 'r+') as var: t_lines = var.readlines()
    counter, b = 0, 0
    k1 = len(urls)
    if k1 == 0:
        return 0
    var = 100.0/(k1*1.0)
    urls = [i for i in urls if i]
    if not urls: return 0
    second, third = '', ''
    for i in urls:
        imagename = '{1}{0}.{2}'.format(imagecount, filename[0], i.split('.')[-1])
        try: urllib.request.urlretrieve( i, imagename)
        except urllib.error.URLError:
            if choice == 1:
                #only for choice == 1 since no need to store urls for search results as they vary.
                with open('.temp-logs', 'w+') as var:
                    var.write(t_lines[0])
                    var.write('imgC {}'.format(imagecount))
                print('\nAbort')
                sys.exit()
            else: print('\nAbort'); sys.exit()
        counter += var
        if is_img(imagename):
            if third: preview(third, imagepreview[2])
            if second:
                preview(second, imagepreview[1])
                third = second
            preview(imagename, imagepreview[0])
            second = imagename
            time.sleep(1)
        imagecount += 1
        pgo.setProperty("value", int(counter))  ##so many errors being produced here
    return 1


def searchnDownload(str1, flickr, typ, pgo, imprev_list, cwo, spb, to_search, api_key_val):
    """ pgo is progressBar object
        imprev_list is  list of image preview places in seq.
        cwo is centralwidget object
        spb is spinBox objecy
    """
    bool_broad = 0 ## pretending that i have bool_broad, have to fix it.
    if typ.lower() == 'tags':
        tags = [i.rstrip() for i in str1.split(',') if i]
        #bool_broad = int(input_anim('You wanna search broad category or strict in tagging?\
        #(1 for former/prior, 0 for later):').rstrip())
        #text = input_anim("Give a general text for search: ").strip()
        nums = int(spb.text().strip())
        if bool_broad == 1:
            t = flickr.tags.getRelated(api_key = api_key_val, tag = tags)
            tags = [[j.text for j in i] for i in t][0]
            if not to_search or to_search == 'both':
                searched_elem = flickr.photos.search(api_key = api_key_val, tags = tags, 
            text = text, accuracy = 1, safe_search = 1, content_type = 1, extras = 'url_o',
            per_page = nums)#int(input_anim('how many images(max 500): ').rstrip())) 
            #there is media argument, per_page and page too. GUI handling needed.
            elif to_search == 'images' or to_search == 'others':
                searched_elem = flickr.photos.search(api_key = api_key_val, tags = tags, 
                accuracy = 1, safe_search = 1, content_type = 1, extras = 'url_o',
            per_page = nums, media = to_search)
        else:
            if not to_search or to_search == 'both':
                searched_elem = flickr.photos.search(api_key = api_key_val, tags = tags,
                accuracy = 1, safe_search = 1, content_type = 1, extras = 'url_o', 
            per_page = nums)#int(input_anim('how many images(max 500): ').rstrip()))
            elif to_search == 'images' or to_search == 'others':
                searched_elem = flickr.photos.search(api_key = api_key_val, tags = tags,
                accuracy = 1, safe_search = 1, content_type = 1, extras = 'url_o', 
            per_page = nums, media = to_search)
        photo_elems = [[j for j in i] for i in searched_elem][0]
        url_list = []
        counter_photo, printed, len_p = 1, False, 0
        for p in photo_elems:
            try:
                dict_ = p.attrib
                md = flickr.photos.getSizes(api_key = api_key_val, photo_id = dict_['id'])
                t1 = [[j.attrib['source'] for j in i][-1] for i in md][0]
                url_list.append(t1)
            except KeyboardInterrupt:
                print('\nAbort')
                sys.exit()
            except:
                printed = False
                anim_write('Error occured in retrieving url, Ignoring')
        #directory work
        v1 = tags[0].split(' ')
        v2 = v1 + ['etcs']
        new_dir, old_dir = mkname('Flickr_Imgs_{}'.format('_'.join([i for i in v2 if i])))
        if not os.path.exists(old_dir):
            os.mkdir(new_dir)
            os.chdir(new_dir)
        else: os.chdir(old_dir)
        downloaded = download(url_list, v1, pgo, imprev_list, cwo, choice = 0)
        return downloaded
        #do stuffs
    elif typ.lower() == 'name':
        user_name = ''.join([i.rstrip() for i in str1.split(',') if i])
        #do stuffs
        try:user_id_val = flickr_api.Person.findByUserName(user_name).id
        except: raise NoUserFound
        #directory work
        new_dir, old_dir = mkname('Flickr_Imgs_{}'.format('_'.join(user_name.split(' '))))
        if not os.path.exists(old_dir):
            os.mkdir(new_dir)
            os.chdir(new_dir)
        else: os.chdir(old_dir)

        imagecount = 0
        if not os.path.exists('.temp-logs'):
            with open('.temp-logs', 'w+') as var:
                urls = url_list_maker(flickr, user_id_val)
                var.write(str(urls))
                var.write('\n')
        else:
            with open('.temp-logs', 'r+') as var:
                lines_urls_lgs = var.readlines()
            try: susp_int= lines_urls_lgs[1].rstrip()[5:]
            except IndexError:
                with open('.temp-logs', 'w+') as var:
                    urls = url_list_maker(flickr, user_id_val)
                    var.write(str(urls))
                    var.write('\n')
                    susp_int = 0
            with open('.temp-logs', 'r+') as var:
                lines_urls_lgs = var.readlines()
            if susp_int: imagecount = int(susp_int) -1
            urls = eval(lines_urls_lgs[0].rstrip())[imagecount :]
        downloaded = download(urls, user_name, pgo, imprev_list, cwo, choice = 1, imagecount = imagecount)
    return downloaded
