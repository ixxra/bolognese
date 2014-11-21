import httplib2
from bottle import route, run, template, static_file, redirect, response

@route('/')
def index():
    redirect('/app/index.html')


@route('/app/<filepath:path>')
def static(filepath):
    return static_file(filepath, root='app/')


@route('/api/v1/tracks')
def tracks():
    h = httplib2.Http('cache')
    res, content = h.request('http://localhost:5984/local_music/_design/tracks/_view/abstract')
    response.content_type = 'application/json;'
    return content

run(host='localhost', port=8080)
