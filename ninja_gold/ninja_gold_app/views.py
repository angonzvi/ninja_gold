from django.shortcuts import render, redirect, HttpResponse
import random
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0       
    context = {
        'gold': request.session['gold'],
        
    }
    return render(request, 'index.html', context)

def ninjagold(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
        return redirect(request,'index.html')

def process_money(request,game):
        request.session['activities'] = []
        gold = 0
        if game == 'farm':
            rand = random.randint(10,20)
        elif game == 'cave':
            rand = random.randint(5,10)
        elif game == 'house':
            rand = random.randint(2,5)
        elif game == 'casino':
            rand = random.randint(-50,50)
        request.session['gold'] += rand
        gold +=rand
        if gold >= 0:
            request.session['activities'].append({
                'text' : f'Haz ganado {gold} oros en {game}',
                'golds' : request.session['gold']
            })
            request.session.save()
        else:
            request.session['activities'].append({
                'text' : f'You Lose in {game}: {gold} Gold',
                'golds' : request.session['gold']
            })
            request.session.save()

        return redirect('/')

def reset(request):
    request.session['gold'] = 0
    request.session['activities'] = []   
    return redirect('/')

