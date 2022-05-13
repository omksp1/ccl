import os
import json
import urllib
import webapp2
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

    def post(self):
        pincode = self.request.get('zipCode')
        if not pincode.isnumeric() or not len(pincode)==6:
            template_values = {
                "error" : "Incorrect Pin Code (String / False Code entered)"
            }
            path = os.path.join(os.path.dirname(__file__), 'index.html')
            return self.response.out.write(template.render(path, template_values))
        url = "http://api.openweathermap.org/data/2.5/weather?zip="+ pincode +",in&appid=6203a485f4932c56612984371d6218e1&units=metric"
        data = urllib.urlopen(url).read()
        data = json.loads(data)
        city = data['name']
        weather = data['weather'][0]['main']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        template_values = {
            "city": city,
            "weather": weather,
            "temperature": temperature,
            "humidity": humidity
        }
        path = os.path.join(os.path.dirname(__file__), 'results.html')
        self.response.out.write(template.render(path, template_values))
        
        
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)