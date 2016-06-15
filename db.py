#!/usr/bin/python

import json
import sqlite3
from decimal import Decimal

def select(dbname, itype):
    result = list()

    with sqlite3.connect(dbname) as con:
        cur = con.cursor()
        query = "SELECT Content FROM Cells WHERE Type=?"
        for d in cur.execute(query, (itype,)):
            pair = map(lambda (k, v): (Decimal(k), Decimal(v)), json.loads(d[0]).iteritems())
            result.append(dict(pair))

    return result

if __name__ == "__main__":
    for itype in ('type1', 'type2', 'type3'):
        print select('cells.db', itype)
