

.. index::
   pair: Django test Autocomplete ; Versions
   ! Versions


.. _versions:

=========
Versions
=========

.. seealso::

   - http://keepachangelog.com
   - http://semver.org/


Creating tags from the command line
====================================

To create a tag on your current branch, run this::

    git tag <tagname>

This will create a local tag with the current state of the branch you are on. 
When pushing to your remote repo, tags are NOT included by default. 
You will need to explicitly say that you want to push your tags to your 
remote repo::

    git push origin --tags



Versions
=========

.. toctree::
   :maxdepth: 3
   
   0.1.0/0.1.0
   
