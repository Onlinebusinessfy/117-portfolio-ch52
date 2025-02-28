from django.shortcuts import render, redirect
from .models import Project
from django.views.generic import ListView
from .forms import ProjectForm

# Create your views here.
# def project_list_view(request):
#     my_projects=Project.objects.all()
#     return render(request, "content/project_list.html", {"projects": my_projects})

class ProjectsListView(ListView):
    model=Project
    template_name="content/project_list.html"
    context_object_name="projects"

def project_new_view(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("project_list")
    else:
        form = ProjectForm()

    return render(request, "content/project_new.html", {"form": form})