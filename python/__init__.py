import datetime
import time
from collections.abc import Iterable
from typing import Tuple

import psycopg2

from db_types import News, Quantum, Tutor, Event


def connect(
        user: str = 'postgres',
        dbname: str = 'postgresdb',
        password: str = 'root',
        host: str = 'localhost',
        port: str = '5050') -> psycopg2.connect:
    try:
        print(4567)
        print()
        conn = psycopg2.connect(user=user, dbname=dbname, password=password, host=host, port=port)
        print(1234)
        with conn.cursor() as cur:
            cur.execute('select version();')

    except psycopg2.Error as e:
        raise ConnectionError(f'error with psql: {e}')

    return conn


def create_tables(conn: psycopg2.connect):
    queries = ['CREATE TABLE news (news_id integer, publication_time integer, name text preview_description text, '
               'description text, preview_photo_id integer)', 'CREATE TABLE quantum (quantum_id integer, name text,'
               'description text)', 'CREATE TABLE tutor (tutor_id integer, name text, description text, photo_id integer)',
               'CREATE TABLE event (event_id integer, name text, quantum_id integer, tutor_id integer, time_start'
               'integer, time_end integer)']

    with conn.cursor() as cur:
        for query in queries:
            cur.execute(query, (id,))
            data = cur.fetchone()
        conn.commit()


def delete_quantum(
        conn: psycopg2.connect,
        id: int):
    query = 'DELETE FROM quantum WHERE id=%s RETURNING 1'

    with conn.cursor() as cur:
        cur.execute(query, (id,))
        data = cur.fetchone()
        conn.commit()

    return bool(data)


def create_quantum(conn: psycopg2.connect,
                   quantum: Quantum):
    query = 'INSERT INTO event (name, quantum_id, tutor_id, time_start, time_end) VALUES (%s, %s, %s, %s, %s)' \
            ' RETURNING news_id;'

    with conn.cursor() as cur:
        try:
            cur.execute(query, (quantum.name, quantum.description))
        except psycopg2.errors.UniqueViolation:
            conn.commit()
            return False
        data = cur.fetchone()
        conn.commit()

    return bool(data)


def get_quantum_by_id(conn: psycopg2.connect,
                      id: int):
    query = 'SELECT * FROM quantum WHERE id = %s'

    with conn.cursor() as cur:
        cur.execute(query, (id,))
        data = cur.fetchone()

        if data and len(data) == 4:
            return Quantum(data[0], data[1], data[2])

        return Tutor(0, ..., ..., ...)


def get_tutor_by_id(conn: psycopg2.connect,
                    id: int):
    query = 'SELECT * FROM tutor WHERE id = %s'

    with conn.cursor() as cur:
        cur.execute(query, (id,))
        data = cur.fetchone()

        if data and len(data) == 4:
            return Tutor(data[0], data[1], data[2], data[3])

        return Tutor(0, ..., ..., ...)


def get_latest_n_news(conn: psycopg2.connect,
                      n: int):
    query = 'SELECT * FROM news ORDER BY publication_time LIMIT %s'  # порядок (reverse) проверить

    with conn.cursor() as cur:
        cur.execute(query, (n,))
        data = cur.fetchall()

        if data and len(data) == n:
            ret = []
            for i in data:
                ret.append(News(data[0], data[1], data[2], data[3], data[4]))
            return ret

        return [News(0, ..., ..., ...) for i in range(n)]


def create_news(conn: psycopg2.connect,
                news: News):
    query = 'INSERT INTO news (name, preview_description, description, preview_photo_id) VALUES (%s, %s, %s, %s)' \
            ' RETURNING news_id;'

    with conn.cursor() as cur:
        try:
            cur.execute(query, (news.name, news.preview_description, news.description, news.preview_photo_id))
        except psycopg2.errors.UniqueViolation:
            conn.commit()
            return False
        data = cur.fetchone()
        conn.commit()

    return bool(data)


def get_latest_events(conn: psycopg2.connect):
    query = 'SELECT * FROM event ORDER BY time_start WHERE time_start > %s'  # порядок (reverse) проверить

    with conn.cursor() as cur:
        cur.execute(query, (datetime.datetime.now() - datetime.timedelta(weeks=1),))
        data = cur.fetchall()

        if data and len(data) == 5:
            return News(data[0], data[1], data[2], data[3], data[4])

        return News(0, ..., ..., ...)


def create_event(conn: psycopg2.connect,
                 event: Event):
    query = 'INSERT INTO event (name, quantum_id, tutor_id, time_start, time_end) VALUES (%s, %s, %s, %s, %s)' \
            ' RETURNING news_id;'

    with conn.cursor() as cur:
        try:
            cur.execute(query, (event.name, event.quantum_id, event.tutor_id, event.time_start, event.time_end))
        except psycopg2.errors.UniqueViolation:
            conn.commit()
            return False
        data = cur.fetchone()
        conn.commit()

    return bool(data)


def edit_event():
    pass
a = connect()