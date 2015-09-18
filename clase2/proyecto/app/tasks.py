from celery import task


@task
def calculo():
    j = 1
    for i in xrange(100000):
        if j % 2 and i:
            j *= i
        else:
            j += 1

    print j
