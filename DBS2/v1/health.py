import json

import psycopg2
from django.http import HttpResponse
from DBS2.settings import env


def index(request):

    database_connection = psycopg2.connect('host=' + env('DATABASE') + ' port=' + env('DATABASE_PORT') + ' user=' + env(
        'DATABASE_LOGIN') + ' password=' + env('DATABASE_PW') + ' dbname=' + env('DATABASE_NAME'))
    cursor = database_connection.cursor()

    query = "SELECT VERSION();"
    cursor.execute(query)
    reply = cursor.fetchall()

    query2 = "SELECT pg_database_size('dota2')/1024/1024 as dota2_db_size;"
    cursor.execute(query2)
    reply2 = cursor.fetchall()

    cursor.close()
    database_connection.close()

    response = {
        "pgsql": {
            "version": reply[0][0],
            "dota2_db_size": reply2[0][0]

        }
    }

    return HttpResponse(json.dumps(response),content_type='application/json')



