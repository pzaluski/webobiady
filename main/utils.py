from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from orders.models import OrderSettings
from restaurants.models import Restaurant


def get_order_settings():
    try:
        os = OrderSettings.objects.get(active=True)
    except ObjectDoesNotExist:
        os = OrderSettings()
        os.active = False
        # try:
        #     os = OrderSettings.objects.last()
        # except ObjectDoesNotExist:
        #     os = OrderSettings()
        #     try:
        #         os.restaurant = Restaurant.objects.first()
        #     except ObjectDoesNotExist:
        #         r = Restaurant(name="Zagrycha", delivery_price=0)
        #         r.save()
        #         os.restaurant = r
        #     try:
        #         os.purchaser = User.objects.get(username="mbork")
        #     except ObjectDoesNotExist:
        #         os.purchaser = User.objects.first()
        #     os.order_deadline = "10:30"
        #     os.active = True
        #     os.save()
        #     return os
        # os.active = True
        # os.save()
    return os


def get_today_restaurant():
    os = get_order_settings()
    return os.restaurant


class EmailMessageCreator(object):
    subject = None
    body_template = None
    body_template_html = None
    rendered_message = None
    rendered_message_html = None
    from_email = 'WebObiady <noreply@webobiady.pl>'

    def set_subject(self, subject):
        self.subject = subject.strip()

    def set_body_template(self, template):
        self.body_template = template

    def set_body_template_html(self, template):
        self.body_template_html = template

    def set_message_context(self, context):
        self.rendered_message = get_template(self.body_template).render(context)
        if self.body_template_html is not None:
            self.rendered_message_html = get_template(self.body_template_html).render(context)

    def send_message(self, to_emails):
        msg = EmailMultiAlternatives(self.subject, self.rendered_message, self.from_email, to_emails)

        if self.body_template_html is not None:
            msg.attach_alternative(self.rendered_message_html, "text/html")

        msg.send()
