from oscar.core.loading import get_model

from ecommerce.courses.tests.factories import CourseFactory
from ecommerce.extensions.api.filters import ProductFilter
from ecommerce.extensions.catalogue.tests.mixins import CourseCatalogTestMixin
from ecommerce.tests.testcases import TestCase

Product = get_model('catalogue', 'Product')


class ProductFilterTests(CourseCatalogTestMixin, TestCase):
    """ Tests for ProductFilter. """

    def setUp(self):
        super(ProductFilterTests, self).setUp()
        self.filter = ProductFilter()

    def test_filter_product_class(self):
        """ Verify the method supports filtering by product class or the parent product's class. """
        course = CourseFactory()
        seat = course.create_or_update_seat('verified', True, 1, self.partner)
        parent = course.parent_seat_product
        product_class_name = self.seat_product_class.name
        queryset = Product.objects.all()

        actual = list(self.filter.filter_product_class(queryset, 'product_class', product_class_name))
        self.assertListEqual(actual, [seat, parent])
