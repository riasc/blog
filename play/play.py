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

months = ["January",
        "February",
        "March",
        "April",
        "Mai",
        "June",
        "July",
        "August",
        "September",
        "Oktober",
        "November",
        "December"]

def valid_month(month):
    if(month):
        short_month = month

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(form)
    def post(self):
        self.response.out.write("Thanks! That's a totally valid day!")

app = webapp2.WSGIApplication([('/', MainPage)], 
                                debug=True)
