from django.shortcuts import redirect

def defaultDirect(request):
    return redirect('/admin/')