from django.shortcuts import render

from api import models
from api.models import Post
from api.serializers import PostListSerializer
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def post_lists(request):
    if request.method == 'GET':
        p_lists = Post.objects.all()
        serializer = PostListSerializer(p_lists, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        p_list = json.loads(request.body)
        serializer = PostListSerializer(data=p_list)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)


@csrf_exempt
def post_list(request, pk):
    try:
        p_list = models.Post.objects.get(id=pk)
    except models.Post.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)

    if request.method == 'GET':
        serializer = PostListSerializer(p_list)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = PostListSerializer(instance=p_list, data=data)
        if serializer.is_valid():
            serializer.save()
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        p_list.delete()
        return JsonResponse({})
