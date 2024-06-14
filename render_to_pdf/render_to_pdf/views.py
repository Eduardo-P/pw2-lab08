from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from .renderers import render_to_pdf
import datetime

class GeneratePDF(View):
    def get(selt, request, *args, **kwargs):
        template = get_template('pdfs/invoice.html')
        context = {
            'today': datetime.date.today(), 
            'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'invoice_number': 1233434,
        }
        html = template.render(context)
        pdf = render_to_pdf('pdfs/invoice.html', context)
        if pdf:
            return HttpResponse(pdf, content_type='application/pdf')
        return HttpResponse("Not found")

"""
def generate_view(request, *args, **kwargs):
    template = get_template('incoice.html')
    context = {
        'today': datetime.date.today(), 
        'amount': 39.99,
        'customer_name': 'Cooper Mann',
        'invoice_number': 1233434,
    }
    html = template.render(context)
    return HttpResponse(html)
"""