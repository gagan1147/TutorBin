from django.shortcuts import render,redirect
from .models import Category, Photo
from PIL import Image
import os,time
from django.core.paginator import Paginator

# Create your views here.
def gallery(request):
    
    category = request.GET.get('category')

    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)

    paginator = Paginator(photos, 8) # Show 8 Photos per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    '''
    for photo in page_obj:
        print(photo.category.all())
    '''
    categories = Category.objects.all()

    return render(request,"gallery.html",{'categories':categories, "photos":page_obj})

def view_photo(request,pk):
    base_url = os.getcwd()
    base_url = base_url + '/static'
    photo = Photo.objects.get(id=pk)
    photo_url = base_url+photo.image.url
    photo_name = photo.image.url[8:]
    ID = photo.id
    CAT = photo.category
    

    if request.method == 'POST':
        data = request.POST
        
        try:
            if data['left'] == '270':
                print(data['left'])
                print(photo_url)
                Photo.objects.filter(id=photo.id).delete()
                rotate_img(photo_url,270)
                print(photo_name)
                Photo.objects.create(category=CAT,id=ID,image=photo_name)
                #photo = Photo.objects.get(id=photo.id)
                #return redirect('gallery')

        except:
            print(data['right'])
            print(photo_url)
            Photo.objects.filter(id=photo.id).delete()
            rotate_img(photo_url,90)
            print(photo_name)
            Photo.objects.create(category=CAT,id=ID,image=photo_name)
            #photo = Photo.objects.get(id=photo.id)
            #return redirect('gallery')
    


    return render(request,"photo.html",{'photo':photo})

def add_photo(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['new_category'] != '':
            category, created = Category.objects.get_or_create(
                name=data['new_category'])
        else:
            category = None

        Photo.objects.create(
                category=category,
                image=images,
            )

        return redirect('gallery')
    
    return render(request,"add.html",{'categories':categories})



def rotate_img(image_path,angle):
    image = Image.open(image_path)
    image_out = image.rotate(angle)
    time.sleep(2)
    image_out.save(image_path)