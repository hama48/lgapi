# simple-fastapi

## 起動方法
```bash
$ uvicorn app.main:app --reload
```

`:app`の前はソースのファイル名を指定する。  
例えばファイルが`./src/app.py`に格納されているなら`src.app`と指定する。  
  
ファイル名の指定が正しくないと以下のようにエラーが発生する。
```bash
Error loading ASGI app. Could not import module "app".
```
  
起動したら`http://localhost:8000`にアクセスする。  

## Swagger UIのドキュメント
`http://localhost:8000/docs`にアクセスすれば、Swagger UIのドキュメントが確認できる。  