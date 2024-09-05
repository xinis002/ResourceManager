import stripe
from users.models import Payment
from config.settings import STRIPE_API_KEY
stripe.api_key = STRIPE_API_KEY

def create_stripe_product(course):
    product = stripe.Product.create(
        name=course.name,
        description=course.description
    )
    return product['id']
def create_stripe_price(course, product_id):

    price = stripe.Price.create(
        unit_amount=int(course.price * 100),
        currency='rub',
        product=product_id,
    )
    return price['id']

def create_checkout_session(course, price_id):

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': price_id,
            'quantity': 1,
        }],
        mode='payment',
        success_url='https://yourdomain.com/success/',
        cancel_url='https://yourdomain.com/cancel/',
    )
    return session['id'], session['url']

def retrieve_session(session_id):

    return stripe.checkout.Session.retrieve(session_id)