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

```html
<form action="http://www.google.com/search">
    <input name="q"> <!-- defines an input field with name q -->
    <input type="submit"> <!-- defines button to submit the form -->
</form>
```

## Google App Engine
[](https://cloud.google.com/appengine/)

The Google Cloud Platform
[provides](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/appengine/standard/hello_world) the hello world example. In it the main python file `(./hello_world/main.py)` contains two sections.

```python
import webapp2
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
```

In the section on the bottom, an URL in this case `/` is mapped to a handler called MainPage, that in
turn is defined in the class MainPage. It inherits from `webapp2.RequestHandler`, which is the generic request handler from Google. The class is a function valled `get`, which takes a parameter
called self. This function does two things. First, it takes `self.response`, which is the global
response object and sets a header. It sets the content-type header to `text/plain`. By default, the
content type is `text/html`. In the next statement, it writes the string `Hello World`. Google App
Engine can be started through the commandline with `dev_appserver.py hello_world`. `localhost:8080`
serves the app that shows `Hello World!` when opened in a browser.



