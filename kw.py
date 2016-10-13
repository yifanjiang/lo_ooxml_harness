#!/usr/bin/evn python

import json, hashlib
from haralyzer import HarPage

def _save(f, is_encoded=True):

    url = f['request']['url']
    f_ext = f['response']['content']['mimeType'].rsplit('/', 1)[1]
    
    # ugly hack, js in the HAR uses image's file name as the index of the user customized sentences
    if f_ext == "jpg" or f_ext == "jpeg" or f_ext == "png":
        f_nam = url.split('?', 1)[0].rsplit('/', 1)[-1]
    else:
        f_nam = '.'.join([hashlib.sha1(url).hexdigest(), f_ext])

    with open(f_nam, "wb") as fn:
        if is_encoded:
            fn.write(f['response']['content']['text'].decode('base64')) 
        else: fn.write(f['response']['content']['text'].encode('utf-8').strip())

    return f_nam

with open('har', 'r') as f:
    har_page = HarPage('page_1', har_data=json.loads(f.read()))

for f in har_page.html_files:
    html = f['response']['content']['text']
    break

for f in har_page.image_files:
    fn = _save(f)
    html = html.replace(f['request']['url'], fn)

for f in har_page.css_files:
    fn = _save(f, False)
    html = html.replace(f['request']['url'], fn)

for f in har_page.js_files:
    fn = _save(f, False)
    html = html.replace(f['request']['url'], fn)

# for f in har_page.audio_files:
#     print f['request']['url']

# TODO lookinto the conversion: http://stackoverflow.com/questions/25575575/what-do-i-do-with-har-information
print html.encode('utf-8').strip()
