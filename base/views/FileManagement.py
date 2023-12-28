from django.shortcuts import render, redirect
from base.models import PathManager, FolderManager

def add_data(request):
    if request.method == 'POST':
        # Retrieve data from request.POST
        
        # check title value are unique or not.. check user are logged or not
        
        path = request.POST.get('path')
        file = request.FILES.get('file')  # Assuming file is submitted in the form
        category = request.POST.get('category')
        title = request.POST.get('title')
        

        # Create a new data entry
        PathManager.objects.create(
            user_id=request.user,
            path=path,
            file=file,
            category=category,
            title=title
        )
        sample = PathManager.objects.filter(user_id=request.user)
        for i in sample:
            print(i.path,i.file)

        return redirect('list_data')  # Redirect to the list_data view after successful submission

    return render(request, 'file_manager/add_data.html')

def list_data(request):
    data_entries = PathManager.objects.all()
    return render(request, 'file_manager/list_data.html', {'data_entries': data_entries})




def add_folder(request):
    if request.method == 'POST':
        folder_name = request.POST.get('folder_name')
        category = request.POST.get('category')
        path = request.POST.get('path')

        FolderManager.objects.create(
            user_id=request.user,
            FolderName=folder_name,
            category=category,
            path=path
        )

        return redirect('list_folders')  # Redirect to the list_folders view after successful submission

    return render(request, 'file_manager/add_folder.html')

def list_folders(request):
    folders = FolderManager.objects.all()
    return render(request, 'file_manager/list_folder.html', {'folders': folders})
