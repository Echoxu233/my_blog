from django.shortcuts import render
from .models import Comment
def home_page(request):

    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.POST.get("username")

        comment_obj = Comment.objects.create(
        	comment=comment,
        	user=user
        )




        print(comment * 10)
        return render(request, 'blog/home_page.html', {'comment':comment_obj})

    return render(request, 'blog/home_page.html', {'test': 'Hey this is a test can you see this?'} )
    
# Create your views here.
