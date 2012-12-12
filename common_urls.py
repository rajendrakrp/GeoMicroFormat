from django.conf.urls.defaults import *
from core.models import Post

post_info_dict = { 
                  'queryset': Post.live.all(),
                  'date_field': 'date',
                 }

urlpatterns = patterns('django.views.generic.date_based',
                      (r'^$', 'archive_index', dict(post_info_dict, template_name="post_index.html"), 'blog_post_archive_index'),
                      (r'^(?P<year>\d{4})/$', 'archive_year',
                       dict(post_info_dict, template_name="post_archive_year.html", make_object_list=True), 'blog_post_archive_year'),
                      (r'^(?P<year>\d{4})/(?P<month>\w{3})/$', 'archive_month',
                       dict(post_info_dict, template_name="post_archive_month.html"), 'blog_post_archive_month'),
                      (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$', 'archive_day',
                       dict(post_info_dict, template_name="post_archive_day.html"), 'blog_post_archive_day'), 
                      (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'object_detail',
                       dict(post_info_dict, template_name="post_detail.html"), 'blog_post_detail'),
)

                       
                       
    

