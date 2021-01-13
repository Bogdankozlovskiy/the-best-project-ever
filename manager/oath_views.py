from django.shortcuts import render
from requests import post, get
from book_shop.settings import GIT_CLIENT_ID, GIT_CLIENT_SECRET
from manager.models import AccountUser


def brazzers_view(request):
    url = f"https://github.com/login/oauth/authorize?client_id={GIT_CLIENT_ID}"
    return render(request, "brazzers.html", {"url": url})


def brazzers_callback(request):
    code = request.GET.get("code")
    url = f"https://github.com/login/oauth/access_token?client_id={GIT_CLIENT_ID}&client_secret={GIT_CLIENT_SECRET}&code={code}"
    response = post(url, headers={'Accept': 'application/json'})
    access_token = response.json()['access_token']
    url = "https://api.github.com/user"
    response = get(url, headers={'Authorization': f'token {access_token}'})
    login = response.json()['login']
    url = f"https://api.github.com/users/{login}/repos"
    response = get(url)
    repos = [i['name'] for i in response.json()]
    if request.user.is_authenticated:
        au = AccountUser(user=request.user, github_account=login)
        au.github_repos = repos
        au.save()
    return render(request, "brazzers.html", {'data': repos})
