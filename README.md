# file_converter

このツールは、MarkdownファイルをHTML形式に変換するスクリプトです。

## 必要条件
- Python 3.6 以上
- markdown ライブラリ


## 使用方法

以下のコマンドを実行してください：

```
python3 file_converter.py markdown <input_filepath> <output_filepath>
```

## 引数説明
<`input_filepath`>: 入力となるMarkdownファイルのパス
<`output_filepath`>: 出力するHTMLファイルのパス
※ 出力ファイルが指定できない場合は、同じディレクトリに output.html という名前で保存されます。

## 注意事項
- 入力ファイルが存在しない場合はエラーメッセージが表示されます。
- HTML出力には tables 拡張機能が含まれています。
