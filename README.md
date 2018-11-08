# django-distill-example

This is a complete working example of how to build a static site with Django,
Django Distill and Django Cachekiller. It was built and tested under Python
3.6, but any modern 3.x Python should work.

This site is fully working and a live demo if this sites output is available
here:

https://django-distill-example.m.pr/


# Usage

You can use this style of site generation on any platform which supports
continuous deployment, good (and free or low cost) examples being:

  * [Netlify](https://netlify.com/)
  * [GitLab Pages](https://docs.gitlab.com/ee/user/project/pages/)

This example repo includes working demo content and a working Django admin. To
get it working, just clone this repository and install the requirements:

```bash
$ pip install -r requirements.txt
```

Then run the development server:

```bash
$ ./manage.py runserver
```

You should be able to access the site on your local development server at [http://127.0.0.1:8000/](http://127.0.0.1:8000/). The admin is at
`[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin) and the default
credentials are:

* Username: `blogadmin`
* Password: `blogadmin`

*Note* This is obviously not at all secure, the static site once generated is
secure, however the Django interface is *only* suitable for local development
and content editing.


# Detailed example to put get site live

1. Go and create an account on Netlify
2. Create working Django website with some URLs wrapped by Distill
3. Check that `./manage.py distill-local some-directory` creates a working
   static copy of your site
4. Create a build script for simplicity, see the `Makefile` in this repo for an
   example, make this build script create the site in a directory called
   `public`
5. Link your Netlify account to your GitHub or GitLab or other repo account
6. Create the domain on Netlify using your repo as the source
7. In the domain details in Netlify, enter the directory as `public` and the
   build command as `make`
8. Click done

After a minute or two your static site should be live!
