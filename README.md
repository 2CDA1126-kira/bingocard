# 基本仕様
- プログラミング言語：Python
- GUIライブラリ:tkinter
- ビンゴの参加者が手元の画面で利用するシステムのGUI.
- システムにアクセスすると,5x5のマス目にランダムな数字を表示する.
- マス目上の数字の範囲は一般的なビンゴのルールにしたがう.
- 生成したカードのパターンには,ハッシュ値により重複しない番号を付けて，同じパターンが出ないように管理する.
- マス目をタッチして,数字を選択できる.
- 選択した数字の並びをチェックして,リーチまたはビンゴを判定する.

# 使用方法
1. システムを起動するとハッシュ値のリストに被らないようなビンゴカードが生成される
1. マス目の値を選択すると背景色が黄色に変更され選択状態となる.
1. 間違えて選択した場合は再び選択すると背景色が白に戻り非選択状態となる.
1. マス目を選択するごとにリーチ,ビンゴの判定が行われ,条件を満たしている場合上部に表記される.
