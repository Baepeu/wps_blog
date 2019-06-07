from django.template.loader import render_to_string
from django.contrib.contenttypes.models import ContentType

from django.template import Library
register = Library()

from comment.forms import CommentForm
from comment.models import Comment

@register.simple_tag(takes_context=True)
def show_comment(context, content_type, object_id):
    # 폼 만들기
    content_type = ContentType.objects.get_for_model(content_type)
    form = CommentForm(initial={'content_type':content_type, 'object_id':object_id})

    # 해당 하는 댓글 목록 뽑기
    comments = Comment.objects.filter(content_type=content_type, object_id=object_id).all()

    # 템플릿 렌더링
    return render_to_string('comment/show_comment.html',{'form':form, 'object_list':comments}, request=context['request'])






