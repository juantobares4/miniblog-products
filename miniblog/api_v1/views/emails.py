from django.core.mail import send_mail, EmailMultiAlternatives
from django.http import HttpResponse
from django.template.loader import render_to_string # Convierte un HTML a un String
from django.utils.html import strip_tags # Convierte un HTML a texto plano

def send_test_email(request):
    subject = 'Probando el envío de emails'
    body = 'Enviando emails desde Django'
    recipient = ['matias@matias.com', 'huck@itec.com']
    from_email = 'salidodeaca@google.com'

    send_mail(
        subject=subject,
        message=body,
        recipient_list=recipient,
        from_email=from_email

    )

    return HttpResponse('Email enviado correctamente.')

def email_products_sender(request):
    user = 'John Doe'

    products = [
        {
            'name':'product1',
            'price': 123456
        },
        {
            'name':'product2',
            'price': 1234567,
        },
        {
            'name':'product3',
            'price': 12345678
        }

    ]

    subject = 'Tenemos ofertas para vos'

    html_content = render_to_string(
        'email/products_email.html',
        dict(user = user, products = products)

    )

    text_content = strip_tags(html_content) # Convertir todo el HTML en un texto.

    email = EmailMultiAlternatives(
       subject=subject,
       body=text_content,
       from_email='salidodeaca@email.com',
       to=['Carlitos@carlitos.com']
    
    )

    email.attach_alternative(html_content, 'text/html')
    email.send()

    return HttpResponse('Email enviado correctamente')