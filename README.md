# ScratchからAPIをrequestするための拡張機能
参考： 
http://www.moonmile.net/blog/archives/10331
## 初期設定
scratch-vmとscratch-guiの初期設定を行ってください。 
※nodejs（scratch）とpython3（API server）が必要です。condaがインストールされている場合はconda_env.ymlでnodejsとAPIで使用しているpythonライブラリのインストールが可能です
```conda
conda env create -f conda_env.yml
```

scratch-vmとscratch-guiの初期設定についてはnodejsをインストール後、scratch-vmとscratch-guiのREADME.mdを確認し初期設定を進めてください。

## 使用方法
初期設定後、scratch-guiを起動した状態でAPI serverを起動してください
```
# scratch-guiの起動
cd scratch-gui
npm start

# API serverの起動
uvicorn api:app --host 0.0.0.0 --reload
```

## ScratchからのAPI呼び出し
「参考」サイトに記載されている「実行してみる」の手順にて呼び出し可能<br>
api.py（Fastapi）を編集することで、API接続後の処理を作成することが可能です。<br>
Fastapiの使用方法については[公式サイト](https://fastapi.tiangolo.com/ja/, "Fastapi")を確認してください。

# Reference
https://github.com/llk/scratch-vm<br>
https://github.com/llk/scratch-gui<br>
http://www.moonmile.net/blog/archives/10331
