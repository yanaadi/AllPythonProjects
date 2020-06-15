
import sqlite3

import base64
import time

from sqlite3 import Error


class StoreManager:

    def __init__(self, username, website, password):

        self.username = username

        self.website = website

        self.password = password

    def store(self):

        try:

            conn = sqlite3.connect('passwd.db')

            table = """
            CREATE TABLE PasswordManager(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            website TEXT NOT NULL,
            password TEXT NOT NULL
            );
            """
            cur = conn.execute(table)

            print('The table has been created...')

        except Error as e:

            conn = sqlite3.connect('passwd.db')

            print('Connected to Database')

            cur = conn.cursor()

            check_query_1 = 'SELECT %s FROM PasswordManager WHERE %s=? AND %s=?' % (
                'password', 'username', 'website')

            cur.execute(check_query_1, (self.username, self.website))

            conn.commit()

            value = cur.fetchall()

            print('Checking if password already exists for username {} and website {}'.format(
                self.username, self.website))

            time.sleep(1)

            if value:

                print('It seems a password already exists for the username {} for the website {}'.format(
                    self.username, self.website))

                time.sleep(1)

                print('Would you like to update the existing password ? (y/n)')

                update = input()

                if update == 'y':

                    try:

                        b = bytes(self.password, 'utf-8')

                        base64_b = base64.b64encode(b)

                        update_query = 'UPDATE PasswordManager SET password = ? WHERE %s = ? AND %s = ?' % (
                            'username', 'website')

                        cur = conn.cursor()

                        cur.execute(update_query, (base64_b, self.username, self.website))

                        conn.commit()

                        print('The Password has been updated Successfully !!!')

                        conn.close()

                    except Error as e:

                        print('Error : {}'.format(e))

            else:

                print('No existing passwords found for username {} for the website {}'.format(
                    self.username, self.website))

                time.sleep(1)

                try:

                    store_query = """
                    INSERT INTO
                    PasswordManager(username,website,password)
                    VALUES
                    (?, ?, ?)
                    """

                    b = bytes(self.password, 'utf-8')

                    base64_b = base64.b64encode(b)

                    entry = (self.username, self.website, base64_b)

                    cur.execute(store_query, entry)

                    print('Record Added to Database Successfully')

                    conn.commit()

                    conn.close()

                except Error as e:

                    print('{} Error..'.format(e))


class GetManager:

    def __init__(self, username, website):

        self.username = username

        self.website = website

    def retrieve(self):

        try:

            conn = sqlite3.connect('passwd.db')

            print('Connected to Database')

            cur = conn.cursor()

            get_query = 'SELECT %s FROM PasswordManager WHERE %s=? AND %s=?' % (
                'password', 'username', 'website')

            cur.execute(get_query, (self.username, self.website))

            conn.commit()

            value = cur.fetchall()

            value = value[0][0]

            base64_b = base64.b64decode(value)

            print('The password is {}'.format(base64_b.decode('utf-8')))

        except Error as e:

            print('{} error occured'.format(e))


def existing_master_db(user_, master_):

    global success

    success = False

    try:

        connect = sqlite3.connect('passwd.db')

        create = """
        CREATE TABLE Master(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
        );
        """

        cur = connect.cursor()

        cur.execute(create)

        connect.commit()

        print('Table Created..')

    except Error as e:

        connect = sqlite3.connect('passwd.db')

        cur = connect.cursor()

        select = 'SELECT %s FROM Master WHERE %s=?' % ('password', 'username')

        cur.execute(select, (user_,))

        connect.commit()

        fetch = cur.fetchall()

        if fetch:

            if fetch[0][0] == master_:

                print('Successfully Logged in')

                success = True

                time.sleep(1)

            else:

                success = False
        else:

            success = False

    return success


def new_master_db(user_, master_):

    try:

        connect = sqlite3.connect('passwd.db')

        create = """
        CREATE TABLE Master(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
        );
        """

        cur = connect.cursor()

        cur.execute(create)

        print('Table Created..')

    except Error as e:

        insert = """
        INSERT INTO
        Master(username,password)
        VALUES
        (?, ?)
        """

        connect = sqlite3.connect('passwd.db')

        cur = connect.cursor()

        cur.execute(insert, (user_, master_,))

        connect.commit()

        print('Record added to database successfully !!!')


def new():

    global username

    global website

    global password

    print('To store a new password provide the following :\n')

    print('1. Username\n2. Website\n3. Password\n')

    username = input()

    website = input()

    password = input()

    return username, website, password


def new_():

    global username

    global website

    print('To get password provide the following :\n')

    print('1. Username\n2. Website\n')

    username = input()

    website = input()

    return username, website


if __name__ == '__main__':

    while True:

        print('*'*50 + '\n')

        print('Welcome to Password Manager !!!\n'.center(55))

        print('*'*50 + '\n')

        print('1.Existing User\n')

        print('2.New User\n')

        try:

            option = int(input('Input:(1 or 2)\n'))

            if option == 1:

                user_ = input('Enter your username\n')

                master_ = input('Please enter your master password to proceed further..\n')

                existing_master_db(user_, master_)

                if success:

                    print('1. Store Password\n2. Get Password\n')

                    try:

                        option1 = int(input('Input:(1 or 2)\n'))

                        if option1 == 1:

                            new()

                            m = StoreManager(username, website, password)

                            m.store()

                            break

                        else:

                            new_()

                            m = GetManager(username, website)

                            m.retrieve()

                            break

                    except Exception as e:

                        print('Invalid Input Detected. Enter a valid Input')

                        time.sleep(1)

                else:

                    print('Incorrect username or password.Try again')

                    time.sleep(1)

            else:

                user_ = input('Please create your username\n')

                master_ = input('Please create your master password\n')

                new_master_db(user_, master_)

                print('New account created.')

                time.sleep(1)

                user_ = input('Enter your username\n')

                master_ = input('Please enter your master password to proceed further..\n')

                existing_master_db(user_, master_)

                if success:

                    print('Would you like to store a password ? (y/n)\n')

                    option1 = input()

                    if option1 == 'y':

                        new()

                        m = StoreManager(username, website, password)

                        m.store()

                        break

                    elif option1 == 'n':

                        break

                    else:

                        print('Invalid Input Detected.Enter a valid Input')

                        time.sleep(1)

                else:

                    print('Incorrect username or password. Try again')

                    time.sleep(1)

        except Exception as e:

            print('Invalid Input Detected. Enter a valid Input')

            time.sleep(1)
