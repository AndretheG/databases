### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?

A database management program for storing information.

- What is the difference between SQL and PostgreSQL?

SQL is language used to store and search through data. PostreSQL uses SQL to store data in a certain manner.

- In `psql`, how do you connect to a database?

\c databasename

- What is the difference between `HAVING` and `WHERE`?

HAVING filers groups in a data table while WHERE filters single rows.

- What is the difference between an `INNER` and `OUTER` join?

Inner join searches for matching data between tables an returns the join result in a new table. Outer joins returns what inner joins returns plus other rows that don't match in the two tables.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?

Left outer returns data from the left table and not the right. Right outer does the opposite.

- What is an ORM? What do they do?

ORM stands for object-relational mapping. ORM allows for object oriented programming between different systems while converting data.

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?

  Server requests don not have to respect single origin policy while AJAX requests do. Server requests keep private keys secret while with AJAX they're in the client browser.

- What is CSRF? What is the purpose of the CSRF token?

CSRF is Cross-site request forgery. The purpose of a CSRF token is prove that individual are indeed themselves making the request and not someone else.

- What is the purpose of `form.hidden_tag()`?

form.hidden_tag() renders all of the hidden input tags and allows certain values to be passed through a hidden field on WTForms.
