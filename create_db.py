import mysql.connector

# MySQLに接続
mydb = mysql.connector.connect(
  host="randaction.mysql.pythonanywhere-services.com",
  user="randaction",
  password="2024-spring-hackathon-group2",
  database="randaction$randaction"
)

mycursor = mydb.cursor()

# usersテーブルの作成クエリ
create_users_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(30) NOT NULL,
    email VARCHAR(255) UNIQUE,
    password VARCHAR(255) NOT NULL,
    image LONGBLOB
)
"""


# missionsテーブルの作成クエリ
create_missions_table_query = """
CREATE TABLE IF NOT EXISTS missions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(225) NOT NULL DEFAULT 'ミッション',
    content VARCHAR(1000),
    count INT NOT NULL DEFAULT 0,
    start_time DATETIME,
    end_time DATETIME
)
"""

# postsテーブルの作成クエリ
create_posts_table_query = """
CREATE TABLE IF NOT EXISTS posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    content VARCHAR(1000),
    image_data LONGBLOB NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_id INT NOT NULL,
    mission_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (mission_id) REFERENCES missions(id)
)
"""


# favoritesテーブルの作成クエリ
create_favorites_table_query = """
CREATE TABLE IF NOT EXISTS favorites (
    user_id INT NOT NULL,
    post_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id, post_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (post_id) REFERENCES posts(id)
)
"""

# followsテーブルの作成クエリ
create_follows_table_query = """
CREATE TABLE IF NOT EXISTS follows (
    follower_id INT NOT NULL,
    followed_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (follower_id, followed_id),
    FOREIGN KEY (follower_id) REFERENCES users(id),
    FOREIGN KEY (followed_id) REFERENCES users(id)
)
"""

# テーブルの作成クエリをリストにまとめる
create_table_queries = [
    create_users_table_query,
    create_missions_table_query,
    create_posts_table_query,
    create_favorites_table_query,
    create_follows_table_query
    ]

# クエリを実行してテーブルを作成
for query in create_table_queries:
    mycursor.execute(query)

# 変更を確定
mydb.commit()
mycursor.close()
mydb.close()