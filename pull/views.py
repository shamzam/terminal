from django.shortcuts import render
from django.template import loader
import subprocess

def index(request):
    result = []
    try:
        output = subprocess.run(["cd /var/www/mymanager/mymanager/ && git reset --hard HEAD && git pull && touch wsgi.py"], shell=True, capture_output=True)
        result.append((output.stdout.decode('utf8') + '\n').replace('\n', '<br/>'))
        if hasattr(output, 'stderr'):
            result.append(('stderr: ' + output.stderr.decode('utf8') + '\n').replace('\n', '<br/>'))
    except:
        result.append('failed')

    context = {
        'result': result,
    }

    return render(request, 'pull/index.html', context)
