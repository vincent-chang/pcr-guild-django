from django.db import models


class Group(models.Model):
    """
    队伍分组
    """
    g_id = models.AutoField(primary_key=True)  # 组id
    name = models.CharField(max_length=16, default=u'group')  # 组名
    owner = models.ForeignKey('login.User', on_delete=models.CASCADE, related_name='group')  # 所属用户

    @property
    def detail(self):
        return {
            'id': self.g_id,
            'name': self.name
        }


class Team(models.Model):
    """
    队伍
    """
    t_id = models.AutoField(primary_key=True)  # 队伍id
    g_id = models.ForeignKey('team.Group', on_delete=models.CASCADE, related_name='team')  # 队伍所属组id
    name = models.CharField(max_length=16)  # 队名

    @property
    def detail(self):
        return {
            'id': self.t_id,
            'g_id': self.g_id,
            'name': self.name
        }


class TeamCharacter:
    """
    队伍中的队员
    """
    tc_id = models.AutoField(primary_key=True)  # 记录id
    t_id = models.ForeignKey('team.Team', on_delete=models.CASCADE, related_name='character')  # 队伍id
    c_id = models.CharField(max_length=16)  # 队员角色id

    @property
    def detail(self):
        return {
            'id': self.tc_id,
            't_id': self.t_id,
            'c_id': self.c_id
        }


class TeamBossDamage:
    """
    队伍对某个Boss的伤害记录
    """
    tbd_id = models.AutoField(primary_key=True)  # 记录id
    t_id = models.ForeignKey('team.Team', on_delete=models.CASCADE, related_name='damage')  # 队伍id
    b_id = models.CharField(max_length=16)  # Boss id
    damage = models.IntegerField()  # 伤害值
    damage_date = models.DateTimeField()  # 伤害发生时间

    @property
    def detail(self):
        return {
            'id': self.tbd_id,
            't_id': self.t_id,
            'damage': self.damage,
            'damage_time': self.damage_date
        }
