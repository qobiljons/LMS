import psycopg2


def main():
    conn = psycopg2.connect('postgres://avnadmin:AVNS_ECdStPudvotQYrfyMPs@pg-2e26136-qobiljons.i.aivencloud.com:28015/defaultdb?sslmode=require')

    query_sql = 'SELECT VERSION()'

    cur = conn.cursor()
    cur.execute(query_sql)

    version = cur.fetchone()[0]
    print(version)


if __name__ == "__main__":
    main()