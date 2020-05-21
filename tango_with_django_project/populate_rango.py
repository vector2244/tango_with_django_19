import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category,Page

def populate():
    python_pages = [
        {"title": "Official Python Tutorial", "url":"http://docs.python.org/2/tutorial/", "views": 10, "likes": 8},
        {"title":"How to Think like a Computer Scientist", "url":"http://www.greenteapress.com/thinkpython/", "views": 20, "likes": 12},
        {"title":"Learn Python in 10 Minutes", "url":"http://www.korokithakis.net/tutorials/python/", "views": 56, "likes": 65} ]

    django_pages = [
        {"title":"Official Django Tutorial", "url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/", "views": 25, "likes": 23},
        {"title":"Django Rocks", "url":"http://www.djangorocks.com/", "views": 17, "likes": 17},
        {"title":"How to Tango with Django", "url":"http://www.tangowithdjango.com/", "views": 20, "likes": 5} ]

    other_pages = [
        {"title":"Bottle", "url":"http://bottlepy.org/docs/dev/", "views": 40, "likes": 10},
        {"title":"Flask", "url":"http://flask.pocoo.org", "views": 48, "likes": 10} ]

    ashmits_pages = [
        {"title":"guitar", "url":"https://troygrady.com/", "views": 220, "likes": 220},
        {"title":"coding", "url":"https://www.geeksforgeeks.org/", "views": 200, "likes": 200}
    ]

    cats = {"Python": {"pages": python_pages, "views": 86, "likes": 85}, "Django": {"pages": django_pages, "views": 62, "likes": 45}, "Other Frameworks": {"pages": other_pages, "views": 88, "likes": 20}, "ashmit": {"pages": ashmits_pages, "views": 420, "likes": 420} }


    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data["views"], cat_data["likes"])
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"],p["views"],p["likes"])
    
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))

def add_page(cat, title, url, views=0, likes=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.likes=likes
    p.save()
    return p

def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views=views
    c.likes=likes
    c.save()
    return c

# Start execution here!
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
    
