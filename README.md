# hackathon-2024-spring-wireframe


# ローカル環境でテストする場合のmysql
0. mysqlをダウンロードする。Macユーザーでhomebrew使っているならHomeberwでダウンロードしてパスを通す
1. `pip install -r requirements.txt` をしてrequirements.txtにあるライブラリを全てダウンロードする
2. randaction という名前のdatabaseを作る
mysqlの画面で以下のコマンドを実行する
    ```mysql> CREATE DATABASE randaction;
    ```
3. USE randaction;
4. create_db.pyを実行する
5. mysqlで、SHOW tablesをしてtableが作成されたかを確認する