from django.http import HttpResponse
import subprocess

def index(request):
    #try:
    try:
        result = subprocess.run(["sudo"], shell=True, capture_output=True)
        text = result.stderr.decode('utf8') + "\n"
        if hasattr(result, 'stderr')
            text += text + 'stderr: ' + result.stderr.decode('utf8') + "\n"
    except:
        text = "aa"
    #except subprocess.CalledProcessError as e:
    #    result = "aa"
    #    if hasattr(e, 'output'):
    #        result += result + 'output: ' + e.output.decode('utf8') + "\n"
    #    if hasattr(e, 'stderr'):
    #        result += result + 'stderr: ' + e.stderr.decode('utf8') + "\n"
    #    if hasattr(e, 'stdout'):
    #        result += result + 'stderr: ' + e.stdout.decode('utf8') + "\n"

    return HttpResponse(text)
