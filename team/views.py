import json

from django.http.response import HttpResponseForbidden, HttpResponseBadRequest, HttpResponseNotFound, HttpResponse

from .models import Group, Team, TeamCharacter, TeamBossDamage


class HttpUnauthorized(HttpResponse):
    status_code = 401


def group_add(request):
    """
    添加分组
    URL: /api/group_add/
    Method: POST
    Permission: 登录用户
    param:
        name: 组名
    """
    if request.method == 'POST':
        if not request.user.is_authenticated:
            # 未登录 401
            return HttpUnauthorized()
        try:
            query = json.loads(request.body)
        except json.decoder.JSONDecodeError:
            # 参数错误 400
            return HttpResponseBadRequest()
        group_name = query.get('name')
        Group.objects.create(name=group_name, owner=request.user)
        return HttpResponse()
    return HttpResponseNotFound()


def group_remove(request):
    """
    删除分组
    URL: /api/group_remove/
    Method: POST
    Permission: 登录用户
    Param:
        id: 分组id
    """
    if request.method == 'POST':
        if not request.user.is_authenticated:
            # 未登录 401
            return HttpUnauthorized()
        try:
            query = json.loads(request.body)
        except json.decoder.JSONDecodeError:
            # 参数错误 400
            return HttpResponseBadRequest()
        g_id = query.get('id')
        group = Group.objects.get(g_id=g_id)
        if not group:
            # 参数错误
            return HttpResponseBadRequest()
        group.delete()
        return HttpResponse()
    return HttpResponseNotFound()


def group_edit(request):
    """
    修改分组
    URL: /api/group_edit/
    Method: POST
    Permission: 登录用户
    Param:
        id: 分组id
        name: 组名
    """
    if request.method == 'POST':
        if not request.user.is_authenticated:
            # 未登录 401
            return HttpUnauthorized()
        try:
            query = json.loads(request.body)
        except json.decoder.JSONDecodeError:
            # 参数错误 400
            return HttpResponseBadRequest()
        g_id = query.get('id')
        if not Group.objects.filter(g_id=g_id):
            # 参数错误 400
            return HttpResponseBadRequest()
        group_name = query.get('name')
        group = Group.objects.get(g_id=g_id)
        try:
            group.name = group_name
            group.save()
            return HttpResponse()
        except ValueError:
            # 参数错误 400
            return HttpResponseBadRequest()
    return HttpResponseNotFound()


def team_add(request):
    """
    添加队伍
    URL: /api/team_add/
    Method: POST
    Permission: 登录用户
    param:
        g_id: 组id
        name: 队名
    """
    if request.method == 'POST':
        if not request.user.is_authenticated:
            # 未登录 401
            return HttpUnauthorized()
        try:
            query = json.loads(request.body)
        except json.decoder.JSONDecodeError:
            # 参数错误 400
            return HttpResponseBadRequest()
        g_id = query.get('g_id')
        team_name = query.get('name')
        Team.objects.create(name=team_name, g_id=g_id)
        return HttpResponse()
    return HttpResponseNotFound()


def team_remove(request):
    """
    删除队伍
    URL: /api/team_remove/
    Method: POST
    Permission: 登录用户
    Param:
        id: 队伍id
    """
    if request.method == 'POST':
        if not request.user.is_authenticated:
            # 未登录 401
            return HttpUnauthorized()
        try:
            query = json.loads(request.body)
        except json.decoder.JSONDecodeError:
            # 参数错误 400
            return HttpResponseBadRequest()
        t_id = query.get('id')
        team = Team.objects.get(t_id=t_id)
        if not team:
            # 参数错误
            return HttpResponseBadRequest()
        team.delete()
        return HttpResponse()
    return HttpResponseNotFound()


def team_edit(request):
    """
    修改分组
    URL: /api/team_edit/
    Method: POST
    Permission: 登录用户
    Param:
        id: 队伍id
        name: 队名
    """
    if request.method == 'POST':
        if not request.user.is_authenticated:
            # 未登录 401
            return HttpUnauthorized()
        try:
            query = json.loads(request.body)
        except json.decoder.JSONDecodeError:
            # 参数错误 400
            return HttpResponseBadRequest()
        t_id = query.get('id')
        team = Team.objects.get(t_id=t_id)
        if not team:
            # 参数错误 400
            return HttpResponseBadRequest()
        team_name = query.get('name')
        try:
            team.name = team_name
            team.save()
            return HttpResponse()
        except ValueError:
            # 参数错误 400
            return HttpResponseBadRequest()
    return HttpResponseNotFound()
