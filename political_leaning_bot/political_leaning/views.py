from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import models
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import QUESTIONS, predict_leaning
from .models import UserResponse

def questionnaire_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'political_leaning/index.html', {'questions': QUESTIONS})

def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    responses = UserResponse.objects.all()
    labels = ['Far Left', 'Left', 'Center', 'Right', 'Far Right']
    counts = [responses.filter(label=label).count() for label in labels]
    total_responses = responses.count()
    average_score = responses.aggregate(models.Avg('score'))['score__avg'] or 0
    return render(request, 'political_leaning/dashboard.html', {
        'counts': counts,
        'total_responses': total_responses,
        'average_score': average_score
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('questionnaire-view')
        return render(request, 'political_leaning/login.html', {'error': 'Invalid username or password'})
    return render(request, 'political_leaning/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        if password != password_confirm:
            return render(request, 'political_leaning/register.html', {'error': 'Passwords do not match'})
        if User.objects.filter(username=username).exists():
            return render(request, 'political_leaning/register.html', {'error': 'Username already taken'})
        if User.objects.filter(email=email).exists():
            return render(request, 'political_leaning/register.html', {'error': 'Email already registered'})
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        return redirect('questionnaire-view')
    return render(request, 'political_leaning/register.html')

def logout_view(request):
    logout(request)
    return redirect('login')

class PoliticalLeaningAPI(APIView):
    def post(self, request):
        answers = [int(request.data.get(f'q{i+1}')) for i in range(20)]
        if not all(1 <= ans <= 5 for ans in answers):
            return Response({'error': 'Invalid answers'}, status=400)
        result = predict_leaning(answers)
        UserResponse.objects.create(
            user=request.user if request.user.is_authenticated else None,
            question_1=answers[0], question_2=answers[1], question_3=answers[2],
            question_4=answers[3], question_5=answers[4], question_6=answers[5],
            question_7=answers[6], question_8=answers[7], question_9=answers[8],
            question_10=answers[9], question_11=answers[10], question_12=answers[11],
            question_13=answers[12], question_14=answers[13], question_15=answers[14],
            question_16=answers[15], question_17=answers[16], question_18=answers[17],
            question_19=answers[18], question_20=answers[19],
            score=result['score'], label=result['label'], comparison=result['comparison']
        )
        return Response({
            'score': result['score'],
            'label': result['label'],
            'comparison': result['comparison']
        })