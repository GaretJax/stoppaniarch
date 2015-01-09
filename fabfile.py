from fabric.api import local, task, hide, settings


@task
def up():
    with hide('running', 'stdout'):
        local('fig up -d --no-recreate db gulp')
    try:
        with hide('running'):
            local('fig up --no-recreate app server')
    except KeyboardInterrupt:
        with settings(warn_only=True), hide('running', 'stdout'):
            local('fig stop app server')

    with hide('everything'):
        local('fig rm --force app server')


@task
def shell():
    local('fig run --entrypoint=bash baseconfig')
