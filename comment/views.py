from django.shortcuts import render

from .forms import CommentForm
from .models import Comment
from django.shortcuts import redirect
from django.urls import resolve
from urllib.parse import urlparse

from django.contrib import messages
def add_comment(request):
    if not request.user.is_anonymous:
        comment_form = CommentForm(request.POST)
        comment_form.instance.author_id = request.user.id
        if comment_form.is_valid():
            comment_form.save()
            messages.add_message(request, messages.SUCCESS, "댓글을 작성하였습니다.")
        else:
            messages.add_message(request, messages.WARNING, "Comment Invalid")
    else:
        messages.add_message(request, messages.WARNING, "댓글은 로그인 사용자만 남길 수 있습니다.")

    referer = request.META['HTTP_REFERER']
    return redirect(referer)

def delete_comment(request, pk):
    comment = Comment.objects.filter(pk=pk)
    if comment.exists() and comment[0].author == request.user :
        comment.delete()
        messages.add_message(request, messages.SUCCESS, "댓글을 삭제하였습니다.")
    else:
        messages.add_message(request, messages.WARNING, "댓글을 삭제할 수 없습니다.")

    referer = request.META['HTTP_REFERER']
    return redirect(referer)









