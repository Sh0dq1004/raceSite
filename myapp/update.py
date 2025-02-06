from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .models import Person,Odds

def update():
   if (len(Odds.objects.all())!=0):
    odds_model=Odds.objects.all()[len(Odds.objects.all())-1]
    odds_model.odds_opt1=odds_model.total_money/odds_model.money_opt1
    odds_model.odds_opt2=odds_model.total_money/odds_model.money_opt2
    odds_model.odds_opt3=odds_model.total_money/odds_model.money_opt3
    odds_model.odds_opt4=odds_model.total_money/odds_model.money_opt4
    odds_model.save()

# new=>
def start():
   scheduler = BackgroundScheduler()
   
   scheduler.add_job(update, 'interval', seconds=5) # schedule
   scheduler.start()