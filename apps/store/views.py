from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView, UpdateView
from django.views.generic.edit import UpdateView

from .models import Store


class IndexTemplateView(TemplateView):
    template_name = "index.html"


class StoreCreateView(SuccessMessageMixin, CreateView):
    model = Store
    fields = [
        "ticket",
        "name",
        "block",
        "parcel",
    ]
    success_url = "/"
    success_message = "order# %(ticket)s was created"


class OrderListView(ListView):
    model = Store
    queryset = Store.objects.filter(
        Q(status="payment pending")
        | Q(status="searching")
        | Q(status="stamped")
        | Q(status="printed")
    )
    ordering = ["-updated"]
    template_name = "store/order_list.html"


class CashierListView(ListView):
    model = Store
    queryset = Store.objects.filter(
        Q(status="payment pending") | Q(status="stamped")
    )
    template_name = "store/cashier_list.html"
    ordering = ["-updated"]


def mark_as_paid(request, pk):
    order_item = Store.objects.get(pk=pk)
    order_item.status = "searching"
    order_item.save()
    return redirect("store:cashier-list")


def mark_as_delivered(request, pk):
    delivered_item = Store.objects.get(pk=pk)
    delivered_item.status = "delivered"
    delivered_item.save()
    return redirect("store:cashier-list")


class VaultListView(ListView):
    model = Store
    queryset = Store.objects.filter(status="searching")
    ordering = ["-updated"]
    template_name = "store/vault_list.html"


def mark_as_printed(request, pk):
    vault_item = Store.objects.get(pk=pk)
    vault_item.status = "printed"
    vault_item.save()
    return redirect("store:vault-list")


class SecretaryListView(ListView):
    model = Store
    queryset = Store.objects.filter(status="printed")
    ordering = ["-updated"]
    template_name = "store/secretary_list.html"


def mark_as_stamped(request, pk):
    secretary_item = Store.objects.get(pk=pk)
    secretary_item.status = "stamped"
    secretary_item.save()
    return redirect("store:secretary-list")


class DeliveriesListView(ListView):
    model = Store
    queryset = Store.objects.filter(status="delivered")
    ordering = ["-updated"]
    template_name = "store/delivered_list.html"
