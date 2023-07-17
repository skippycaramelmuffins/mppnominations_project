from django.shortcuts import render, redirect
from .models import Voter, Position, Nomination, Vote
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, "index.html")

def position(request):
    return render(request, "position.html")

def login(request):
    if request.method == 'POST':
        student_email = request.POST.get('student_email')
        student_password = request.POST.get('student_password')
        try:
            voter = Voter.objects.get(student_email=student_email)
            if student_password == student_password:
                return redirect('dashboard', studentid=voter.pk)
            else:
                error_message = "Invalid email or password"

        except Voter.DoesNotExist:
            error_message = "Invalid email or password"

        return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        contact_number = request.POST.get("contact_number")
        student_email = request.POST.get('student_email')
        student_password = request.POST.get('student_password')

        if Voter.objects.filter(student_email=student_email).exists():
            return render(request, 'register.html', {'error_message': 'Email already exists'})

        voter = Voter(
            student_name=student_name,
            contact_number=contact_number,
            student_email=student_email,
            student_password=student_password
        )

        voter.save()

        return redirect('login')
    
    return render(request,'register.html')

def voter(request):
    if request.method == 'POST':
        studentname = request.POST['student_name']
        address = request.POST['address']
        contact_number= request.POST['contact_number']
        data = Voter(student_name=studentname, address=address, contact_number=contact_number)
        data.save()
        dict = {
            'message': 'Your details has been successfully submitted.'
        }

        return render(request, "voter.html", dict)
    
    else:
        dict = {
            'message': ' '
        }

        return render(request, "voter.html", dict)

def voterdata(request):
    data = Voter.objects.all()
    dict = {
        'data': data
    }

    return render(request, "profile.html", dict)

def nominees(request):
    if request.method == 'POST':
        nomineeid = request.POST['nomineeID']
        position = request.POST['position']
        session = request.POST['session']
        year = request.POST['year']
        n_desc = request.POST['n_desc']

        data = Nomination(
            nomineeID=nomineeid, 
            position=position, 
            session=session,
            year=year,
            n_desc=n_desc
        )
        
        data.save()

        return render(request, "nominees.html")
    
    else:
        return render(request, "nominees.html")

def nomineesdata(request):
    alldata = Nomination.objects.all()
    dict = {
        'alldata': alldata
    }

    return render(request, "nomineesdata.html", dict)

def dashboard(request, studentid):
    voter = Voter.objects.get(pk=studentid)
    nominations = Nomination.objects.all()
    votes = Vote.objects.filter(studentid=studentid).values_list('nomineeID', flat=True)

    position = Position.objects.all()

    context = {
        'voter' : voter,
        'votes' : votes,
        'positions' : position,
        'nominations' : nominations
    }

    return render(request, 'dashboard.html', context)

def voted(request, studentid):
    voter = Voter.objects.get(pk=studentid)
    voted = Vote.objects.filter(voter=voter)

    context = {
        'voter': voter,
        'voted': voted
    }
    return render(request, 'voted.html', context)

def voting(request, studentid, nomineeID):
    if request.method == "POST":
        voter = Voter.objects.get(pk=studentid)
        nominations = Nomination.objects.get(nomineeID=nomineeID)
        vote, created = Vote.objects.get_or_create(voter=voter, nomineeID=nominations)

        if created:
            return redirect('voted', studentid=studentid)

        else:
            messages.error(request, 'Vote has already being casted!')
            return redirect('dashboard', studentid=studentid)

    return redirect('dashboard', studentid=studentid)

def profile_view(request, studentid):
    try:
        # Retrieve the logged-in voter from the database using the ID
        voter = Voter.objects.get(pk=studentid)
        
        # Pass the voter data to the profile template
        return render(request, 'profile.html', {'voter': voter})
    
    except Voter.DoesNotExist:
        # Handle the case when the voter is not found
        error_message = "Voter not found"
        return render(request, 'profile.html', {'error_message': error_message})
