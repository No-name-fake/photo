from django.views.generic import ListView, CreateView, DetailView, DeleteView, TemplateView, FormView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.contrib import messages
from .forms import PhotoPostForm, ContactForm
from .models import PhotoPost
from django.shortcuts import render
from django.core.paginator import Paginator
from .utils import get_local_images

class IndexView(ListView):                                  #index
    template_name = 'index.html'
    queryset = PhotoPost.objects.order_by('-posted_at')
    paginate_by = 9

@method_decorator(login_required, name='dispatch')          #post
class CreatePhotoView(CreateView):
    form_class = PhotoPostForm
    template_name = 'post_photo.html'
    success_url = reverse_lazy('photo:post_done')

    def form_valid(self, form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)

class PostSuccessView(TemplateView):                        #post後のやつ
    template_name = 'post_success.html'

class CategoryView(ListView):                               #カテゴリ
    template_name = 'index.html'
    paginate_by = 9

    def get_queryset(self):
        category_id = self.kwargs['category']
        return PhotoPost.objects.filter(category=category_id).order_by('-posted_at')

class UserView(ListView):                                   #ユーザー
    template_name = 'index.html'
    paginate_by = 9

    def get_queryset(self):
        user_id = self.kwargs['user']
        return PhotoPost.objects.filter(user=user_id).order_by('-posted_at')

class DetailView(DetailView):                               #お気に入り投稿のやつ
    template_name = 'detail.html'
    model = PhotoPost

class MypageView(ListView):                                 #マイページ
    template_name = 'mypage.html'
    paginate_by = 9

    def get_queryset(self):
        return PhotoPost.objects.filter(user=self.request.user).order_by('-posted_at')

class PhotoDeleteView(DeleteView):                          #
    model = PhotoPost
    template_name = 'photo_delete.html'
    success_url = reverse_lazy('photo:mypage')

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class FavoriteView(ListView):
    template_name = 'favorite.html'
    queryset = PhotoPost.objects.order_by('-posted_at')
    paginate_by = 9

class InDetailView(ListView):
    template_name = 'In_detail.html'
    queryset = PhotoPost.objects.order_by('-posted_at')

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('photo:contact')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']
        subject = f'お問い合わせ: {title}'
        message = f'送信者名: {name}\nメールアドレス: {email}\n件名: {title}\nメッセージ:\n{message}'
        from_email = 'admin@example.com'
        to_list = ['admin@example.com']
        email_message = EmailMessage(subject, message, from_email, to_list)
        email_message.send()
        messages.success(self.request, 'お問い合わせは正常に送信されました。')
        return super().form_valid(form)




def image_gallery(request):
    images = get_local_images()
    
    # ファイル名順にソート
    images.sort(key=lambda x: int(x['name'].split('.')[0]))
    
    # ページネーションの設定
    paginator = Paginator(images, 45)  # 1ページに45個の画像を表示（3列×15行）
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'image_gallery.html', {'page_obj': page_obj})


from django.views.generic import ListView
from .models import ImageModel
from .forms import ImageSearchForm
import re

class ImageListView(ListView):
    model = ImageModel
    template_name = 'image_search_list.html'
    context_object_name = 'images'
    paginate_by = 30  # 1ページに表示するアイテム数

    def get_queryset(self):
        queryset = super().get_queryset()
        form = ImageSearchForm(self.request.GET)
        if form.is_valid():
            if form.cleaned_data['name']:
                queryset = queryset.filter(name__icontains=form.cleaned_data['name'])
            if form.cleaned_data['type']:
                queryset = queryset.filter(type=form.cleaned_data['type'])
            if form.cleaned_data['rarity']:
                queryset = queryset.filter(rarity=form.cleaned_data['rarity'])
            if form.cleaned_data['category']:
                queryset = queryset.filter(category=form.cleaned_data['category'])
        
        # ファイル名の数字部分でソート
        def extract_number(name):
            match = re.search(r'\d+', name)
            return int(match.group()) if match else float('inf')  # 数字がない場合は無限大を返す

        queryset = sorted(queryset, key=lambda x: extract_number(x.name))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ImageSearchForm(self.request.GET)
        return context