from django.shortcuts import render,redirect
from .models import Food,Consume
# Create your views here.

def index(request):
    if request.method == 'POST':
        food_consumed_name = request.POST['food_consumed']
        food_consumed = Food.objects.filter(name=food_consumed_name).first()
        user = request.user
        consume = Consume(user=user,food_consumed=food_consumed)
        consume.save()
        foods = Food.objects.all()
    else:
        foods= Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)
    return render(request, 'calorie/index.html',{'foods': foods,'consumed_food':consumed_food})

def delete_consume(request, id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect('/')
    return render(request,'calorie/delete.html')