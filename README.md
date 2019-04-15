# Mosaic-Maker

Mosaic Maker is an application which generates mosaic of images. The parameters are given in URL.  See the example

http://adress/mozaika?losowo=Z&rozdzielczosc=XxY&zdjecia=URL1,URL2,URL3...

### Parameters:

- *losowo* - optional parameter. 1 means that order of pictures should be random
- *rozdzielczosc* - resolution of output mosaic
- *URL1,URL2,URL3* - URL of pictures of which will be made mosaic (min 1, max 8 images)

### How to run (The easiest way is to use pyCharm)

1. pip install -r requirements.txt
2. python3 app.py
3. Type in URL
4. **Ctrl+F5 to see result on the page**

