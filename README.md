# django-distill-example

This is a complete working example of how to build a static site with Django,
Django Distill and Django CacheKiller. It was built and tested under Python
3.6, but any modern 3.x Python should work.

 * [Django](https://www.djangoproject.com/)
 * [Django Distill](https://github.com/mgrp/django-distill)
 * [Django CacheKiller](https://github.com/mgrp/django-cachekiller)

This site is fully working and a live demo if this sites output is available
here, hosted on Netlify:

https://django-distill-example.m.pr/

This example is slightly unusual in that it commits the SQLite database
with the content into the repository, this is fine for single developer or
small teams, however larger sites with a lot of content should use a secured
external database or you'll end up overwriting each others content edits with
endless merge conflicts.


# Usage

You can use this style of site generation on any platform which supports
continuous deployment, good (and free or low cost) examples being:

 * [Netlify](https://netlify.com/)
 * [GitLab Pages](https://docs.gitlab.com/ee/user/project/pages/)

This example repo includes working demo content and a working Django admin. To
get it working, just clone this repository and install the requirements (using
a virtual env would be a good idea):

```bash
$ pip install -r requirements.txt
```

Then run the development server:

```bash
$ ./manage.py runserver
```

You should be able to access the site on your local development server at [http://127.0.0.1:8000/](http://127.0.0.1:8000/). The admin is at
[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin) and the default
credentials are:

* Username: `blogadmin`
* Password: `blogadmin`

**Note** This is obviously not at all secure, the static site once generated is
secure, however the Django interface is *only* suitable for local development
and content editing on a secure computer. If you want to secure the development
server interface make sure you change the `SECRET_KEY` to something sensible
(and store it in an environment variable).

To build a static website into a `public` directory make sure you have `make`
installed, for example on Debian or Ubuntu systems:

```bash
# May need "sudo" prefix
$ apt install make
```

Then in the project directory just run:

```bash
$ make
```

And you static site will be in the `public` directory.


# Detailed steps to get a site live

1. Go and create an account on [Netlify](https://netlify.com/)
2. Create working Django website with some URLs wrapped by Distill, or clone /
   fork this repo
3. Check that `./manage.py distill-local some-directory` creates a working
   static copy of your site
4. Create a build script for simplicity, see the `Makefile` in this repo for an
   example, make this build script create the site in a directory called
   `public` - you can use a shell script or whatever you like.
5. Make sure you set the correct Netlify runtime, see the `runtime.txt` file in
   this repo for an example. Remember, no trailing line breaks!
6. Link your Netlify account to your GitHub or GitLab or other repo account
7. Create the domain on Netlify using your repo as the source, it will ask you
   for some configuration details. In the "Build command" option put `make` 
   (or whatever your shell script is if you created one instead of a makefile)
   and in the "Publish directory" option put `public`.
8. Click "Deploy site"

After a minute or two your static site should be live! Now every time you
commit some changes, including content into the SQLite database, and do a push
your changes will be automatically deployed live and your static assets will
have their cache-busting tags updated.
