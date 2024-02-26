import pymysql.cursors
from dotenv import  dotenv_values

env_vars = dotenv_values(".env")
print(str(env_vars['MYSQL_PASSWORD']))
print("mysql",MYSQL_PASSWORD)
# MySQLに接続
mydb = pymysql.connect(
    host="localhost",
    user="root",
    password=str(env_vars['MYSQL_PASSWORD'])

)

# カーソルを取得
cursor = mydb.cursor()


# usersテーブルを作成するクエリ
create_users_table = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(30) NOT NULL,
    email VARCHAR(255),
    password_hash VARCHAR(255),
    image LONGBLOB,
    caption VARCHAR(1000),
    follow_count INT DEFAULT 0,
    follower_count INT DEFAULT 0,
    randaction_count INT DEFAULT 0
)
"""

# postsテーブルを作成するクエリ
create_posts_table = """
CREATE TABLE IF NOT EXISTS posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    caption VARCHAR(1000),
    image_data LONGBLOB NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    user_id INT NOT NULL,
    fav_count INT DEFAULT 0,
    mission_title VARCHAR(1000),
    FOREIGN KEY (user_id) REFERENCES users(id)
)
"""

# favoritesテーブルを作成するクエリ
create_favorites_table = """
CREATE TABLE IF NOT EXISTS favorites (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    post_id INT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (post_id) REFERENCES posts(id)
)
"""

# missionsテーブルを作成するクエリ
create_missions_table = """
CREATE TABLE IF NOT EXISTS missions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(225) NOT NULL DEFAULT 'ミッション',
    count INT NOT NULL DEFAULT 0,
    start_time DATETIME,
    end_time DATETIME
)
"""

# followsテーブルを作成するクエリ
create_follows_table = """
CREATE TABLE IF NOT EXISTS follows (
    id INT AUTO_INCREMENT PRIMARY KEY,
    follower_id INT NOT NULL,
    followed_id INT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (follower_id) REFERENCES users(id),
    FOREIGN KEY (followed_id) REFERENCES users(id)
)
"""
#テーブル作成

cursor.execute('DROP DATABASE IF EXISTS randaction')
cursor.execute('CREATE DATABASE IF NOT EXISTS randaction')
cursor.execute('USE randaction')

# テーブルを作成するクエリを実行
cursor.execute(create_users_table)
cursor.execute(create_posts_table)
cursor.execute(create_favorites_table)
cursor.execute(create_missions_table)
cursor.execute(create_follows_table)

# 変更をコミット
mydb.commit()

# 接続を閉じる
mydb.close()

