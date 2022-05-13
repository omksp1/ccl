import webapp2
class mainPage(webapp2.RequestHandler):
    def get(self):
        for i in range(1,10):
            self.response.write("5 x %d = %d<br>" % (i, i*5))

app = webapp2.WSGIApplication([('/', mainPage),], debug=True)
