from django.test import SimpleTestCase
from django.urls import reverse, resolve
from post_api.views import *


class TestUrls(SimpleTestCase):
    """test all urls from post_api"""

    def test_all_post_url(self):
        url = reverse('all-post')
        self.assertEqual(resolve(url).func.view_class, PostView)

    def test_post_create_url(self):
        url = reverse('post-create')
        self.assertEqual(resolve(url).func.view_class, PostCreateView)

    def test_post_update_url(self):
        url = reverse('post-update', args=['post_slug', ])
        self.assertEqual(resolve(url).func.view_class, PostUpdateView)

    def test_post_delete_url(self):
        url = reverse('post-delete', args=['post_slug', ])
        self.assertEqual(resolve(url).func.view_class, PostDeleteView)

    def test_day_analytic_url(self):
        url = reverse('day-analytic', args=['2020-07-15', ])
        self.assertEqual(resolve(url).func.view_class, DayLikeAnalyticsView)

    def test_days_analytics_url(self):
        url = reverse('days-analytics', kwargs={'slug1': '2020-07-15', 'slug2': '2020-07-16'})
        self.assertEqual(resolve(url).func.view_class, RangeDaysLikeAnalyticsView)

    def test_post_detail_url(self):
        url = reverse('post-detail', args=['post_slug', ])
        self.assertEqual(resolve(url).func.view_class, PostDetailView)

    def test_add_like_url(self):
        url = reverse('add-like', args=['post_slug', ])
        self.assertEqual(resolve(url).func.view_class, PostAddLikeView)

    def test_delete_like_url(self):
        url = reverse('delete-like', args=['post_slug', ])
        self.assertEqual(resolve(url).func.view_class, PostRemoveLikeView)
