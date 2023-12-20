from django.shortcuts import render


def post_list(request):
    return render(request, 'archive/post_list.html', {})