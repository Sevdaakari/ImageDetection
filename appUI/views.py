from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .models import UploadedImage
from .detection import detect_object

def upload_image(request):    
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ImageUploadForm()
    return render(request, 'appUI/home.html', {'form': form})

def success(request):
    path_for_image = None
    detected_objects = None
    if request.method == "GET":
        latest_uploaded_image = UploadedImage.objects.last()
        if latest_uploaded_image:
            path_for_image = latest_uploaded_image.user_image.url
            print(path_for_image)
            detected_objects = detect_object(latest_uploaded_image.user_image.path)
            print(detected_objects)
    return render(request, 'appUI/success.html', {'path_for_image': path_for_image, 'detected_objects': detected_objects})
    
