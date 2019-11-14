# 忙しい人向け使い方
詳細は以下のページで説明

http://testerchan.hatenadiary.com/entry/2019/11/14/001443


## kubernetesのインストールをしておく
macでしたらdockerアイコンの右クリック→preference→kubernetesでチェックを入れればインストールが始まります。

## docker imageのbuild
seleniumディレクトリに移動。

そこで以下を実行。

初回のみで大丈夫です。

```
 $ docker-compose build
 ```

## kubernetes起動

以下を実行

```
$ docker stack deploy --orchestrator=kubernetes -c docker-compose.yml kube
```

## sample.pyの実行

まずは以下を実行

```
$ kubectl get pods
```

これでpodのnameがわかるのでpythonのpodのnameをコピーしておく

次に以下を実行

```
$ kubectl exec -it コピーしたname python /root/script/sample.py
```

## 確認

macであれば画面共有から確認できる。

画面共有で、localhost:5901と入力した後、パスワードでsecretを入力。

## 終了

以下を入力

```
$ docker stack rm --orchestrator=kubernetes kube
```

