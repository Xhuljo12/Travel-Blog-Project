from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage
from .forms import CommentsForm
from django.contrib import messages
from .models import *
from django.db.models import Q 


# Create your views here.

def homepage(request):
    category = Category.objects.all()
    context = {"category":category}
    if request.method == "POST":
        email_subscribe = request.POST['email']
        if Subscribe.objects.filter(subscribe_email=email_subscribe).exists():
         messages.error(request, 'Email already subscribed')
         return redirect('homepage')
        else : 
         Subscribe(subscribe_email=email_subscribe).save()
         messages.success(request, 'Email registered successfully')
         return render(request, 'response.html')
    return render(request, 'homepage.html', context)

def search (request):
    if request.method == "POST":
        searched = request.POST.get('search')
        if searched:
            searching= Articles.objects.filter(articles_name__contains=searched)
            if searching:
                context={'searched':searched,'searching': searching}
                return render(request,'search.html',context)
            else:
                messages.info(request, ' ')
        else:
            return HttpResponseRedirect('/search/')
    context={'searching':searching}
    return render(request,'search.html', context)

def about(request):
    return render(request, 'about.html')

def response(request):
    return render(request, 'response.html')

def contact(request):

    if request.method == "POST":
        name_contact = request.POST['firstName']
        surname_contact = request.POST['lastName']
        email_contact = request.POST['email']
        comment_contact = request.POST['comment']
        Contact(contact_name=name_contact, contact_surname=surname_contact, 
        contact_email=email_contact, contact_message=comment_contact).save()

        return render(request, 'response.html')
    return render(request, 'contact.html')

def articles(request):
    articles = Articles.objects.all().order_by("-articles_id")
    p = Paginator(articles, 4)
    print('NUMBER OF PAGES')
    print(p.num_pages)
    page_num = request.GET.get("page", 1)
    try: 
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    context = {"articles":page}
    return render(request, 'articles.html', context)

def category(request, id):
    categories = Category.objects.get(category_id=id)
    categori = Articles.objects.filter(articles_categories=categories)
    category = Category.objects.all().order_by("-category_id")
    context = {"category":category, "categories":categories, "categori":categori}
    return render(request, 'category.html', context)

def article(request, id):
    articleDetail = Articles.objects.get(articles_id=id)
    different = Comments.objects.filter(comments_categories=articleDetail)
    if request.method == "POST":
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_categories = articleDetail
            comment.save()
    else:
        form = CommentsForm()
        #email_comments = request.POST['email']
        #lines_comments = request.POST['comment']
        #Comments(comments_lines=lines_comments, comments_email=email_comments).save()
    #comments = Comments.objects.all().order_by("-comments_id")
    context = {"articleDetail":articleDetail, "different":different, "form":form} 
    return render(request, 'article.html', context)

