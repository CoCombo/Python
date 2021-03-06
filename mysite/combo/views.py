from django.shortcuts import render
from combo.models import Category, Page
from combo.forms import CategoryForm
#from django.http import HttpResponse

# Create your views here.
def index(request):
	category_list = Category.objects.order_by('-likes')[:5]
	context_dict = {'categories': category_list}
	
	return render(request, 'combo/index.html', context_dict)

def shit(request):
	context_dict = {'boldmessage': "media!"}
	
	return render(request, 'combo/shit.html', context_dict)
	#return HttpResponse("bull shit.")

def category(request, category_name_slug):
	context_dict = {}
	
	try:
		category = Category.objects.get(slug = category_name_slug)
		context_dict['category_name'] = category.name
		
		pages = Page.objects.filter(category = category)
		
		context_dict['pages'] = pages
		context_dict['category'] = category
	except 	Category.DoesNotExist:
		pass
		
	return render(request, 'combo/category.html', context_dict)

def add_category(request):
	if request.method == 'POST':
		form = CategoryForm(request.POST)

		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print form.errors
	else:
		form = CategoryForm()
	
	return render(request, 'combo/add_category.html', {'form': form})

def add_page(request):
	try:
		cat = 
