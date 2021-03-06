###  

### POPULATING OUR DATABASE

Now that we have our database in place, we’ll to populate it with some data. We
can do this by running Django’s **dumpdata** command. Let’s do that now.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
python manage.py dumpdata --natural-foreign -e contenttypes -e auth.Permission --indent=4 > db.json --settings=settings.dev
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   **–natural** will format the JSON in a readable format.

-   **-e** will exclude a model. In this case we’re excluding
    Django’s **contenttypes** and **auth.Permission** models. These are
    generated by Django as soon as the models are generated. If we don’t
    exclude **contenttypes** and **auth.Permission**, we’ll get a duplicate
    entry error when we try loading the data.

-   **–indent** will determine the indentation of the data in the JSON file.

This will dump all our data into a json file in the root directory of our
project. Once that’s done we’ll need to push our **db.json** file up to GitHub.

Once we’ve done that we’ll need to load our data into the staging database with:

heroku run --app YOUR_HEROKU_APP python manage.py loaddata db.json
--settings=settings.staging

You should now be able to log into the admin panel as well as all of the
magazines and products you had in your database.  


### STATIC FILES

The next thing that we need to do is organise all of our static files. For this
step we’re going to use **whitenoise**. Go ahead and add whitenoise
to **requirements/base.txt**:

`whitenoise==3.2`

Once that’s completed, we’ll go ahead and run:

`pip install -r requirements/base.txt`

Next we’ll need to open up our we_are_social/wsgi.py file and change it to the
following:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import os
 
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "we_are_social.settings")
 
application = get_wsgi_application()
application = DjangoWhiteNoise(application)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This will enable Django to load our static files.

That’s it! We have successfully deployed our Django project and our database to
Heroku and ClearDB.
