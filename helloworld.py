import cherrypy
import os
import urllib
import oauth2 as oauth


consumer_key = 'Ma6HbYAcfiwSZ3yldpYLIkrtk'
consumer_secret = '9SXotYYcjFKwIZJpptEOlX7zOOvKTe8Js3Unra130EIorTD8Mm'

request_token_url = 'https://api.twitter.com/oauth/request_token'
access_token_url = 'https://api.twitter.com/oauth/access_token'
authorize_url = 'https://api.twitter.com/oauth/authorize'

    
class HelloWorld(object):
    def index(self):
        consumer = oauth.Consumer(consumer_key, consumer_secret)
        client = oauth.Client(consumer)
        
        resp, content = client.request(request_token_url, "GET")
        if resp['status'] != '200':
            raise Exception("Invalid response %s." % resp['status'])
            
        request_token = dict(urllib.parse.parse_qsl(content))
        print ("Request Token:")
        print (" - oauth_token        = %s" % request_token[b'oauth_token'])
        print ("    - oauth_token_secret = %s" % request_token[b'oauth_token_secret'])
        print ("")
        
        
        # Step 2: Redirect to the provider. Since this is a CLI script we do not 
        # redirect. In a web application you would redirect the user to the URL
        # below.

        print ("Go to the following link in your browser:")
        print ("%s?oauth_token=%s" % (authorize_url, request_token[b'oauth_token']))
        print ("")
        
        
        
        return "<br/><p><a href='"+authorize_url+"?oauth_token="+request_token[b'oauth_token']+"' > Click here to login</a></p> "
    index.exposed = True
    
    def generate(self):
        return "Generate page"
    generate.exposed=True

cherrypy.config.update({'server.socket_host': '0.0.0.0',})
cherrypy.config.update({'server.socket_port': int(os.environ.get('PORT', '5000')),})
cherrypy.quickstart(HelloWorld())
