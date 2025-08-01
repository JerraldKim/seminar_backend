import json
from django.http import JsonResponse
from .models import Author, Book, BookAuthors  # Make sure this import is correct
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt

@require_GET
def authors(request):
    try:
        authors_list = []

        for author in Author.objects.all():
            authors_list.append({
                "id": author.id,
                "info": f"{author.name} ({author.country})" if author.country else author.name,
            })

        return JsonResponse({"authors": authors_list})
    
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    
@csrf_exempt
def authors_add(request):
    if request.method == 'POST':
        try: 
            data = json.loads(request.body)
            name = data.get('name')
            country = data.get('country', '')
            
            new_author = Author(name=name, country=country)
            new_author.save()

            return JsonResponse({
                'id': new_author.id, 
                'name': new_author.name,
                'country': new_author.country,
            })
        
        except Exception as e:
            return JsonResponse({'error':str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)

from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .models import Author, Book  # Make sure Book is imported

@require_GET
def authors_of_books(request):
    try:
        book_title = request.GET.get('title')  # GET param: ?book_name=...

        if not book_title:
            return JsonResponse({'error': 'Missing book_name parameter'}, status=400)

        # This is your 'SELECT * FROM books WHERE name = book_name LIMIT 1'
        book = Book.objects.filter(title=book_title).first()
        if not book:
            return JsonResponse({'error': 'No book found with that name'}, status=404)

        # book.authors is a reverse ManyToMany or ForeignKey relationship
        author_links = BookAuthors.objects.filter(book_id = book.id)
        author_ids = [link.author_id for link in author_links]

        authors = Author.objects.filter(id__in=author_ids)

        author_list = [{"id": a.id, "name": a.name, "cuntry": a.country} for a in authors]

        return JsonResponse({
            'book': book.title,
            'authors': author_list
        })

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

