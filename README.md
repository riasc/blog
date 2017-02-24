# Blog

## Forms
HTML forms (also web form) are web pages that allow user to enter data that
is sent to a server for processing. `<form></form>` defines a form in HTML
that take a couple of attributes. A complete list of attributes can be found at
[w3schools](https://www.w3schools.com/tags/tag_form.asp).
* `action` specifies where to send the form data when a form is submitted.
A form contains form elements where `<input>` is the most important form
element that can assume different types. It can take a couple of attributes.
A complete list of attributes can be found at
[w3schools](https://www.w3schools.com/tags/tag_input.asp).
* `name` specifies the name of the input element.
```html
<form action="http://www.google.com/search">
    <input name="q"> <!-- defines an input field with name q -->
    <input type="submit"> <!-- defines button to submit the form -->
</form>
```
When submitting the form