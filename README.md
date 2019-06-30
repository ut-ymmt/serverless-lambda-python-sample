# serverless-lambda-python-sample
serverless frameworkのサンプルテンプレート

## serverless framework install
[公式サイト](https://serverless.com/)の導入手順を参考にコマンドをインストール

```
# Install serverless globally
npm install serverless -g
```

## library install
開発に必要なライブラリをインストール

```
# 新規プラグインインストール
sls install plugin -n <plugin_name>

# serverless frameworkのプラグインをインストール
npm install

# 依存関係のライブラリをインストール
pip install -r requirements.txt
```

## deploy


全体をデプロイ
```
serverless deploy [options: --profile <aws_profile>]
```

必要なFunctionのみデプロイ
```
serverless deploy function -f <function_name> [options: --profile <aws_profile>]
```

### デプロイに必要なIAM権限
確認次第更新
