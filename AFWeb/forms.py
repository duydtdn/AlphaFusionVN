from django import forms
from AFWeb.models import TheLoai, TinTuc

class TinTucForm(forms.ModelForm):
    tieu_de = forms.CharField(label="Tiêu đề", required=True)
    # theloai = forms.ModelMultipleChoiceField(
    #                     queryset=TheLoai.objects.all().order_by('ten'),
    #                     label="Chuyên mục",
    #                     widget=forms.CheckboxSelectMultiple)
    trich_yeu = forms.CharField(label="Trích yếu", required=False)
    # noi_dung = forms.CharField(label="Nội dung", required=True)
    class Meta:
        model = TinTuc
        # fields = '__all__'
        exclude = ['ngay_dang', 'duyet']