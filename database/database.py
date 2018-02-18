# -*- coding: utf-8 -*-
# Winddows の場合は以下からダウンロード
# 　http://www.stickpeople.com/projects/python/win-psycopg/
# Python3.xの場合、unicode(row[1],'utf-8') は不要。
#
import psycopg2
import textwrap

try:
    cnn = psycopg2.connect("dbname=sandbox host=localhost user=postgres password=")
    cur = cnn.cursor()

    #試験データの整理
    pref_cd = 100
    sql = textwrap.dedent('''
    DELETE FROM t01prefecture WHERE PREF_CD >= %s
    ''').strip()

    cur.execute(sql, (pref_cd,))
    cnn.commit()

    print("単純なSELECT文==========================")
    from_id = 45
    to_id = 999
    sql = textwrap.dedent('''
    SELECT PREF_CD,PREF_NAME FROM t01prefecture
    WHERE PREF_CD BETWEEN %s AND %s
    ''').strip()
    cur.execute(sql , (from_id, to_id, ))
    rows = cur.fetchall()
    for row in rows:
        #print("%d %s" % (row[0], unicode(row[1],'utf-8')))
        print("%d %s" % (row[0], row[1]))

    print("コミットの試験==========================")
    pref_cd = 100
    pref_name = u"モテモテ国"
    cur.execute(u"""INSERT INTO t01prefecture(PREF_CD, PREF_NAME)
                VALUES (%s, %s)""" , (pref_cd, pref_name))

    pref_cd = 101
    pref_name = u"野望の国"
    cur.execute(u"""INSERT INTO t01prefecture(PREF_CD,PREF_NAME)
                VALUES (%s, %s)""" , (pref_cd, pref_name,))
    cnn.commit()

    sql = textwrap.dedent('''
    SELECT PREF_CD,PREF_NAME FROM t01prefecture
    WHERE PREF_CD BETWEEN %s AND %s
    ''').strip()
    cur.execute(sql, (from_id, to_id, ))
    rows = cur.fetchall()
    for row in rows:
        #print("%d %s" % (row[0],unicode(row[1],'utf-8')))
        print("%d %s" % (row[0],row[1]))


    print("ロールバックの試験==========================")
    pref_cd = 102
    pref_name = u"ロール"
    cur.execute(u"""INSERT INTO t01prefecture(PREF_CD,PREF_NAME)
                VALUES (%s, %s)""" , (pref_cd, pref_name,))

    cur.execute("""SELECT PREF_CD,PREF_NAME FROM t01prefecture
                WHERE PREF_CD BETWEEN %s AND %s""" , (from_id, to_id, ))
    rows = cur.fetchall()
    for row in rows:
        #print("%d %s" % (row[0], unicode(row[1],'utf-8')))
        print("%d %s" % (row[0], row[1]))

    print("-------------------------")
    cnn.rollback()
    cur.execute("""SELECT PREF_CD,PREF_NAME FROM t01prefecture
                WHERE PREF_CD BETWEEN %s AND %s""" , (from_id, to_id, ))
    rows = cur.fetchall()
    for row in rows:
        #print("%d %s" % (row[0], unicode(row[1],'utf-8')))
        print("%d %s" % (row[0], row[1]))

    print("ユーザー定義==========================")
    cur.execute("""SELECT * FROM test_sp(%s,%s)""" , (from_id, to_id, ))
    rows = cur.fetchall()
    for row in rows:
        #print("%d %s" % (row[0], unicode(row[1],'utf-8')))
        print("%d %s" % (row[0], row[1]))

    cur.close()
    cnn.close()

except (psycopg2.OperationalError) as e:
    print (e)
