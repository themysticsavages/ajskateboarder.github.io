import requests
import json

# Brief step-by-step explanation
#
# 1 . Fetches repositories and saves as JSON
# 2 . Builds the redirection pages
# 3 . Creates a pretty repo list
# 4 . [FUTURE UPDATE] Pushes all this stuff to this repository

res = json.loads(requests.get('https://api.github.com/users/themysticsavages/repos').text)

names = []
files = []

for i in range(len(res)):
    html = '<p>Redirecting</p> <script type="text/javascript"> window.onload = function() {{ window.location.href = "{}" }}</script>'.format('https://github.com/themysticsavages/{}'.format(res[i]['name']))
    
    files.append('./{}.html'.format(res[i]['name']))
    names.append(res[i]['name'])

    with open('./{}.html'.format(res[i]['name']), 'w') as fh:
        fh.write(html)
    fh.close()

del html
del i

ptags = []
html = "<!doctype html> <link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css' integrity='sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm' crossorigin='anonymous'> <link rel='stylesheet' href='./styles.css'> <br><h2>Literally all my repos</h2><hr class='header'> <div class='bg'></div> <html> "

for i in range(len(res)):
    ptags.append('<a href="./{}"><p>{}</p></a> '.format(files[i], names[i]))

with open('../repositories.html', 'w') as fh: 
    fh.write(html+' '.join(ptags)+'</html>')
