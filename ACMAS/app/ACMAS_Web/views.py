<<<<<<< HEAD
import zlib
=======
import os

>>>>>>> main
from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import redirect, render

from .form import CroppedImgForm, CroppedQuestionForm
from .models import CroppedImg, Question, UploadedFile
from .ocr_files import ocr_prototype
from .search import searchFacade
from .upload import createFacade

# When using context, use context_base.copy() to create a copy of this base context, rather than using this directly
context_base = {
    "GOOGLE_ADSENSE_URL": os.getenv("GOOGLE_ADSENSE_URL", default="")
    + os.getenv("GOOGLE_ADSENSE_ID", default=""),
    "GOOGLE_ANALYTICS_ID": os.getenv("GOOGLE_ANALYTICS_ID", default=""),
    "GOOGLE_ANALYTICS_URL": os.getenv("GOOGLE_ANALYTICS_URL", default="")
    + os.getenv("GOOGLE_ANALYTICS_ID", default=""),
}


# ACMAS homepage
def index(request):
    context = context_base.copy()
    return render(request, "index.html", context)


# ACMAS Sitemap.xml file (used for Google Search Console)
def sitemap(request):
    return redirect("static/sitemap.xml")


# ACMAS favicon.ico logo (used for browser tab icon)
def favicon(request):
    return redirect("static/img/favicon.ico")


# Search by question page
def searchByQuestion(request):
    context = context_base.copy()
    question = request.POST.get("question")  # Check to see if a question was entered
    if (
        question is not None and len(question) > 0
    ):  # If a question was entered, ignore file input
        # Do manual question search logic here
        print("Manual question: ", question)
        # Instantiate and get session key
        sessionID = request.session._get_or_create_session_key()
        # Prevent session from client from changing until 20 minutes
        request.session.modified = True
        # If session has no facade, create one
        facade = cache.get(sessionID)
        if facade is None:
            cache.set(sessionID, searchFacade(), 1200)
            facade = cache.get(sessionID)
        # Search with Facade
        files = facade.searchQuestion(question)
        # Save facade state
        cache.set(sessionID, facade, 1200)

        context.update({"files": files, "manual": True})
        return render(request, "search-results.html", context)
    return render(request, "search-by-question.html", context)


def searchByCourse(request):
    context = context_base.copy()
    return render(request, "search-by-course.html", context)


# Utilizes search by course form
def searchResults(request):
    context = context_base.copy()

    # Get input
    school = request.POST.get("school")
    course = request.POST.get("course")
    assignmentType = request.POST.get("type")

    # Check input
    if (
        school is not None
        and course is not None
        and len(school) > 0
        and len(course) > 0
    ):
        print("University:", school)
        print("Course:", course)
        print("Assignment Type:", assignmentType)
        # Instantiate and get session key
        sessionID = request.session._get_or_create_session_key()
        request.session.modified = True
        # If session has no facade, create one
        facade = cache.get(sessionID)
        if facade is None:
            cache.set(sessionID, searchFacade(), 1200)
            facade = cache.get(sessionID)
        files = facade.search(school, course, assignmentType)

        # Save facade state
        cache.set(sessionID, facade, 1200)

        # If the search input was valid
        if files is not None:
            context.update({"files": files, "manual": False})
            return render(request, "search-results.html", context)
    # If input was invalid
    return render(request, "search-results.html", context)


def returnQuery(request):
    context = context_base.copy()

    # Returns to previous query results
    # Getting current session facade
    sessionID = request.session._get_or_create_session_key()
    facade = cache.get(sessionID)

    # If there is no facade default to homepage
    if facade is None:
        return redirect("/")
    # Else return to previous query
    search_type = [False]
    resultsList = facade.getQuery(search_type)
    context.update({"files": resultsList, "manual": search_type[0]})
    return render(request, "search-results.html", context)


def pdfReader(request):
    context = context_base.copy()

    name = request.GET.get("url")
    if "." in name:
        file_extension = name.rsplit(".")[1]
    else:
        file_extension = ""
    if file_extension == "txt":  # If the file is a .txt load by filename
<<<<<<< HEAD
        return render(request, "pdf-reader.html", {"directory": "../mediafiles/" + name})
=======
        context.update({"directory": "../media/" + name})
        return render(request, "pdf-reader.html", context)
>>>>>>> main
    # Else obtain object from session Facade and display file
    sessionID = request.session._get_or_create_session_key()
    facade = cache.get(sessionID)
    # If session expired, or no search by course was made, or recent search does not contain file
    if (
        facade is None
        or facade.getQuery() is None
        or not facade.getQuery().filter(filename=name).exists()
    ):
        # Get file directly
        file = UploadedFile.objects.get(filename=name)
        context.update({"directory": file.file_dir})
        return render(request, "pdf-reader.html", context)
    # Obtain pdf from last search and display
    file = facade.getQuery().get(filename=name)
    context.update({"directory": file.file_dir})
    return render(request, "pdf-reader.html", context)


def uploadFile(request):
    context = context_base.copy()

    school = request.POST.get("school")  # Check to see if a school was entered
    course = request.POST.get(
        "course"
    )  # Check to see if a course name or course code was entered

    if (
        len(request.FILES) != 0
        and school is not None
        and len(school) > 0
        and course is not None
        and len(course) > 0
    ):  # If a school and course were entered, and there is an uploaded file
        assignmentType = request.POST.get("type")
        file = request.FILES["fileUpload"]  # Get the uploaded file
        uploaded_id = createFacade().uploadPdf(school, course, assignmentType, file)
        print("School: ", school, "\nCourse: ", course)
<<<<<<< HEAD
        CroppedImg.objects.all().delete()  # delete all cropped images that may have not been deleted from previous use
        return redirect("crop-file", file_id=uploaded_id, pgcount=0)
    return render(request, "upload-file.html")
=======
    return render(request, "upload-file.html", context)
>>>>>>> main


def get_Cropped_Image(request):
    form = CroppedImgForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return JsonResponse({"message": "works"})
    context = {"form": form}
    return render(request, "cropped-img.html", context)


def crop_uploaded_file(request, file_id, pgcount):
    uploadedfile = UploadedFile.objects.get(id=file_id)
    if ocr_prototype.ending_type(uploadedfile.filename) == "pdf":
        pages = ocr_prototype.png_conversion("." + "/mediafiles/" + uploadedfile.filename)
        tcount = len(pages) - 1
        return render(
            request,
            "crop-pdf.html",
            {"file": uploadedfile, "count": pgcount, "total": tcount},
        )
    return render(request, "crop-uploaded-file.html", {"file": uploadedfile})


def pdf_reader(request, file_id, pgcount, total):
    uploadedfile = UploadedFile.objects.get(id=file_id)
    return render(
        request,
        "crop-pdf.html",
        {"file": uploadedfile, "count": pgcount, "total": total},
    )


def ocr_cropped_files(request, file_id2):
    cropped_imgs = CroppedImg.objects.all()
    for img in cropped_imgs:
        if img.text:
            continue
        img.text = ocr_prototype.ocr_driver("mediafiles/{}".format(img.file))
        img.save()
    context = {"Cimages": cropped_imgs, "file": file_id2}
    return render(request, "all-cropped-imgs.html", context)


def edit_question(request, pk, pk2):
    cropped_img = CroppedImg.objects.get(id=pk2)
    form = CroppedQuestionForm(instance=cropped_img)
    if request.method == "POST":
        form = CroppedQuestionForm(request.POST, instance=cropped_img)
        if form.is_valid():
            form.save()
            return redirect("print-Cropped-Imgs", pk)
    context = {"form": form}
    return render(request, "edit-question.html", context)


def delete_Cropped_Text(request, pk, pk2):
    cropped_img = CroppedImg.objects.get(id=pk2)
    if request.method == "POST":
        cropped_img.delete()
        return redirect("print-Cropped-Imgs", pk)
    return render(request, "delete.html")


def submit_questions(request, file_id):
    uploadedfile = UploadedFile.objects.get(id=file_id)
    for q in CroppedImg.objects.all():
        hashString = str(zlib.crc32(bytes(q.text.encode("utf-8"))))
        Question.objects.create(question=q.text, Answers="", Hash=hashString, filename=uploadedfile.filename)
    CroppedImg.objects.all().delete()
    return redirect("index")


def uploadManually(request):
    context = context_base.copy()

    school = request.POST.get("school")  # Check to see if a school was entered
    course = request.POST.get(
        "course"
    )  # Check to see if a course name or course code was entered
    question = request.POST.get("question")  # Check to see if a question was entered
    answer = request.POST.get("answer")  # Check to see if an answer was entered

    if (
        question is not None
        and len(question) > 0
        and answer is not None
        and len(answer) > 0
        and school is not None
        and len(school) > 0
        and course is not None
        and len(course) > 0
    ):  # If a school, course, question, and answer were entered
        # Do manual question upload logic
        createFacade().uploadText(school, course, question, answer)
    return render(request, "upload-manually.html", context)
