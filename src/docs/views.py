from django.shortcuts import render
from django.views import View

from .models import DocumentCategory

# Create your views here.
class DocsView(View):
    def get(self, request):
        document_categories = DocumentCategory.objects.published()
        return render(request, 'docs/list.html', {'document_categories': document_categories})