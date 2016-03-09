def app(environ, start_response):
    response_status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(response_status, response_headers)
    resp = environ['QUERY_STRING'].split("&")
    return ["\n".join(resp).encode('utf-8')]
