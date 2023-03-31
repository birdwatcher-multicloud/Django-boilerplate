from django.test import TestCase
from .models import SampleTest

class SampleTestCase(TestCase):
    def setUp(self):
        SampleTest.objects.create(name = "blabla", description = "test desc")
        SampleTest.objects.create(name = "bla", description = "blablabla")

    def test_description(self):
        object_one = SampleTest.objects.get(name = "blabla")
        object_two = SampleTest.objects.get(name = "bla")

        self.assertEqual(object_one.description, "test desc")
        self.assertEqual(object_two.description, "blablabla")

    def test_name(self):
        object_one = SampleTest.objects.get(name = "blabla")
        object_two = SampleTest.objects.get(name = "bla")

        self.assertEqual(object_one.name, "blabla")
        self.assertEqual(object_two.name, "bla")