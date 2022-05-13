import webapp2
class MainPage(webapp2.RequestHandler):
    def get(self):
        for i in range(10):
            self.response.write("Omkar T190058674 IT" + '<br>')
        
        
app = webapp2.WSGIApplication([('/', MainPage),], debug=True)