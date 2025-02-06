from django.shortcuts import render,redirect
from .forms import TestForm,BettingForm,AnswerForm
from .models import Person,Odds
from copy import copy

# Create your views here.
def index_template(request):
    name=request.session.get('user_name')
    context={
        'field':Person.objects.filter(name=name)[0]
    }
    return render(request, 'index.html', context)

def user_setting_template(request):
    message="ユーザーの登録をお願いします"
    name_lst=[i.name for i in Person.objects.all()]
    if (request.method=='POST'):
        name=request.POST['name']
        if name in name_lst:
            message="そのユーザーは既に登録されています"
            return render(request, 'user_setting.html',{'form':TestForm,'message':message})    
        else:
            request.session['user_name']=name
            model = Person(name=name, money=100000, bet=0, bet_to=0)
            model.save()
            return redirect('/home')
    else:
        return render(request, 'user_setting.html',{'form':TestForm,'message':message})

def betting_template(request):
    message="掛け金を入力してください"
    if(request.method=='POST'):
        name=request.session.get('user_name')
        bet=int(request.POST['bet_money'])
        user=Person.objects.filter(name=name)[0]
        if (bet > user.money):
            message="上限を超えています"
        else:
            name_lst=['しょうた','たいが','たくみ','そら']
            p_num=int(request.POST['select'][0])
            user.bet_to=name_lst[p_num]
            user.bet=bet
            user.save()
            odd_model=Odds.objects.all()[len(Odds.objects.all())-1]
            odd_model.total_money+=bet
            if (p_num==0):
                odd_model.money_opt1+=bet
            elif (p_num==1):
                odd_model.money_opt2+=bet
            elif (p_num==2):
                odd_model.money_opt3+=bet
            elif (p_num==3):
                odd_model.money_opt4+=bet
            odd_model.save()
            return redirect('/confirm_before')
    return render(request, 'betting.html', {'form':BettingForm, 'message':message})

def confirm_before_template(request):
    name=request.session.get('user_name')
    user=Person.objects.filter(name=name)[0]
    context={
        'field':user
    }
    if (request.method=='POST'):
        print("1")
        user.money-=user.bet
        user.save()
        return redirect('/confirm_after')
    else:
        return render(request, 'confirm-before.html', context)

def confirm_after_template(request):
    name=request.session.get('user_name')
    context={
        'field':Person.objects.filter(name=name)[0]
    }
    return render(request, 'confirm-after.html', context)

def admin_template(request):
    match_num=0
    if (request.method=='POST'):
        if ('clear' in request.POST):
            Person.objects.all().delete()
            Odds.objects.all().delete()
        elif ('answer' in request.POST):
            name_lst=['しょうた','たいが','たくみ','そら']
            odds_model=Odds.objects.all()[len(Odds.objects.all())-1]
            odds_lst=[odds_model.odds_opt1,odds_model.odds_opt2,odds_model.odds_opt3,odds_model.odds_opt4]
            p_num=int(request.POST['select'][0])
            answer=name_lst[p_num]
            for user in Person.objects.all():
                if (user.bet_to==answer):
                    user.money+=odds_lst[p_num]*user.bet
                user.bet=0
                user.save()
        elif ('result' in request.POST):
            first_money=0
            second_money=0
            first_users=[]
            second_users=[]
            for user in Person.objects.all():
                print(user.money)
                if second_money > user.money:
                    continue
                if second_money == user.money:
                    second_users.append(user.name)
                elif first_money > user.money:
                    second_money=user.money
                    second_users=[user.name]
                elif first_money == user.money:
                    first_users.append(user.name)
                else:
                    second_money=copy(first_money)
                    second_users=copy(first_users)
                    first_money=user.money
                    first_users=[user.name]
            
            print(f"１位は{first_money}円で{first_users}です。")
            print(f"２位は{second_money}円で{second_users}です。")

        else:
            for i in range(1,4):
                if (f'match{i}' in request.POST):
                    Odds(match_num=i).save()
                    match_num=i
                    break
    return render(request, 'admin.html', {'form':AnswerForm, 'match_num':match_num})

def odds_template(request):
    return render(request, 'odds.html', {'field':Odds.objects.all()[len(Odds.objects.all())-1]})