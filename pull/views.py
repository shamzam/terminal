from django.http import HttpResponse
import subprocess

def index(request):
    #try:
    result = subprocess.run(["aa"], shell=True, capture_output=True).stdout
    #except subprocess.CalledProcessError as e:
    #    result = "aa"
    #    if hasattr(e, 'output'):
    #        result += result + 'output: ' + e.output.decode('utf8') + "\n"
    #    if hasattr(e, 'stderr'):
    #        result += result + 'stderr: ' + e.stderr.decode('utf8') + "\n"
    #    if hasattr(e, 'stdout'):
    #        result += result + 'stderr: ' + e.stdout.decode('utf8') + "\n"

    return HttpResponse(result)
