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
        queryset = Comment.objects.filter(parent_comment__isnull=True)

        sort_param = self.request.GET.get('sort', 'created_at')
        order_param = self.request.GET.get('order', 'desc')

        order_by_field = sort_param if order_param == 'asc' else f"-{sort_param}"

        if sort_param == 'user_name':
            queryset = queryset.order_by(order_by_field, 'user_name')
        elif sort_param == 'email':
            queryset = queryset.order_by(order_by_field, 'email')
        elif sort_param == 'created_at':
            queryset = queryset.order_by(order_by_field)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sort_param'] = self.request.GET.get('sort', 'created_at')
        context['order_param'] = 'asc' if self.request.GET.get('order', 'desc') == 'desc' else 'desc'
        return context


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

        response = super().form_valid(form)

        self.object.parent_comment.add(parent_comment)

        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        parent_comment_id = self.kwargs.get('parent_comment_id')
        context['parent_comment'] = get_object_or_404(
            Comment, pk=parent_comment_id
        )
        return context
