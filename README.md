
# A Photo Gallery with Image Rotation
# Create a gallery of images using Django.
- Each image can have tags (eg. -Sketch, Nature, Portrait, Cars, Wildlife…)
- Paginate the pages (max 8 images per page)
- We can filter the images in the gallery by their tags. Selecting a tag or some tags will show only the images with those tags in the gallery.
- Clicking an image in a gallery will take us to a page for that specific image. Two buttons there to rotate the image 90 degrees clockwise or anti-clockwise. 
- (Image is rotated and the resulting image is saved in the media folder replacing the previous(actual) image).

	# Input form to upload new images -
	• Select tag 
	• Select Image
	• Upload Button

# To Run

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver