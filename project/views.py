from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from FocalHUB.models import Post, Like, Comment
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from datetime import timedelta
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, update_session_auth_hash




def signup(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def upload_post(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        description = request.POST.get('description')

        if image:
            post = Post(image=image, uploader=request.user, description=description)
            post.save()
            return redirect('/')
        else:
            return render(request, 'upload.html', {'error': 'Please select an image file.'})
    else:
        return render(request, 'upload.html')


def feed(request):
    posts = Post.objects.all()
    return render(request, 'feed.html', {'posts': posts})

def trending(request):
    period = request.GET.get('period','week')
    if period == 'week':
        sdate = timezone.now() - timedelta(days=7)
    elif period == 'month':
        sdate = timezone.now() - timedelta(days=30)
    elif period == 'year':
        sdate = timezone.now() - timedelta(days=365)
    else:
        sdate = timezone.now() - timedelta(days=7)

    posts = Post.objects.filter(upload_date__gte=sdate).order_by('-likes')
    return render(request, 'trending.html', {'posts': posts})

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user

    like = Like.objects.filter(user=user, post=post).first()

    if like:
        like.delete()
        post.likes -= 1
    else:
        Like.objects.create(user=user, post=post)
        post.likes += 1

    post.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'feed'))





@login_required
def deletepicture(request,post_id):
    if request.method == 'POST':
        try:
            picture = Post.objects.get(id=post_id)
            picture.delete()
            messages.success(request, 'Picture deleted successfully.')
        except Post.DoesNotExist:
            messages.error(request, 'Picture not found.')

    return redirect('usersettings')


@login_required
def usersettings(request):
    if request.method == 'POST':
        # Handle username change functionality
        newUsername = request.POST['new_username']
        password = request.POST['password']

        currentuser = User.objects.get(username=request.user.username)

        if currentuser.check_password(password):
            currentuser.username = newUsername
            currentuser.save()

            update_session_auth_hash(request, currentuser)
            messages.success(request, "Username has been changed!Please log in again to see the changes!")
        else:
            messages.error(request, 'Invalid password. Try again!')

    # Retrieve user posts
    user = request.user
    posts = Post.objects.filter(uploader=user)

    return render(request, 'user_settings.html', {'posts': posts})


@login_required
def writecomment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        commentcont = request.POST.get('comment')
        if commentcont:
            comment = Comment.objects.create(
                post = post,
                user = request.user,
                content = commentcont
            )
    return  redirect('feed')

@login_required
def deletecomment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.post.uploader == request.user:
        comment.delete()
        messages.success(request, "Succesfully deleted comment.")
    else:
        messages.error(request, "Couldn't delete comment!")

    return  redirect('feed')



