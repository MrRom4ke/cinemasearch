from CinemaSearch.cinemasearch.app.utils.manage_db import connect_db


def get_menu():
    """Запрос меню из БД"""
    conn = connect_db()
    sql = '''SELECT * FROM menu'''
    cur = conn.cursor()
    try:
        cur.execute(sql)
        res = cur.fetchall()
        if res:
            return res
    except:
        print('Error reading from DB')
    return []


def get_rubric():
    """Запрос рубрик"""
    conn = connect_db()
    sql = '''SELECT * FROM rubric'''
    cur = conn.cursor()
    try:
        cur.execute(sql)
        res = cur.fetchall()
        if res:
            return res
    except:
        print('Error reading from DB')
    return []