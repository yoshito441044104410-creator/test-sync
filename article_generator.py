"""
ガジェット系の短文記事を作って txt に保存するシンプルなツール（API は不要）。
"""

import random
from datetime import datetime
from pathlib import Path
from typing import Optional

# 目標となる文字数（本文＋見出しの合計の目安）
TARGET_LENGTH = 500

INTROS = [
    "最近注目のガジェットを、忙しい日々でも活用しやすい視点から整理してみました。買う前に知っておきたいポイントだけに絞っています。",
    "身の回りのデジタル機器が増えると、選択に迷うことも増えます。今回は失敗しない選び方のヒントと、楽しむコツを短くまとめます。",
    "コンパクトな機器ひとつで、暮らしや仕事が少しラクになることがあります。初心者にも分かりやすく、チェックリスト感覚で紹介します。",
]

GADGET_FOCUSES = [
    ("ワイヤレスイヤホン", (
        "音質だけでなく、装着感と電池の持ちが続くかどうかが長く付き合えるかの分かれ目です。接続は規格だけでなく、普段使う端末との相性も確認しましょう。",
        "外音取り込みやノイキャン機能の有無は、通勤や在宅それぞれで快適さが変わります。実店舗があるなら試聴だけでも差が体感しやすいです。",
    )),
    ("スマートウォッチ", (
        "健康や運動だけでなく、通知の見逃しや手ぶらでの支払いなど、場面によって便利さが変わります。まずは毎日使う機能が二つだけでも十分効果があります。",
        "画面の見やすさとバンドの調整がしやすさに直結します。アプリ側の操作性も一度触って確認してから選ぶと後悔が少なくなります。",
    )),
    ("モバイルバッテリー", (
        "容量が大きいほど重量も増えるので、通勤ならコンパクト重視、長旅なら安心の大容量という切り替えがおすすめです。ポート数も忘れずにチェックしましょう。",
        "急速充電に対応しているかは時間の短縮にもつながります。ご自身のケーブル規格やスマホの許容ワット数もセットで読めると説明書が読みやすくなります。",
    )),
    ("キーボード・マウス", (
        "打鍵は静かめのシャロー／タクタイルなど好みが分かれるので、可能なら店頭でタイプングしてみましょう。長時間仕事では手首のラインにも気をつけたいです。",
        "ワイヤレスはすっきりしますが電池や充電の手間があります。ケーブルの一本化だけでもデスク環境が整って集中しやすくなることがあります。",
    )),
    ("Wi‑Fi関連", (
        "速度表示よりも自宅での届きやすさと安定性が大切です。置き場所と干渉源を確認し、アプリでの測定を一度試すだけでも改善の糸口が見つかります。",
        "メッシュや中継器は家の間取りによって相性があります。コンセント直結型は設置が手軽で、広い空間でのカバーを広げやすいこともあります。",
    )),
]

OUTROS = (
    "最後は保証やサポート、返品条件も軽く目を通しておくと安心です。自分のライフスタイルに合わせて一つずつ試すことが、続けやすさの鍵になります。"
)

# 文字数調整や締めのバリエーション用の短文（足りないときだけ順に追加）
EXTRA_LINES = (
    "価格だけでなく、レビューの使い勝手やサポート情報もセットで確認するとミスマッチが減りやすいです。",
    "まずは小さく試せるモデルや返品しやすいルートがあるかだけでも、はじめの一歩が軽くなります。",
    "アップデート方針や互換性情報はメーカーサイトを一度見ておくだけでも後から迷いません。",
    "毎日触るものこそ優先順位を付け、「今いちばん困っていること」を一つだけ解決すると続きやすいです。",
)


def pick_paragraphs():
    """見出し用の話題と、本文に使う段落を決める。"""
    title, paragraphs = random.choice(GADGET_FOCUSES)
    choice = random.sample(paragraphs, k=min(2, len(paragraphs)))
    body_core = "".join(choice)
    return title, body_core


def build_article() -> str:
    """ランダムに要素を並べて記事全文を組み立てる。"""
    title, core = pick_paragraphs()
    intro = random.choice(INTROS)

    headline = f"【ガジェット視点】{title}で暮らしをちょっと便利に"

    parts = [headline, "", intro, "", core, "", OUTROS]
    article = "\n".join(parts)

    # 目標より短いときだけ、短文を順に追加しておよそ500字に寄せる
    extras = list(EXTRA_LINES)
    random.shuffle(extras)
    while len(article) < TARGET_LENGTH - 35 and extras:
        article = article.rstrip() + "\n\n" + extras.pop()

    return article


def save_article(text: str, directory: Optional[Path] = None) -> Path:
    """記事を txt で保存して、保存パスを返す。"""
    folder = directory or Path(__file__).resolve().parent
    folder.mkdir(parents=True, exist_ok=True)
    fname = datetime.now().strftime("article_gadget_%Y%m%d_%H%M%S.txt")
    path = folder / fname
    path.write_text(text, encoding="utf-8")
    return path


def main() -> None:
    article = build_article()
    saved = save_article(article)
    print("記事を保存しました:")
    print(saved)
    print()
    print("--- 内容プレビュー ---")
    print(article[:300] + ("..." if len(article) > 300 else ""))
    print()
    print(f"(合計 {len(article)} 文字)")


if __name__ == "__main__":
    main()
