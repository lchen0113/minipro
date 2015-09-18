#!/usr/bin/env python

import webapp2
import os
import jinja2
from google.appengine.api import users

JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions=['jinja2.ext.autoescape'],
	autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
	    template = JINJA_ENVIRONMENT.get_template('templates/index.html')
	    self.response.write(template.render())
#            greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
#                        (user.nickname(), users.create_logout_url('/')))
#            self.response.out.write('<html><body>%s</body></html>' % greeting)
	    
        else:
            greeting = ('<a href="%s">Sign in or register</a>.' %
                        users.create_login_url('/'))
            self.response.out.write('<html><body>%s</body></html>' % greeting)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
