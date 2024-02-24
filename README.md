# hackathon-2024-spring-wireframe


# ローカル環境でテストする場合のmysql
0. mysqlをダウンロードする。Macユーザーでhomebrew使っているならHomeberwでダウンロードしてパスを通す
1. pip install requirements.txtをしてrequirements.txtにあるライブラリを全てダウンロードする
2. randaction という名前のdatabaseを作る(CREATE DATABASEコマンド)
3. USE randaction;
4. create_db.pyを実行する
5. mysqlで、SHOW tablesをしてtableが作成されたかを確認する