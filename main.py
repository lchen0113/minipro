#!/usr/bin/env python

import webapp2
import os
import jinja2
from google.appengine.api import users
from google.appengine.ext import db

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class Photo(db.Model):
    comment = db.StringProperty()
    date = db.DateTimeProperty(auto_now_add=True)
    creator = db.StringProperty()

#class Stream(db.Model):

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            template = JINJA_ENVIRONMENT.get_template('templates/index.html')
            self.response.write(template.render())
        else:
            greeting = ('<a href="%s">Sign in or register</a>.' %
                        users.create_login_url('/'))
            self.response.out.write('<html><body>%s</body></html>' % greeting)


class Manage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            template = JINJA_ENVIRONMENT.get_template('templates/manage.html')
            self.response.write(template.render())
        else:
            greeting = ('<a href="%s">Sign in or register</a>.' %
                        users.create_login_url('/'))
            self.response.out.write('<html><body>%s</body></html>' % greeting)


class Create(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            template = JINJA_ENVIRONMENT.get_template('templates/create.html')
            self.response.write(template.render())
        else:
            greeting = ('<a href="%s">Sign in or register</a>.' %
                        users.create_login_url('/'))
            self.response.out.write('<html><body>%s</body></html>' % greeting)


class View(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            template = JINJA_ENVIRONMENT.get_template('templates/view.html')
            self.response.write(template.render())
        else:
            greeting = ('<a href="%s">Sign in or register</a>.' %
                        users.create_login_url('/'))
            self.response.out.write('<html><body>%s</body></html>' % greeting)


class Search(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            template = JINJA_ENVIRONMENT.get_template('templates/search.html')
            self.response.write(template.render())
        else:
            greeting = ('<a href="%s">Sign in or register</a>.' %
                        users.create_login_url('/'))
            self.response.out.write('<html><body>%s</body></html>' % greeting)


class Trending(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            template = JINJA_ENVIRONMENT.get_template('templates/trending.html')
            self.response.write(template.render())
        else:
            greeting = ('<a href="%s">Sign in or register</a>.' %
                        users.create_login_url('/'))
            self.response.out.write('<html><body>%s</body></html>' % greeting)


class Social(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            template = JINJA_ENVIRONMENT.get_template('templates/manage.html')
            self.response.write(template.render())
        else:
            greeting = ('<a href="%s">Sign in or register</a>.' %
                        users.create_login_url('/'))
            self.response.out.write('<html><body>%s</body></html>' % greeting)


class AddStream(webapp2.RequestHandler):
    def post(self):
        user = users.get_current_user()
        stream_name = self.request.get("stream_name")
        stream_tags = self.request.get("tags")
        subcribers = self.request.get("requests")
        cover_image_url = self.request.get("cover_image_url")

        if user:
           # streams = (db.GqlQuery('SELECT * FROM'))
            self.redirect('/')
        else:
            greeting = ('<a href="%s">Sign in or register</a>.' %
                        users.create_login_url('/'))
            self.response.out.write('<html><body>%s</body></html>' % greeting)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/manage', Manage),
    ('/create', Create),
    ('/view', View),
    ('/search', Search),
    ('/trend', Trending),
    ('/social', Social),
    ('/add_stream', AddStream)
], debug=True)
