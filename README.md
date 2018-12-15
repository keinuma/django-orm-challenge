# Django Starter Template
## 用意するもの
- Docker
- Docker Compose
- Python 3.7.0 or later

## 起動方法
`.env.example` を修正して、`.env` ファイルを作成する

```bash
# 初めて起動する場合
$ docker-compose up --build

# イメージビルド後に起動する場合
$ docker-compose up

# コンテナを終了する場合
$ docker-compose down
```

## パッケージインストール方法
パッケージを追加でインストールしてみる

```bash
# コンテナに入る
$ docker-compose run backend bash

# パッケージインストール
$ pipenv install django-cors-headers
```
