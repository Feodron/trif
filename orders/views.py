from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
# from .qr import img_2
from django.shortcuts import render
import qrcode


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            return render(request, 'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form})


def index(request):
    qr_image = False
    if request.method == "POST":
        data = request.POST['data']
        img = qrcode.make(data)
        img.save("media/qr/qr.png")
        qr_image = True

    return render(request, 'orders/order/created.html', {'qr_image': qr_image})
