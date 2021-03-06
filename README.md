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
which is the generic request handler from Google. The class is a function called `get`, 
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

### Forms with Google App Engine
```python
import webapp2

form="""
<form action="http://www.google.com/search">
	<input name="q">
	<input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
	def get(self);
		self.response.out.write(form)
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)

```

### Handling of the Request Data
The request handler instance can access the request data using its request property. This is initialized 
to a populated Request object by the application. The request object provides a `get()` method that 
returns values for arguments parsed from the query and from POST data. The method takes the argument name 
as its first parameter. 

```python
class MyHandler(webapp.RequestHandler):
    def post(self):
        name = self.request.get("name")
```
By default, `get()` returns the empty string `('')` if the requested argument is not in the request. 
If the parameter `default_value` is specified, `get()` returns the value of that parameter instead of 
the empty string if the argument is not present. If the argument appears more than once in a request, 
`get()` returns the first occurrence. To get all occurrences of an argument as a possibly empty list, 
use `get_all()`.

```python
# <input name="name" type="text" />
name = self.request.get("name")

# <input name="subscribe" type="checkbox" value="yes" />
subscribe_to_newsletter = self.request.get("subscribe", default_value="no")

# <select name="favorite_foods" multiple="true">...</select>
favorite_foods = self.request.get_all("favorite_foods")
for food in favorite_foods:
  # ...<Paste>
```

## Validation, Substitution and Redirection
### Validation
<a href="validation"></a>
Validation for user input from a form (e.g., date - month, day, year). At first, the user makes
a request for the form to the server - this is a `GET` request. Afterwards, the server responds
with the form as html. Finally, the user will make a `POST` request to the server with the data. 
The server will run some validation functions. If the data is valid the server will return a success
html.

1. verify the user's input
2. on error, render form again
3. include error message


### String Substitution
Python allows string substitution. A simple string with a little bit of html `"<b> some bold text </b>"` can be written 
as `"<b> %s </b>" %VARIABLE` in which the content of `VARIABLE` will be substitute for `%s`. 
```python
given_string = "I think %s is a perfectly normal thing to do in public."
def sub1(s):
    return given_string %s

#print sub1("running") 
# => "I think running is a perfectly normal thing to do in public."    
#print sub1("sleeping") 
# => "I think sleeping is a perfectly normal thing to do in public."
```
Likewise, multiple variables can be substituted into a string.
```python
given_string2 = "I think %s and %s are perfectly normal things to do in public."
def sub2(s1, s2):
    return given_string2 %(s1,s2)

#print sub2("running", "sleeping") 
# => "I think running and sleeping are perfectly normal things to do in public."
#print sub2("sleeping", "running") 
# => "I think sleeping and running are perfectly normal things to do in public."
```
Furthermore, the same variable can be substituted multiple times with 
`"text %(NAME)s text" %{ "NAME":value }`. Instead of including just variables at the 
end, a dictionary can be included that maps name to value and `%(NAME)s` can appear 
in the string multiple times and there can be multiple names.
```python
given_string2 = "I'm %(nickname)s. My real name is %(name)s, but my friends call me %(nickname)s."
def sub_m(name, nickname):
    return given_string2 % {"name": name,"nickname": nickname}

#print sub_m("Mike", "Goose") 
# => "I'm Goose. My real name is Mike, but my friends call me Goose."
```

### Redirection
When the html of a successful request is being rendered (see [validation](#validation))
it can't be shared (e.g., link) or reloaded (form needs to be resubmited). Instead of
returning the (success) html a redirect to a different URL allows the user to request
the (success) html (via `GET`) to which the server responds accordingly.
A simple example of validation, string substitution and redirection can be found in the [play folder](./play).

## Templates
[./templates/shoplist_notmpl](./templates/shoplist_notmpl) implements a shopping list with the concept introduced before.
However, this approach has no syntax highlighting for the forms and is error prone as well as hard to maintain. Using
templates can resolve this. A template library is a library to build complicated strings (html) - 
[jinja2](http://www.jinja.pocoo.org). Variable substitution in jinja2 works with just double curly braces 
`{{ variable }}`. Basically, the curly braces mean print. It is the same as typing the print statement in the 
middle of the code. In a similar fashon, statements can be written insides curly brackets and percent signs. 
```python
{% statement %}
output
{% statement end %}
```
An `if`-statement would look like the following. 
Note: statement need to be ended, because there are no whitespaces or indentation to end the statements.
```python
{% if name == "riasc" %}
  Hello, riasc!
{% else %}
  Who are you?
{% endif %}
```
### FizzBuzz
Implementation of a FizzBuzz template that when provided with the variable n prints `FizzBuzz` up to n.
If `n` is divisible by 3 print `Fizz`. If `n` is divisible by 5 print `Buzz`. If `n` is divisible by
3 and 5 print `FizzBuzz`. Otherwise print `n`. At first a new handlerclass is created.
```python 
class FizzBuzzHandler(Handler):
    def get(self):
        n = self.request.get('n',0)
        n = n and int(n)
        self.render('fizzbuzz.html', n = n)
```
FizzBuzzHandler is addressed via `/FizzBuzz` with 
[fizzbuzz.html](./templates/shoplist_tmpl/templates/fizzbuzz.html) implementing the logic.
```python 
app = webapp2.WSGIApplication([('/', MainPage),('/FizzBuzz', FizzBuzzHandler)], debug=True)
```

