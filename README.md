# hackathon-2024-spring-wireframe
2024年2月に開催したハッカソンのグループ2の作品 "Randaction(ランダクション)"です。

# 発表資料
https://www.canva.com/design/DAF9z1gpOr0/JRJO0h6-tjildBp6X0huGA/edit?utm_content=DAF9z1gpOr0&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton


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
