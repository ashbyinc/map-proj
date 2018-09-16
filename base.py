import webapp2


class MainPage(webapp2.RequestHandler):
  def get(self):
      self.response.headers['Content type'] = 'text/plain'
      self.response.write('I AM')
      
app = webapp2.WSGIApplication([
     ('/', MainPage),
], debug=True)     
