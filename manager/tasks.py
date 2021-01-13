from celery import shared_task
from requests import get
from manager.models import AccountUser


@shared_task
def check_users():
    git_hub_users = AccountUser.objects.all()
    for user in git_hub_users:
        url = f"https://api.github.com/users/{user.github_account}/repos"
        response = get(url)
        repos = [i['name'] for i in response.json()]
        user.github_repos = repos
        user.save()
