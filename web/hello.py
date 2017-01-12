from os import environ
from cgi import parse_qs, escape

bind = '0.0.0.0:' + environ.get('PORT', '8080')
max_requests = 1000
worker_class = 'gevent'

def application(environ, start_response):

        start_response("200 OK", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(data)))
        ])
       	print(environ['QUERY_STRING'])
        return ([1,2])