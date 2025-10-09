from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Category, Expense
from .serializers import CategorySerializer, ExpenseSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['category', 'date']

    @action(detail=False)
    def summary(self, request):
        data = self.queryset.values('category__name').annotate(total=Sum('amount'))
        return Response(data)
