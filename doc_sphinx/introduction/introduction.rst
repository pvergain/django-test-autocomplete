
.. index::
   pair: Autocomplete ; definitions 


.. _auto_intro:

=======================================================================
Autocomplete introduction 
=======================================================================

.. contents::
   :depth: 3
   
   
Definitions
============
 
Definition 1
-------------

.. seealso::    

   - http://blog.appliedinformaticsinc.com/autocomplete-input-field-in-django-template-with-jquery-ui/

 
**Auto-complete is one of the most important aspects of modern web interface**. 

Auto-complete feature is used to provide auto suggestion for users while 
entering input. We can create auto-complete using an AJAX call to make a list 
and display the list using javascript. 
Creating auto-complete with jquery and jquery-ui is the most efficient way of 
creating it.


Definition 2
-------------

.. seealso::

   - http://api.jqueryui.com/autocomplete/
   - http://api.jqueryui.com/autocomplete/#option-source
   

You can pull data in from a local or remote source: Local is good for small 
data sets, e.g., an address book with 50 entries; remote is necessary for 
big data sets, such as a database with hundreds or millions of entries to 
select from. 
To find out more about customizing the data source, see the documentation for 
the `source option`_.


.. _`source option`:  http://api.jqueryui.com/autocomplete/#option-source
   
   

Arguments
==========

When using *<select>* you need to retrieve *all* values from the database
before displaying the form. This is a potentially expensive operation
on the server and delays the time when the user see the form.

    


