import sqlite3


class DataBase:
    __connection = None

    def get__connection(self):
        if DataBase.__connection is None:
            DataBase.__connection = sqlite3.connect('Users.db', check_same_thread=False)
        return DataBase.__connection

    def init_db(self, force: bool = False):
        conn = self.get__connection()
        c = conn.cursor()

        if force:
            c.execute('DROP TABLE IF EXISTS user_message')

        c.execute('''
			CREATE TABLE IF NOT EXISTS users (
				id          INTEGER PRIMARY KEY,
				user_id     INTEGER NOT NULL,
				status      TEXT NOT NULL
			)
			''')

        # save
        conn.commit()

    def add_user(self, user_id: int, status):
        conn = self.get__connection()
        c = conn.cursor()
        c.execute('INSERT INTO users (user_id, status) VALUES (?, ?)', (user_id, status,))
        conn.commit()

    def subscriber_exist(self, user_id):
        conn = self.get__connection()
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE (user_id) = ?', (user_id,))
        return c.fetchall()

    def get_users(self):
        conn = self.get__connection()
        c = conn.cursor()
        c.execute('SELECT * FROM users')
        rows = c.fetchall()
        user_ids = []
        for i in rows:
            user_ids.append(i[1])
        return user_ids

    def delete_user(self, user_id):
        conn = self.get__connection()
        c = conn.cursor()
        c.execute('DELETE FROM users WHERE (user_id) = ?', (user_id,))
        conn.commit()
