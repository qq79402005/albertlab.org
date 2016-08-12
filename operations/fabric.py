from fabric.api import *
from fabric.context_managers import *
from fabric.contrib.console import confirm

env.user = 'root'
env.hosts = ['120.25.122.107']
env.password='Q19870816q'

# 上传文件任务
@task
def sync_task() :
    

    