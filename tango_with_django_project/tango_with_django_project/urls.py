from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'tango_with_django_project.views.home', name='home'),
                       # url(r'^tango_with_django_project/', include('tango_with_django_project.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       # url(r'^admin/', include(admin.site.urls)),

                       url(r'^rango/', include('rango.urls')),
                       )
"""
#   The added mapping looks for url strings that match the patterns ^rango/. When a match is made the remainder of the url string is then passed onto and handled by rango.urls (which we have already configured). This is done with the help of the include() function from within django.conf.urls. Think of this as a chain that processors the URL string - as illustrated in Figure 2. In this chain, the domain is stripped out and the remainder of the url string (rango/) is passed on to tango_with_django project, where it finds a match and strips away rango/ leaving and empty string to be passed on to the application rango. Rango now tries to match the empty string, which it does, and this then dispatches the index() view that we created.
"""
