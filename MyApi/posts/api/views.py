from rest_framework import viewsets
from rest_framework.response import Response
from ..models import Posts, PostsRates
from .serializers import PostsRatesSerializer, PostsSerializer
from django.core.mail import send_mail
import threading


class HandleNotifications(threading.Thread):

    def __init__(self, message, subject, recipient_list):
        self.message = message
        self.subject = subject
        self.recipient_list = recipient_list
        threading.Thread.__init__(self)

    def run(self):
        from_email = 'brainplow618@gmail.com'
        send_mail(self.subject, self.message, from_email, self.recipient_list, fail_silently=False)


class PostsViewSet(viewsets.ModelViewSet):
    serializer_class = PostsSerializer

    def send_email(self, message, subject, recipient_list):
        from_email = 'brainplow618@gmail.com'
        send_mail(subject, message,from_email,recipient_list, fail_silently=False)


    def get_queryset(self):
        posts = Posts.objects.all()
        return posts

    def create(self, request, *args, **kwargs):
        post_data = request.data

        # new_rates = PostsRates.objects.create(likes=post_data["rates"]["likes"], dislikes=post_data["rates"]["dislikes"])
        # new_rates.save()
        #
        # new_post = Posts.objects.create(post_title=post_data["post_title"], post_body=post_data["post_body"], rates=new_rates)
        # new_post.save()

        new_rate = PostsRates.objects.create(likes=0, dislikes=0)
        new_rate.save()

        new_post = Posts.objects.create(
            post_title=post_data["post_title"], post_body=post_data["post_body"], rates=new_rate)
        new_post.save()

        self.send_email("this a notification", "Notification", ['brainplow618@gmail.com', ])
        HandleNotifications("this a notification", "Notification",['codes.environment@gmail.com',]).start()
        serializer = PostsSerializer(new_post)
        return Response(serializer.data)


class PostsratesViewSet(viewsets.ModelViewSet):
    serializer_class = PostsRatesSerializer

    def get_queryset(self):
        rates = PostsRates.objects.all()
        return rates
