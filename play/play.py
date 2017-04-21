import webapp2

form = """
<form method="post">
    What is your birthday?
    <label>
        <input type="text" name="month"> 
    </label>
    <input type="text" name="day">
    <input type="text" name="year">
    <br>
    <br>
    <input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
    def post(self):
        self.response.out.write(form)

app = webapp2.WSGIApplication([('/', MainPage)], 
                                debug=True)
