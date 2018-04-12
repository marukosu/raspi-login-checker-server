# raspi-login-checker-server

## 開発

### インストール

```
$ pipenv install 

$ pipenv run python init_database.py
```

### 実行

```
$ export FLASK_APP=run.py

# 開発環境のconfigを使用する場合
$ export FLASK_CONFIG_FILE=`pwd`/config/development.py

# DEBUGを有効にする場合
$ export FLASK_DEBUG=1

$ pipenv run flask run
```
