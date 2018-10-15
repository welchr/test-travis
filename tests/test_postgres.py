import psycopg2

def test_quick():
  with psycopg2.connect(database="pytest", user="postgres", host="127.0.0.1", port="5432") as con:
    with con.cursor() as cur:
      cur.execute("select * from rest.assoc_master")
      results = cur.fetchall()
      assert len(results) > 1
