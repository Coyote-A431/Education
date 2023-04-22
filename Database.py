import psycopg2


class DatabaseClass:

    def __init__(self, settings_init):
        self.host = settings_init[0]
        self.port = settings_init[1]
        self.database = settings_init[2]
        self.user = settings_init[3]
        self.password = settings_init[4]
        self.connect = self.connection()
        self.cursor = self.connect.cursor()

    def connection(self):
        try:
            connect = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password
            )
            return connect
        except Exception as err:
            print(err)

    def insert(self, df, scheme_name, table_name):
        try:
            insert_query = 'insert into ' + scheme_name + '.' + table_name + """ (city, state_code, country_code, 
            processed_dttm, temp_min, temp_max) values(%s, %s, %s, %s, %s, %s)"""
            for index, row in df.iterrows():
                self.cursor.execute(insert_query, (row['city'], row['state_code'], row['country_code'], row['processed_dttm'], row['temp_min'], row['temp_max']))
            self.connect.commit()
        except Exception as err:
            print(err)

    def disconnection(self):
        if self.connect:
            self.cursor.close()
            self.connect.close()
