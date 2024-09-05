from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from users.models import Payment, User
from users.serializers import PaymentSerializer, UserSerializer

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Course, Payment
from .services import create_stripe_product, create_stripe_price, create_checkout_session


class PaymentCreateAPIView(CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_fields = ("payment_type", "lesson", "course")
    ordering_fields = ("payment_date",)
    search_fields = ("user",)


    def create_payment(request, course_id):

        course = get_object_or_404(Course, id=course_id)


        product_id = create_stripe_product(course)
        price_id = create_stripe_price(course, product_id)


        session_id, payment_url = create_checkout_session(course, price_id)


        payment = Payment.objects.create(
            course=course,
            stripe_session_id=session_id,
        )

        return JsonResponse({'url': payment_url})


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()



