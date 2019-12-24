import os

from django.http import HttpResponse


def index(request):
    cur_file_path = os.path.abspath(__file__)
    members_file_path = os.path.dirname(cur_file_path)
    app_file_path = os.path.dirname(members_file_path)

    templates_file_path = os.path.join(app_file_path, 'templates')
    members_html_file_path = os.path.join(templates_file_path, 'index.html')

    f = open(members_html_file_path, 'rt')
    html = f.read()
    f.close()

    return HttpResponse(html)

