from bs4 import BeautifulSoup
from urllib import FancyURLopener

from django.template import RequestContext
from django.shortcuts import render_to_response

MAP_URL = "http://maps.google.com/?q=%s,%s"
class MyOpener(FancyURLopener):
    version = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20100101 Firefox/15.0.1'

myopener = MyOpener()

def getlink(request):

    """ Handles user entered url and return the resultant page """

    geo_data = []
    html = ""
    if request.method == "POST":
        link = request.POST.get("link")
        if link:
            html = geo_uformat(link)
        if html:
            base_template = "empty_base.html" # Don't want to inherit from 'base.html' while displaying result
        else:
            base_template = "base.html"
        return render_to_response("geolinks.html", {"html": html, "base_template": base_template}, context_instance=RequestContext(request))
    else:
        return render_to_response("404.html", context_instance=RequestContext(request))
        
def geo_uformat(url):

    """ Extracts geo microformats and inserts Google maps links into the page """

    try:
        soup = BeautifulSoup(myopener.open(url).read())
        for geo in soup.find_all('span', 'geo'):
            lat, llong = geo.text.split(';')
            new_tag = soup.new_tag('a')
            new_tag['href'] = MAP_URL % (lat, llong)
            new_tag['style'] = "color: rgb(238,15,15)"
            new_tag.insert(1, "  Map  ")
            geo.insert(1, new_tag)

        html = soup.renderContents()
        return html
    except Exception:
        return None
    
    
