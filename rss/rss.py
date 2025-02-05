import feedparser


def load_seen_urls(filename: str) -> set[str]:
    """ファイルから既知のURLをセットとして読み込む"""
    try:
        with open(filename, encoding="utf-8") as f:
            seen = {line.strip() for line in f if line.strip()}
        return seen
    except FileNotFoundError:
        return set()


def save_seen_urls(filename: str, seen: set[str]) -> None:
    """更新後のURLセットをファイルに保存する"""
    with open(filename, "w", encoding="utf-8") as f:
        for url in seen:
            f.write(url + "\n")


def filter_new_entries(entries: list, seen: set[str]) -> list:
    """エントリーの中から、未確認（新規）のものだけを返す。
    各エントリーの 'link' をキーとして利用します。"""
    new_entries = []
    for entry in entries:
        url = entry.get("link")
        if url and url not in seen:
            new_entries.append(entry)
            seen.add(url)
    return new_entries


def new_rss_feeds(feed_url: str) -> list:
    seen_file = "seen_urls.txt"
    # 既知のURLを読み込み
    seen_urls = load_seen_urls(seen_file)
    feed = feedparser.parse(feed_url)
    new_entries = filter_new_entries(feed.entries, seen_urls)
    save_seen_urls(seen_file, [entry.get("link") for entry in feed.entries])
    return new_entries


def main():
    feed_url = "http://b.hatena.ne.jp/hotentry/it.rss"
    new_entries = new_rss_feeds(feed_url)

    if new_entries:
        print("新規の記事:")
        for entry in new_entries:
            title = entry.get("title", "No Title")
            link = entry.get("link", "No Link")
            published = entry.get("published", "No Publication Date")
            print("=" * 40)
            print(f"Title: {title}")
            print(f"Link: {link}")
            print(f"Published: {published}")
            print("=" * 40)
            print("")
    else:
        print("新規の記事はありません。")

    # 更新後のURLセットを保存


if __name__ == "__main__":
    main()
