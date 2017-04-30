# Blog
## Forms
HTML forms (also web form) are web pages that allow user to enter data that
is sent to a server for processing. `<form></form>` defines a form in HTML
that take a couple of attributes. A complete list of attributes can be found at
[w3schools](https://www.w3schools.com/tags/tag_form.asp).

* `action` specifies where to send the form data when a form is submitted.

A form contains form elements where `<input>` is the most important form element
that can assume different types. It can take a couple of attributes. A complete
list of attributes can be found at
[w3schools](https://www.w3schools.com/tags/tag_input.asp).

* `name` attribute specifies the name of the input element.
* `type` attribute specifies the type of the input element.
* `value` attribute specifies the value of the input element.

```html
<form action="http://www.google.com/search">
    <input name="q"> <!-- defines an input field with name q -->
    <input type="submit"> <!-- defines button to submit the form -->
</form>
```

## Methods - GET and POST
`GET` and `POST` are two different methods for HTTP requests. The `GET` method sends the encoded
user information appended to the page request (separated by the character `&`). The `POST` method
transfer information via HTTP headers. Methods are specified in the form with the attribute `method`.
If the method is not specified it defaults to `GET`.
```
<form method="post" action="./testform"></form>
<form method="get" action="./testform"></form>
```
### Differences (GET vs. POST)
* parameters in URL (`GET`) vs. parameters in body (`POST`)
* used for fetching documents (`GET`) vs. used for updating data (`POST`)
* maximum URL length (`GET) vs. no maximum length (`POST`)
* parameters can be cached (`GET`) vs. parameters are almost never cached (`POST`)
* shouldn't change the server (`GET`) vs. can change the server (`POST`)

## Validation
Validation for user input (e.g., date - day, month, year). 
Validate the day:
```python

def valid_day(day):
    if(day and day.isdigit()):
        day = int(day)
        if(day >= 1 and day <= 31):
            return day

#print valid_day('0') 
# => None    
#print valid_day('1') 
# => 1
#print valid_day('15') 
# => 15
#print valid_day('500') 
# => None
```

Validate the month:
```python
months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

month_abbrv = dict((m[:3].lower(),m) for m in months)
def valid_month(month):
    if(month):
        short_month = month[:3].lower()
        return month_abbrv.get(short_month)

#print valid_month("january") 
#=> "January"    
#print valid_month("January") 
#=> "January"
#print valid_month("foo")
#=> None
#print valid_month("")
#=> None
```

Validate the year:
```python
def valid_year(year):
    if(year and year.isdigit()):
        year = int(year)
        if(year >= 1900 and year <= 2020):
            return year

#print valid_year('0') 
#=> None    
#print valid_year('-11') 
#=> None
#print valid_year('1950') 
#=> 1950
#print valid_year('2000') 
#=> 2000
```




## Google App Engine
[](https://cloud.google.com/appengine/)

The Google Cloud Platform
[provides](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/appengine/standard/hello_world) 
the hello world example. In it the main python file `(./hello_world/main.py)` contains two sections.

```python
import webapp2
class MainPage(webapp2.RequestHandler):
    def get(self): 
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
```

In the section on the bottom, an URL in this case `/` is mapped to a handler called MainPage, 
that in turn is defined in the class MainPage. It inherits from `webapp2.RequestHandler`, 
which is the generic request handler from Google. The class is a function valled `get`, 
which takes a parameter called self. In this example `get` implements the method `GET`. 
Similarly, `post` implements the method `POST`.  This function does two things. 
First, it takes `self.response`, which is the global
response object and sets a header. It sets the content-type header to `text/plain`. By default, the
content type is `text/html`. In the next statement, it writes the string `Hello World`. Google App
Engine can be started through the commandline with `dev_appserver.py hello_world`. `localhost:8080`
serves the live web application that shows `Hello World!` when opened in a browser. Setting the header
as plain text and writing out the self-request itself reveals the header of the HTTP request, that is 
helpful for telling the server where the request came from. On a sitenote,  `Referer` is spelled wrong 
(e.g., Referrer) as it was in the original HTTP specification. But it's lived on for backwards compability
reasons.

```
self.response.headers['Content-Type'] = 'text/plain'
self.response.out.write(self.request)
```
```
GET /testform?q=Hello+World HTTP/1.1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: de-DE,de;q=0.8,en-US;q=0.6,en;q=0.4
Content-Type: ; charset="utf-8"
Host: localhost:8080
Referer: http://localhost:8080/
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36
X-Appengine-Country: ZZ
```

