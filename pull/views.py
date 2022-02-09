from django.shortcuts import render
from django.template import loader
import subprocess

def index(request):
    result = []
    try:
        output = subprocess.run(["cd /var/www/mymanager/mymanager/ && git reset --hard HEAD && sudo git pull && touch wsgi.py"], shell=True, capture_output=True)
        result.append((output.stdout.decode('utf8') + '\n'))
        if hasattr(output, 'stderr'):
            result.append(('stderr: ' + output.stderr.decode('utf8') + '\n'))
    except:
        result.append('failed')

    context = {
        'result': result,
    }

    return render(request, 'pull/index.html', context)
