# raspi-login-checker-server

## 開発

### インストール

```
$ pipenv install 

$ mysql -u [username] -p [password] -e 'create database raspi_login_checker;'

$ export FLASK_CONFIG_FILE=`pwd`/config/[利用する環境のconfig]

$ pipenv run python init_database.py
```

### 実行

```
$ export FLASK_APP=run.py

# DEBUGを有効にする場合
$ export FLASK_DEBUG=1

$ pipenv run flask run
```
