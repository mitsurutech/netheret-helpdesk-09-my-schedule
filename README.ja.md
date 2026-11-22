# Netheretヘルプデスク ステップ09：自分の予定

[English](README.md) | [Français](README.fr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [Deutsch](README.de.md)

授業のための作例です。16のステップで、小さな会社のITを支える架空の会社Netheretのために、ヘルプデスクのWebアプリを作っていきます。 このステップでは、Tier 2とTier 3のエンジニアに自分専用の予定表と、作業ごとの作業指示書を用意します。指示書には進み具合を記録します。

## このステップで加わるもの

`helpdesk/jobs.py` に：

- `/jobs/mine`：エンジニアの今日以降の作業を日ごとにまとめたもの。さらに、
  まだ「in progress」になっている過去の作業も表示します。
- `/jobs/<id>`：作業指示書。いつ、どこで、顧客の電話番号、
  指示の内容、そして依頼から生まれた作業なら顧客のもとの問題。
- `/jobs/<id>/progress`：エンジニアが作業を「in progress」か「done」に
  変え、メモを書きます。依頼から生まれた作業が完了すると、その依頼の
  タイムラインにメモが加わります。

`helpdesk/models.py` の `Job.can_be_seen_by()` と `Job.can_be_updated_by()` が、
誰が作業を見たり変えたりできるかのルールを1か所にまとめています。週表示と
指示書のページの両方がこれを使います。

## 動かしてみる

```
python -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
python seed.py
flask --app helpdesk run --debug
```

`tier2@netheret.example` か `tier3@netheret.example`（デモ用
パスワード `password123`）でサインインし、My scheduleを開きます。週表示から別の
エンジニアの作業を開こうとしてみてください。リンクはなく、アドレスを打ち込むと
403になります。

## 注目するところ

- `days.setdefault(day, []).append(job)`：リストを「リストの辞書」にまとめる
  短い書き方です。
- エンジニアは作業をキャンセルできません。フォームにその選択肢はなく、
  サーバーも拒否します。フォームは、使う人が書き換えられるからです。
- `finished_now`：タイムラインのメモは、作業が初めて完了になったときにだけ書かれ、
  メモを保存するたびには書かれません。

## このステップを学ぶ

これは **Task 2. Developing the solution** の16ステップ中のステップ9です。T Level Digital Software Developmentの無料レッスン（英語）のシリーズで、PythonとFlaskを使い、アジャイルのスプリントでNetheretのヘルプデスクを作ります。このステップのレッスンはこちらです：
[エンジニアの予定と作業指示書](https://mitsurutech.co.uk/resources/t-level/dsd-t2-09-my-schedule)。

- 前のステップ：[ステップ08「訪問作業のスケジュール」](https://github.com/mitsurutech/netheret-helpdesk-08-jobs)
- 次のステップ：[ステップ10「ナレッジベース」](https://github.com/mitsurutech/netheret-helpdesk-10-knowledge-base)
- [T Level Digitalの無料レッスン一覧](https://mitsurutech.co.uk/resources/t-level)
- [これらのレッスンをMitsuruTechでクラスに教える](https://mitsurutech.co.uk/ja/learning)、[料金を見る](https://mitsurutech.co.uk/ja/pricing)、
  [学校で無料の1年を始める](https://mitsurutech.co.uk/ja/signup)

## この作例について

T Level Digital Software Developmentの授業のための作例として、[Mitsuru Technologies](https://mitsurutech.co.uk/ja)（MitsuruTech）が書きました。
Netheret IT Support Solutionsの課題文はPearsonのサンプル評価資料によるものです。このコードと解説は私たち自身のもので、
PearsonやDepartment for Educationが公開、推奨、承認したものではありません。
「T Level」はDepartment for Educationの登録商標です。
