from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item,Book

from django.http import JsonResponse



@api_view(['GET'])
def item_list(request):
	if request.method == 'GET':
		items = Item.objects.all()
		data = list(items.values())
		return JsonResponse({'data':data})


@api_view(['POST'])
def item_post(request):
	if request.method == 'POST':
		name = request.data.get('name')
		description = request.data.get('description')
		Item.objects.create(name=name,description=description)
		return JsonResponse({'data':'item succesdfully created'})

		
@api_view(['GET'])
def book_list(request):
	if request.method == 'GET':
		books=Book.objects.all()
		data=list(books.values())
		return JsonResponse({'data':data})
	
@api_view(['GET'])    
def book_id(request,pk):
	if request.method == 'GET':
		print(pk,'hiii')
		#   book_id = pk
		if type(pk)!=int:
			return JsonResponse({'error': 'please give id not str'})

	try:      
		book = Book.objects.get(id=pk)
		book_data = {
					'book_name': book.book_name,
					'book_price': book.book_price,
					'year': book.year
		}
		return JsonResponse({'data': book_data})
	except:
		return JsonResponse({'data': 'id not exist'})
	

@api_view(['GET'])
def book_search(request):
	if request.method == 'GET':
		try:
			book_name=request.get.data('bookname')
			book=book.objects.get(book_name=book_name)
			books=Book.objects.all()
			data=list(books.values())
			return JsonResponse({'data':data})
			book=book.objects.get(book_name=book_name)
		except:
			return JsonResponse({'error': 'Book not found'})	


	




@api_view(['POST'])
def book_post(request):
	if request.method == 'POST':
		

		book_name= request.data.get('book_name')
		book_price=request.data.get('book_price')
		year=request.data.get('year')
		
		if Book.objects.filter(book_name=book_name).exists():
			return JsonResponse({'data': 'Book already exists'})    
		Book.objects.create(book_name=book_name,book_price=book_price,year=year)
		return JsonResponse({'data': 'book added successfully'})
		
			


@api_view(['PUT'])
def book_update(request,pk):
	if request.method == 'PUT':
		# book_id= request.data.get('book_id')
		book_name= request.data.get('book_name')
		book_price=request.data.get('book_price')
		year=request.data.get('year')


		try:
			book_instance = Book.objects.get(id=pk)
			print(book_instance)
			Book.objects.filter(id=book_instance.id).update(book_name=book_name,book_price=book_price,year=year)
			return JsonResponse({'data': 'book updated successfully'}) 
		except:
			return JsonResponse({'data': 'book id does not exist'}) 



		   

@api_view(['DELETE'])    
def book_delete(request,pk):
	if request.method =='DELETE':
		print(pk,'ooooo')

		try:
			book_instance = Book.objects.get(id=pk)
			book_instance = Book.objects.get(id=book_instance.id)
			book_instance.delete()
			return JsonResponse({'data': 'book deleted successfully'})
		except:
			return JsonResponse({'data': 'book does not exit'})



		




