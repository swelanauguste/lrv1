from django.urls import path

from . import views

app_name = "store"


urlpatterns = [
    path("", views.IndexTemplateView.as_view(), name="index"),
    path("new-orders/", views.StoreCreateView.as_view(), name="new-orders"),
    path(
        "order-list/",
        views.OrderListView.as_view(),
        name="order-list",
    ),
    path(
        "cashier-list/",
        views.CashierListView.as_view(),
        name="cashier-list",
    ),
    path(
        "mark-as-paid/<int:pk>/",
        views.mark_as_paid,
        name="mark-as-paid",
    ),
    path(
        "vault-list/",
        views.VaultListView.as_view(),
        name="vault-list",
    ),
    path(
        "mark-as-printed/<int:pk>/",
        views.mark_as_printed,
        name="mark-as-printed",
    ),
    path(
        "secretary-list/",
        views.SecretaryListView.as_view(),
        name="secretary-list",
    ),
    path(
        "mark-as-stamped/<int:pk>/",
        views.mark_as_stamped,
        name="mark-as-stamped",
    ),
    path(
        "deliveries-list/",
        views.DeliveriesListView.as_view(),
        name="deliveries-list",
    ),
    path(
        "mark-as-delivered/<int:pk>/",
        views.mark_as_delivered,
        name="mark-as-delivered",
    ),
]
