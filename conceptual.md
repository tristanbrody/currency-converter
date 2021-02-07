### Conceptual Exercise

Answer the following questions below:

-   What are important differences between Python and JavaScript?

    -   Python is stricter about throwing errors for invalid or missing data

    -   Python doesn't have an explicit way of declaring constant variables

    -   JavaScript is based on prototypes, while Python is more of a traditional OOP language

-   Given a dictionary like `{"a": 1, "b": 2}`: , list two ways you
    can try to get a missing key (like "c") _without_ your program
    crashing.

    1. Use get method to set a default value in the event the key isn't present
    2. Use a conditional statement to check if the key is in the dictionary

-   What is a unit test?

    -   A unit test tests a discrete module of an application

-   What is an integration test?

    -   An integration test tests an application as a whole, as opposed to specific units.

-   What is the role of web application framework, like Flask?

    -   Flask saves you the work of creating your own server, and provides built-in methods and functionality to easily connect your front-end application to a server.

-   You can pass information to Flask either as a parameter in a route URL
    (like '/foods/pretzel') or using a URL query param (like
    'foods?type=pretzel'). How might you choose which one is a better fit
    for an application?

    -   A route URL is probably more suitable for specific topics, such as existing products, while query parameters are usually used with forms to handle search data.

-   How do you collect data from a URL placeholder parameter using Flask?

    -   The URL placeholder parameter is also added as an argument to the view function, and then you can access the data based on the argument.

-   How do you collect data from the query string using Flask?

-   How do you collect data from the body of the request using Flask?

-   What is a cookie and what kinds of things are they commonly used for?

-   What is the session object in Flask?

-   What does Flask's `jsonify()` do?
