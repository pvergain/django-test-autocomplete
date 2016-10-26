
Django test autocomplete
========================

The purpose of this project is to test and document the jquery 
plugins which can be used with Django_ for autocomplete fields.


- Docs: https://django-test-autocomplete.readthedocs.io/en/latest/
- Source: https://github.com/pvergain/django-test-autocomplete

Curently these 3 modules have been tested:

- http://easyautocomplete.com/ (jquery plugin) 
- https://jqueryui.com/autocomplete/ (jquery ui plugin)
- https://github.com/yourlabs/django-autocomplete-light 


.. _Django:  https://www.djangoproject.com/


**Auto-complete is one of the most important aspects of modern web interface**. 

Auto-complete feature is used to provide auto suggestion for users while 
entering input. We can create auto-complete using an AJAX call to make a list 
and display the list using javascript. 
Creating auto-complete with jquery and jquery-ui is the most efficient way of 
creating it.

When using *<select>* you need to retrieve *all* values from the database
before displaying the form. This is a potentially expensive operation
on the server and delays the time when the user see the form.
