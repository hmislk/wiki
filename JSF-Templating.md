# JSF Templating - Developer Documentation

## JSF Templating

JavaServer Faces (JSF) offers a powerful templating system that promotes code reuse and modularity. It uses Facelets as its default templating system, allowing developers to leverage HTML-like templates in their applications.

## JSF Template

A JSF template, often saved with an `.xhtml` extension, serves as a blueprint for web pages, defining their basic layout and structure. The typical JSF template includes placeholders for content that will be defined later.

Here's a simple example of a JSF template:


`<html xmlns="http://www.w3.org/1999/xhtml"`
      `xmlns:ui="http://java.sun.com/jsf/facelets">`
    `<body>`
        `<ui:insert name="content"/>`
    `</body>`
`</html>`

In this template, `<ui:insert name="content"/>` acts as a placeholder for dynamic content.

## JSF Template Client

A JSF template client is a web page that uses a template for its layout. It fulfills the placeholders defined in the template with actual content. 

### HTML / Composition Difference 

In JSF, there are two important tags: `html` and `ui:composition`. 

- `<html>` tag: This is the root tag for an HTML document.
- `<ui:composition>` tag: This Facelets tag defines a template client page. It may optionally reference a template file (`template` attribute) and can contain `<ui:define>` tags to provide content for placeholders.

### Linking Template to Client

To link a template to a client page, you use the `<ui:composition>` tag with a `template` attribute. The `template` attribute's value should be the path to the template file. 

Example:
```xhtml
<ui:composition xmlns="http://www.w3.org/1999/xhtml"
                xmlns:ui="http://java.sun.com/jsf/facelets"
                template="/WEB-INF/templates/basicTemplate.xhtml">
```

## ui:define

`<ui:define>` is a Facelets tag used in a template client to provide content for placeholders (`<ui:insert>` tags) in the template. The `name` attribute should match the name specified in the `<ui:insert>` tag of the template. 

Example:
```xhtml
<ui:define name="content">
    <h1>Welcome to our website!</h1>
</ui:define>
```

## ui:insert

`<ui:insert>` is a Facelets tag used in a template to define a placeholder for content. The `name` attribute identifies the placeholder. A template client can then fill these placeholders with actual content using `<ui:define>` tags.

Example:
```xhtml
<ui:insert name="content"/> <!-- This is a placeholder -->
```
In a template client:
```xhtml
<ui:define name="content">
    <!-- The content here will replace the placeholder in the template -->
</ui:define>
```

Remember, JSF templating system is about building reusable and maintainable UI components and layouts. By mastering `<ui:insert>`, `<ui:define>`, and `<ui:composition>`, you can construct powerful, dynamic web pages.

[Back](https://github.com/hmislk/hmis/wiki)
