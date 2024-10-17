from django.shortcuts import render, redirect
from .models import *
from  django.contrib.auth.models import auth
from  django.contrib.auth import login, logout, authenticate
from django.contrib import messages
import requests
from django.db.models import Q
from .forms import NewsForm
'''from .models import Comment
from .forms import CommentForm'''
from django.http import JsonResponse
from .models import News

# Create your views here.

'''def like_news(request, news_id):
    if request.method == 'POST':
        news = News.objects.get(id=news_id)
        if news.likes.filter(id=request.user.id).exists():
            news.likes.remove(request.user)
            liked = False
        else:
            news.likes.add(request.user)
            liked = True
        return JsonResponse({'liked': liked, 'count': news.likes.count()})

def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user  # Assuming user is authenticated
            comment.save()
            return redirect('home')  # Redirect to homepage or news details
    else:
        form = CommentForm()
    
    return render(request, 'home.html', {'form': form})'''


def createaccount(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        email = request.POST['email']
        
        choice = request.POST.get('choice')

        

        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username already exsist')
                return redirect('createaccount')
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email already exsist')
                return redirect('createaccount')
            
            else:
                user = User.objects.create_user(username=username, email=email, password=password, choice=choice)
                user.save()

                user_login = auth.authenticate(username=username,password=password)
                
                auth.login(request, user_login)

                

                return redirect('home')
                

        
        else:
            messages.info(request, 'invalid data')
            return redirect('createaccount')



    return render(request, 'news/create_account.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
   

     

          
        user = auth.authenticate(username=username ,password=password)  
        if user is not None:
                auth.login(request,user) 
                return redirect('home')  
                   

           
        
        else:
            messages.info(request, 'username or password inccorect')
            return redirect('login')




    return render(request, 'news/login.html')


def logout_page(request):
    logout(request)
    return redirect('/login/')

def home(request):
    if request.method == 'POST':
        user = request.user
        review = request.POST['review']

        review_create = Review.objects.create(user=user, review=review)
        review_create.save()
        return redirect('home')
 
        

    reviews = Review.objects.all()
    users = User.objects.all()
    user_choice = request.user.choice 
    if user_choice:
        newss = News.objects.filter(catergory__title=user_choice)
    else:
        newss = News.objects.all()
    

    context = {'newss':newss, 'users':users, 'reviews':reviews}
    return render(request, 'news/home.html', context)


def profile(request,pk):

    notifications = Notification.objects.all()

    user = User.objects.get(id=pk)
    newss = News.objects.all()
    sportcategory = NewsCategory.objects.get(title='sports')
    politicscategory = NewsCategory.objects.get(title='politics')
    entertainmentcategory = NewsCategory.objects.get(title='entertainment')
    weathercategory = NewsCategory.objects.get(title='weather')
    healthcategory = NewsCategory.objects.get(title='health')
    businesscategory = NewsCategory.objects.get(title='business')
    technologycategory = NewsCategory.objects.get(title='technology')
    
    sports = News.objects.filter(catergory=sportcategory)
    technology = News.objects.filter(catergory=technologycategory)
    health = News.objects.filter(catergory=healthcategory)
    business = News.objects.filter(catergory=businesscategory)
    weather = News.objects.filter(catergory=weathercategory)
    entertainments = News.objects.filter(catergory=entertainmentcategory)
    politics = News.objects.filter(catergory=politicscategory)
    
    context = {'newss':newss, 'sports':sports,'politics':politics,'weather':weather,'entertainments':entertainments,'business':business,'health':health,'technology':technology, 'user':user, 'notifications':notifications}
    return render(request, 'news/profile.html', context)


def sports(request):
    sportcategory = NewsCategory.objects.get(title='sports')
    sports = News.objects.filter(catergory=sportcategory)
    

    context = {'sports':sports}

    return render(request, 'news/sports.html', context)

def technology(request):

    technologycategory = NewsCategory.objects.get(title='technology')
    technology = News.objects.filter(catergory=technologycategory)
    technology = News.objects.filter(catergory=technologycategory)
    

    context = {'technology':technology}

    return render(request, 'news/technology.html', context)

def politics(request):
    politicscategory = NewsCategory.objects.get(title='politics')
    politics = News.objects.filter(catergory=politicscategory)
    

    context = {'politics':politics}

    return render(request, 'news/politics.html', context)


def entertainments(request):
    entertainmentcategory = NewsCategory.objects.get(title='entertainment')
    entertainment = News.objects.filter(catergory=entertainmentcategory)
    

    context = {'entertainment':entertainment}

    return render(request, 'news/entertainment.html', context)

def health(request):
    healthcategory = NewsCategory.objects.get(title='health')
    health = News.objects.filter(catergory=healthcategory)
    

    context = {'health':health}

    return render(request, 'news/health.html', context)

def business(request):
    businesscategory = NewsCategory.objects.get(title='business')
    business = News.objects.filter(catergory=businesscategory)
    

    context = {'business':business}

    return render(request, 'news/business.html', context)

def weather(request):
    weathercategory = NewsCategory.objects.get(title='weather')
    weather = News.objects.filter(catergory=weathercategory)
    

    context = {'weather':weather}

    return render(request, 'news/weather.html', context)


def newsdetails(request,pk):
    news=News.objects.get(id=pk)
    context={'news':news}
    return render(request,'news/newsdetails.html',context)




API_KEY = '321bc1d0b8e0430bac7e3ccb2e1d4d88'



def headlines(request):
    country = request.GET.get('country')
    category = request.GET.get('category')
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&category=business&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()

        articles = data['articles']
    elif category:    
        url = f'https://newsapi.org/v2/top-headlines?category={category}&category=business&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()

        articles = data['articles']

    else:    
        url = f'https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()

        articles = data['articles']



    context = {'articles':articles}
    # context = {'data':data}

    
    return render(request, 'news/headlines.html', context)




def search(request):
    searchs = request.GET.get('q')
    if searchs:
        newss = News.objects.filter(
            Q(name__icontains=searchs)|
            Q(description__icontains=searchs)|
            Q(catergory__title__icontains=searchs)
            
        )

        context = {'newss': newss}
        return render(request, 'news/search.html', context )
    else:
        return render(request, 'news/search.html')

# def adminpanel(request):
#     news = News.objects.get(id=pk)

#     if request.method == 'POST':
#         user = request.user
#         name = request.POST['name']
#         description = request.POST['description']
#         image = request.POST['image']
#         catergory = request.POST['catergory']
#         date = request.POST['date']
#         source = request.POST['source']

#         createnews = News.objects.create(name=name,user=user, description=description, image=image,catergory=catergory, date=date, source=source)
#         createnews.save()
#         return redirect('adminpanel')




#     return render(request,'news/adminpanel.html')





def adminpanel(request):
    # if request.method == 'POST':
    #     name = request.POST['name']
    #     description = request.POST['description']
    #     image = request.FILES.get('image')
    #     category_id = request.POST['catergory']
    #     source = request.POST['source']
        
    #     category = NewsCategory.objects.get(pk=category_id)
        
    #     news = News.objects.create(
    #         name=name,
    #         description=description,
    #         image=image,
    #         category=category,
    #         source=source
    #     )
    #     news.save()
        
    #     # You might want to add some validation and error handling here
        
    #     return redirect('adminpanel')  # Redirect to a page showing the list of news items
    
    # categories = NewsCategory.objects.all()
    form = NewsForm()
    if request.method == "POST":
        form = NewsForm( request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('adminpanel')

        

    context = {'form':form}    
        
    return render(request, 'news/adminpanel.html',context )




def help(request):
    if request.method=="POST":
        user=request.user
        question=request.POST['question']
        helpcreate=Help.objects.create(user=user,question=question)
        helpcreate.save()
        return redirect('help')
    helps=Help.objects.all()
    context={"helps":helps}
    
    
    return render(request,'news/help.html',context)