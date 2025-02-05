import asyncio
import traceback

from discord import Client, Intents
from discord.ext import tasks

import config
from logging_config import logger
from rss import new_rss_feeds
from summarize import summarize_from_url


class BotClient(Client):
    def __init__(self, intents: Intents) -> None:
        super().__init__(intents=intents)
        self.seconds = 3600

    async def on_ready(self):
        logger.info(f"login: {self.user.name} [{self.user.id}]")
        self.channel = self.get_channel(config.CHANNEL_ID)
        if self.channel is None:
            try:
                self.channel = await self.fetch_channel(config.CHANNEL_ID)
            except Exception as e:
                logger.exception(f"Channel取得エラー: {e}")
        self.rss.start()
        logger.info("Ready!")

    @tasks.loop(seconds=3600)
    async def rss(self):
        feed_url = "http://b.hatena.ne.jp/hotentry/it.rss"
        new_entries = new_rss_feeds(feed_url)
        if self.channel:
            for entry in new_entries:
                title = entry.get("title", "No Title")
                link = entry.get("link", None)
                if link is not None:
                    message = f"[{title}]({link})"
                    await self.channel.send(message)
                    logger.info("create summary")
                    try:
                        summary = await asyncio.wait_for(
                            summarize_from_url(link), timeout=1200
                        )
                    except TimeoutError:
                        summary = "要約処理がタイムアウトしました。"
                    except Exception as e:
                        summary = f"要約処理中にエラーが発生しました: {e}"
                        logger.exception(traceback.format_exc())
                    logger.info("end summary")
                    chunk_size = 2000
                    summary_messages = [
                        summary[i : i + chunk_size]
                        for i in range(0, len(summary), chunk_size)
                    ]
                    for message in summary_messages:
                        await self.channel.send(message)
        else:
            logger.warning(
                "チャンネルが設定されていないため、メッセージを送信できません。"
            )


intents = Intents.default()
intents.message_content = True
client = BotClient(intents=intents)


# Bot起動
client.run(config.DISCORD_TOKEN)
