from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from .models import Image


MODEL = Image
PAGINATE_BY = 50


class MediaList(ListView):
    model = MODEL
    template_name = "admin/mediapicker.html"
    paginate_by = PAGINATE_BY

    def get_context_data(self, **kwargs):
        ctx = super(MediaList, self).get_context_data(**kwargs)
        ctx['q'] = self.request.GET.get('q',"")
        ctx['base'] = "CKEditor=%s&CKEditorFuncNum=%s&langCode=%s" % (
            self.request.GET.get('CKEditor',""),
            self.request.GET.get('CKEditorFuncNum',""),
            self.request.GET.get('langCode',"")
        )
        return ctx

    def get_queryset(self):
        queryset = MODEL.objects.all()
        if self.request.GET.get('q', None):
            q = self.request.GET.get('q', None)
            queryset = queryset.filter(
                credit__contains=q, 
                caption__contains=q, 
                description__contains=q
            )
        return queryset

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):        
        return super(MediaList, self).dispatch(request, *args, **kwargs)
