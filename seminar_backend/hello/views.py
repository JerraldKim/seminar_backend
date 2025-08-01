import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

def new_test(request):
    return HttpResponse("New Test!!")

def calculator_add(request):
    try: 
        a = int(request.GET.get('a', 0))
        b = int(request.GET.get('b', 0))
        return HttpResponse(str(a + b))
    except ValueError:
        return HttpResponse("Invalid Input: a and b must be integers.", status=400)

@csrf_exempt
def add_post_json(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            a = int(data.get('a'))
            b = int(data.get('b'))
            return JsonResponse({'result': a + b})
        except Exception:
            return JsonResponse({'error': 'Invalid input'}, status=400)
    else:
        return HttpResponse("Only POST requests allowed.", status=405)
    
@csrf_exempt
def simple_object_json(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = str(data.get('name'))
        age = int(data.get('age'))
        isStudent = bool(data.get('isStudent'))
        if isStudent == True:
            student = 'a student'
        else:
            student = 'not a student'
        sentence = "{0} is {1} years old. He/She is {2}".format(name, age, student)
        return JsonResponse({'result': sentence})

@csrf_exempt
def list_json(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        fruits = list(data.get('fruits'))
        return JsonResponse({"fruits": fruits})

def get_with_time(request):
    author_time_json = request.GET.get('author_time')
    if author_time_json is None:
        return JsonResponse({"error": "Missing 'author_time' parameter."}, status=400)

    try:
        # If author_time_json is a JSON array string, parse it
        author_time = json.loads(author_time_json)
        # If elements are strings, parse them
        if isinstance(author_time, list) and all(isinstance(item, str) for item in author_time):
            author_time = [json.loads(item) for item in author_time]
        results = []
        for info in author_time:
            # Now info should be a dict
            id = info.get("id")
            title = info.get("title")
            author = info.get("author")
            created_at = info.get("createdAt")
            results.append({
                "id": id,
                "title": title,
                "author": author,
                "createdAt": created_at,
            })
        return JsonResponse(results, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
    
@csrf_exempt  # Only for local/test/dev!
def order_echo(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            return JsonResponse(data, safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Only POST allowed"}, status=405)
        
@csrf_exempt
def variable_key_json(request):
    if request.method == 'POST':
        students = json.loads(request.body)
        student_list = list()
        for name, info in students.items():
            student_list.append({"name": name, "age": info.get("age")})
        result = {"students": student_list}
        return JsonResponse(result)
    


# Create your views here.
