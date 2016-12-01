
.. index::
   pair: Packages ; Django 


.. _django_packages:

===================================================
Django packages
===================================================

.. seealso:: 

   - https://gist.github.com/kyle-eshares/0c30d81c4f8f201a41b916a2dd864b2c#file-values-py
   - https://medium.com/@hansonkd/performance-problems-in-the-django-orm-1f62b3d04785#.qoy9oemyt


>>> Book.objects.values('title', 'author__name')
<QuerySet [{'author__name': u'Nikolai Gogol', 'title': u'The Overcoat'}, {'author__name': u'Leo Tolstoy', 'title': u'War and Peace'}]>

#  Retrieve values as a tuple
>>> Book.objects.values_list('title', 'author__name')
<QuerySet [(u'The Overcoat', u'Nikolai Gogol'),
(u'War and Peace', u'Leo Tolstoy')]>
>>> Book.objects.values_list('title')
<QuerySet [(u'The Overcoat',), (u'War and Peace',)]>

#  With one value, it is easier to flatten the list
>>> Book.objects.values_list('title', flat=True)
<QuerySet [u'The Overcoat', u'War and Peace']>


Homepage
eShares
HomeEducationDesignEngineeringOnboardingHenryUpdates
Next story
How to Land Your First Development Job in 5 Simple Steps

    Share

Recommended by Kyle Hanson and
Go to the profile of Kyle Hanson
Kyle Hanson
Engineer @ eSharesinc.com, Programmer, Functional programming aficionado
Oct 17
Solving Performance Problems in the Django ORM

Django is a wonderful tool which has helped thousands boost their productivity when writing web applications. Like any framework, when you first start out and the data model is simple, things are speedy. When you start adding real-world constraints and the data-model grows in complexity you’ll probably find that the same strategies you used in the beginning won’t be as effective. As you learn more about your problem domain, you need to adapt your code accordingly.

All frameworks require upfront knowledge about how the internals work in order to write high performance code. Django is fast, but sometimes it allows you to unwittingly write slow code.
What to look for

With something as complex like a web application, it is hard to know where to start.

A bottom-up technique to working with the data, starting from where the data lives to how it is displayed, gives a pragmatic approach to debugging performance problems.

    Datastore (missing indexes / data-model)
    Interface to the datastore (the ORM / inefficient queries)
    Displaying / using the data (Views / reports)

The vast majority of performance problems in a web application are related to accessing the database. Unless you are dealing with large amounts of data and know what you are doing, don’t approach the problem thinking about what the Big-O notation is for your View. The overhead of a database call will dwarf the overhead of loops and template rendering. Without first addressing how you are using the database, you can’t move on to fixing other problems.

Django has a detailed summary of how to optimize working with the database. The ORM is large and strategies are needed to build efficient code from the beginning.

When approaching optimization, code can often become unclear. If faced with a choice between a small performance gain or clear code, understandable code should always come first. It takes practice to know where to place the threshold.
Tools

The first step to fixing a problem is being able to identify it. When dealing with the ORM, there are a few things you can do. Understand django.db.connection, which records the queries made with the current connection.

This can be cumbersome and as you make more and more queries, it can be hard to digest the information.

In the shell, use django-exension’s shell_plus command with the --print-sql flag turned on.

With the server, a middleware should run in the background of your DEBUG environment and log queries and point out duplicates. Django-debug-toolbar provides this information in the page itself.
Example Schema

For our examples, we will use a classic author/book schema.
Unexpected Queries

When checking the existence of an author for a book or grabbing the id of the author, it is tempting to want to use the author field directly.

It’s tricky, but if the author object isn’t needed, you potentially made an extra query for nothing. If you use the author value later, it doesn’t have an impact. A good habit is to play it safe and always use the column name attribute.
Size and Existence

Knowing when to use count and exists is tough. Django caches querysets, so when you are using the data of the queryset, use the built-in python operations. When not using the data, use the queryset methods.

The same holds true when you need the size of the queryset. If you are using the queryset, use len. If you only need the size use count.
Getting only what you need

By default, Django requests all the managed columns of the table and populates a Python object. When you only need a subset of columns from the table, consider using values and values_list. These methods skip the step of creating a complex python object and instead use dicts, tuples or even plain values. They can even handle getting columns through relationships straight forward.
Handling many rows

When you evaluate a queryset, Django caches the values. This makes sense if you will iterate over the queryset multiple times, but it doesn’t make sense in an instance where you loop through once.

What Django actually does is load all books into memory and then iterate through each one. We want Django to hold the SQL connection open and read each row and call do_stuff before reading the next row. iterator to the rescue!

An added benefit of the iterator, is that it allows you to write linear data like table or a CSV as a stream. You can write a file or serve content to a user incrementally.

This is especially powerful when combined with values and values_list, because it keeps the minimum amount of information in memory as possible.

Using iterator also comes in handy during migrations where you need to mutate every row in a table. Just because the migration isn’t client facing doesn’t mean you should slack when it comes to efficiency. A long running migration could mean transaction locks or downtime.
Relationship Problems

Django’s ORM allows you to interact with a relational database in a way that feels natural for the Object-Oriented Python programming language.

The code is precise code and semantically clear. Django uses lazy loading to only load the author if you need it. This is great, but can lead to an explosion of queries.

Django recognizes the problem and provides select_related and prefetch_related to solve it.

Using prefetch_related and select_related is critical when writing a Django app.

A caveat to prefetch_related is that if you plan on filtering the related queryset (author.books.filter(..)) the cache populated by prefetch_related won’t be used and you will have to use a Prefetch object. Sometimes things can get complex and you might better off making 2 queries, one for the parents and one for the children, and then grouping the children by the parent. If your prefetch plans get too complicated, evaluate how much you value the speed boost compared to making slightly less efficient but clearer code.
When select_related doesn’t help

It is tempting to throw a select_related on everything, but there are certain circumstances that don’t make sense. See the following result of the query. id in python gives you the unique id of an object instance. Objects with the same id value are the same instance.

You can be doing more work than needed. select_related creates a new instance for each row of the query, consuming memory. SQL also returns duplicate information for each row. If you are making a query where all the values of your select_related are the same, you’ll want to use something else. Use related querysets or flip the query and use prefetch_related.

With the related queryset author.books.all(), Django caches the value of the author for each book using the same instance of the already queried value.

A hidden side affect is that if you use select_related and alter an author instance, that change won’t propagate to the other authors in the queryset (even if they represent the same row) because they are different instances in python memory. With related querysets, the changes will propagate.
Easier doesn’t always mean better

Django makes following relationships too easy. This results in functions that cannot manage their own side-effects. When you pass in a model instance to a function and use a relationship, it is practically impossible to know if the relationship has already been fetched.

Will either author_name_length or process_author_books make a query? We can’t tell. The relationship features of the ORM are so enticing that it’s natural that we would want to write code this way. Using these functions without a select_related or prefetch_related in a loop can accidentally result in hundreds of queries. Django will happily make the queries without saying a peep. It is up to you to monitor your SQL logs and the callers of the function to figure out if it should pre-fetch or not.

We can rewrite our functions to be explicit by passing in a flattened data-structure that isn’t a model (like a namedtuple), but we shouldn’t have to think about it.
How do we fix it?

Knowing that we have this problem, how can we extend Django to be more explicit about resource consumption? Many database wrappers have solved this in different ways. In Ecto, the DB wrapper for Elixir, an unfetched relationship returns a Ecto.Association.NotLoaded struct instead of implicitly making the query.

Lets imagine a version of Django that implemented this behavior in a pythonic way.

An implementation can be relatively minimal.
Conclusion

There isn’t a one size fits all answer to utilizing the ORM. Most of the time the performance gains for small apps won’t make much of a difference. You should first seek to make your code clear and then work on optimizing it. As your app grows, it is important to practice good hygiene when working with the ORM. Developing good habits now regarding consumption of resources will lead to big benefits later.

Optimization is a lot to handle, but a few simple rules can go a long way.

    Make a habit of isolating code and recording the queries it produces
    Queries should not be in loops
    Understand how the ORM caches data
    Know when Django will make a query
    Don’t over-optimize at the expense of clarity

ProgrammingWeb DevelopmentDjango
Go to the profile of Kyle Hanson
Kyle Hanson


