from django.test import TestCase

from .models import Course
from .search import University, searchFacade

# Create your tests here.
# 1 Check for model Representation Invariant
# 2 check for if  views.py successfully add data to model
# 3 check if file exists after upload function.


class Test_db(TestCase):
    def test_verifier(self):
        course = Course.objects.create(
            name="FOCS",
            code="2200",
            university="RPI",
            semster="Fall",
            years="2022",
            test_type="Final",
        )
        course.save()
        course = Course.objects.create(
            name="FOCS2",
            code="2200",
            university="RPI",
            semster="Fall",
            years="2022",
            test_type="Final",
        )
        course.save()
        self.assertEqual(len(Course.objects.all()), 2)
        course1 = Course.objects.get(name="FOCS")
        self.assertEqual(course1.code, "2200")
        self.assertEqual(course1.university, "RPI")
        self.assertEqual(course1.semster, "Fall")
        self.assertEqual(course1.years, "2022")
        self.assertEqual(course1.test_type, "Final")

    def test_db_count(self):
        all_entries = Course.objects.all()
        self.assertEqual(all_entries.count(), 0)

    def test_SearchEngineinit(self):
        engine1 = searchFacade()
        uni = University.objects.create(name="RPI")
        uni.save()
        search_result2 = engine1.search("a_silly_university", "FOCS", "Test")

        self.assertEqual(search_result2, None)
