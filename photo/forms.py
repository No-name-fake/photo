from django import forms
from .models import PhotoPost

class PhotoPostForm(forms.ModelForm):
    class Meta:
        model = PhotoPost
        fields = ['category', 'title', 'comment', 'image1', 'image2', 'image3', 'image4']






class ContactForm(forms.Form):
    
    name=forms.CharField(label='お名前')
    email=forms.EmailField(label='メールアドレス')
    title=forms.CharField(label='件名')
    message=forms.CharField(label='メッセージ',widget=forms.Textarea)
    
    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        
        self.fields['name'].widget.attrs['placeholder']=\
            'お名前を入力してください'
        self.fields['name'].widget.attrs['class']='form-control'
        
        self.fields['email'].widget.attrs['placeholder']=\
            'メールアドレスを入力してください'
        self.fields['email'].widget.attrs['class']='form-control'
        
        self.fields['title'].widget.attrs['placeholder']=\
            'タイトルを入力してください'   
        self.fields['title'].widget.attrs['class']='form-control'
        
        self.fields['message'].widget.attrs['placeholder']=\
            'メッセージを入力してください'
        self.fields['message'].widget.attrs['class']='form-control'


# forms.py
from django import forms
from .models import Type, Rarity, Category

class ImageSearchForm(forms.Form):
    name = forms.CharField(required=False, label='名前')
    type = forms.ModelChoiceField(queryset=Type.objects.all(), required=False, label='タイプ')
    rarity = forms.ModelChoiceField(queryset=Rarity.objects.all(), required=False, label='レアリティ')
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False, label='カテゴリ')
