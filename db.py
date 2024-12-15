import sqlite3 as sq

from settings import connect, cursor, DBlist, Say


def WriteData(DB: int,
              st: str,
              value,
              qvest=None) -> None:
    '''
    :param st: столбец для записи.
    :param DB: 1 - Users 2 - Data.
    :param qvest: условия для записи, изначально ID, напишите "!" в начале, для передачи SQ3 условия.
    :param value: данные для записи.'''
    DB = DBlist[DB]
    if qvest is None:
        if Say:
            print(f'Write INTO `{DB}` {st} VALUES "{value}"')
        cursor.execute(f'INSERT INTO `{DB}` {st} VALUES (?)', value)
    qvest = str(qvest)
    if qvest[0] != "!":
        qvest = int(qvest)
        cursor.execute(f'''SELECT * FROM `{DB}` WHERE `ID` = "{qvest}"''')
        result = cursor.fetchone()
        if result is None:
            cursor.execute(f'INSERT INTO `{DB}` {st} VALUES (?)', value)
        else:
            cursor.execute(f'''UPDATE `{DB}` SET {
                           st} = ? WHERE `ID` = ?''', (value, qvest))
    else:
        qvest = qvest[1:]
        cursor.execute(f'''SELECT * FROM `{DB}` WHERE "{qvest}"''')
        result = cursor.fetchone()
        if result is None:
            cursor.execute(f'INSERT INTO `{DB}` {st} VALUES (?)', (value, ))
        else:
            cursor.execute(f'''UPDATE `{DB}` SET `{
                           st}` = ? WHERE  "{qvest}"''', (value, ))
    connect.commit()


def GetData(DB, st, qvest="!1=1"):
    '''
    :param St: столбец для чтения.
    :param DB: 1 - Users 2 - Data.
    :param Qest: условия для чтения, изначально ID, напишите "!" в начале, для передачи SQ3 условия.'''
    DB = DBlist[DB]
    qvest = str(qvest)
    if qvest[0] != "!":
        if Say:
            print(f'''SELECT `{st}` FROM {DB} WHERE `ID` = "{qvest}"''')
        cursor.execute(f'''SELECT `{st}` FROM {DB} WHERE `ID` = "{qvest}"''')
        result = cursor.fetchall()
        if Say:
            print("result", result)
        if result is None or result == [None]:
            return []
        else:
            return result
    elif st == "*":
        cursor.execute(f'''SELECT * FROM {DB}''')
        if result is None or result == [None]:
            return []
        else:
            return result
    elif qvest[0] == "!":
        qvest = qvest[1:]
        if Say:
            print(f'''SELECT {st} FROM {DB} WHERE {qvest}''')
        cursor.execute(f'''SELECT {st} FROM {DB} WHERE {qvest}''')
        result = cursor.fetchall()
        if Say:
            print("result", result)
        if result is None or result == [None]:
            return []
        else:
            return result
