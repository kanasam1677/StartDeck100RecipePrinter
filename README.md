# スタートデッキ100カードリスト印刷ツール

このツールは下記スタートデッキ100公式サイトに掲載された内容をカードサイズにまとめて印刷するツールです。

https://www.pokemon-card.com/ex/si/index.html

デッキナンバーを指定すると、そのデッキの説明とカードリストを取得しA4用紙にカードサイズにまとめて印刷します。
![出力サンプル](image/img1.png)
![出力物とカードのサイズ比較](image/img2.jpg)

# 注意

本ツールはWebスクレイピングにより私的利用のための複製を行うためのツールとして開発しております。

本ツールによって得られた結果を私的利用以外の目的
(e.g. 印刷物の販売、購入されたデッキのおまけとして配布する)に利用すると、
著作権法上の罪に問われる恐れがあります。

また、公式サイト様への負荷は最小限になるように設計しておりますが、過度な起動はおやめください。

MITライセンスに基づき、本ツールによって生じた損害に関して、一切の責任を負いかねます。

# 使い方

## 1.ダウンロード
左側のReleasesからbinのzipファイルをダウンロードし好きな場所に展開します。

## 2.デッキナンバー指定ファイルの作成
展開したフォルダ内に、下記のように印刷したいデッキナンバーを改行区切りで記述したテキストファイルを用意します。
デッキナンバー以外の内容は記述しないでください。
```
9
82
86
87
```
記述順に印刷されます。また、同じ番号を複数回記述すると複数印刷することができます。

## 3.印刷用PDFの作成
2.で作成したファイルを`StartDeck100RecipePrinter.exe`にドラッグアンドドロップします。
複数のファイルを同時にドラッグアンドドロップすることもできます。

しばらく待つと、`(ドラッグアンドドロップしたファイル名).pdf`が生成されます。

## 4.PDFの印刷
3.で生成されたPDFをPDFビューワーでA4用紙に印刷します。
Adobe Acrobat Readerでの動作を確認しております。

## 5.切り取り
印刷された紙を線に沿って切り取って完成です。

スタートデッキ100のデッキナンバーカードにカードスリーブとともに収めるなどご自由にご活用ください。
ぴったりサイズのスリーブにも収まります。
![スリーブにカードとともに収める](image/img2.jpg)

## うまく動作しないときは
エラーメッセージを確認するために、コマンドプロンプトやPowerShellから開いてみてください。
ドラッグアンドドロップの代わりにテキストファイル名を引数として与えます。
