# raspi-login-checker-server

## 実行手順(開発環境)

### インストール

```
$ pipenv install 

$ mysql -u [username] -p [password] -e 'create database raspi_login_checker;'

$ export FLASK_CONFIG_FILE=`pwd`/config/development.py

$ pipenv run python init_database.py
```

### 実行

```
$ export FLASK_APP=run.py

$ export FLASK_DEBUG=1

$ pipenv run flask run
```
