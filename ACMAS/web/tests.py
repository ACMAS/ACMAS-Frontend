from django.test import TestCase
from web.models import Course

# Create your tests here.
# 1 Check for model Representation Invariant
# 2 check for if  views.py successfully add data to model
# 3 check if file exists after upload function.


class Test_db(TestCase):
    def setUp(self):
        course = Course.objects.create(
            name="FOCS",
            code="2200",
            university="RPI",
            semster="Fall",
            years="2022",
            test_type="Final",
        )
        course.save()	

    def test_verifier(self):
        course = Course.objects.get(name="FOCS")
        self.assertEqual(course.code, "2200")
        self.assertEqual(course.university, "RPI")
        self.assertEqual(course.semster, "Fall")
        self.assertEqual(course.years, "2022")
        self.assertEqual(course.test_type, "Final")


    def test_db_count(self):
        all_entries = Course.objects.all()
        self.assertEqual(all_entries.count(),1)
