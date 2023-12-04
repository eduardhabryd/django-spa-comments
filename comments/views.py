from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.shortcuts import get_object_or_404
from .models import Comment
from .forms import CommentForm


class CommentListView(ListView):
    model = Comment
    template_name = 'comments/index.html'
    context_object_name = 'comments'
    paginate_by = 25

    def get_queryset(self):
        return (
            Comment.objects
            .filter(parent_comment__isnull=True)
            .order_by('-created_at')
        )


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comments/add_comment.html'
    success_url = reverse_lazy('comment_list')


class CommentReplyCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comments/add_comment_reply.html'
    success_url = reverse_lazy('comment_list')

    def form_valid(self, form):
        parent_comment_id = self.kwargs.get('parent_comment_id')
        parent_comment = get_object_or_404(Comment, pk=parent_comment_id)

        # Save the form to ensure the comment has an ID before adding the many-to-many relationship
        response = super().form_valid(form)

        # Add the parent_comment to the many-to-many relationship
        self.object.parent_comment.add(parent_comment)

        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        parent_comment_id = self.kwargs.get('parent_comment_id')
        context['parent_comment'] = get_object_or_404(
            Comment, pk=parent_comment_id
        )
        return context
