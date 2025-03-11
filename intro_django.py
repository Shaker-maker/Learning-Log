"""
Django is a web framework - a set of tools that help you build interactive websites

build a project called learning log - an online journal system that lets you kee
track of information you've learnt about particular topics


Setting Up a project 

1 . write a spec
2. se a virtual environment in which to build the project


Writing a Spec

A full spec details the project goals, describes the projects functionality, and discusses its appearance
and interfae

aim - to keep you focused and help your project be on scope

my spec

We'll write a web app ccalled Learning log that allows users to log topics they're interested in and to make
journal entries as they learn about each topic. The learning log Home page will describe the site and invite the users to either register and login, a user can create new topics, add new entries and read and edit exixting entries


whenever you create a new model make migrtations to the database to tell Django
to modify the db to store info related to the model


The Django Admin Site - makes it easy to work with our models
here we will set a superuser - a user who has all privileges available on the site

after creating superuser( python manage.py createsuperuser) now you need to register 
model with the admin site




The Django Shelldjango has a shell(Interactive terminal session) we can examine data programmatically

usage python manage.py shell



MAKING PAGES: The Learning Log Home Page

making web page in django consists three stages
1.defining URLS
2 writing vies
3. writing templates

NOTE: You can do the above in any order, but for this project I will follow the above

we'll start by defining a URL pattern - describes how url is laid out. also
tells django what to look for when matching a browser request with site URL so it know which 
page to return


each url then maps to a particular view - view function retrieves and processes data need for the page

view function often renders the page using template, which contains overall structure of the page

"""

