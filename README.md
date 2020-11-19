  **Flickr-Downloader** 

*A GUI programming Interface utility for flickr*

Python 3.6 or more recent version needed. For lower python3 versions, see the end of this readme file.

Download Flickr images(public) of any user across flickr.
  
Firstly get your *API KEYS* & *SECRET KEY*  from [here](https://www.flickr.com/services/api/keys/)

Give user name(display name) and get public photos of that user downloaded.

Install requirements.txt:-

    $ pip install -r requirements.txt
[![](https://img.shields.io/badge/Me-Flickr-blue.svg)](https://www.flickr.com/photos/158180690@N04/)



For python3 versions older than python3.6:

After installing flickr_api by requirements.txt, you'll need to edit one file in it.
Go to your python directory > site_packages > flickr_api > method_call.py
Replace line 144: 
    resp = json.loads(resp.content)
with
    resp = json.loads(resp.content.decode('utf-8'))
