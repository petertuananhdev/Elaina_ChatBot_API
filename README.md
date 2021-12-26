# Hưỡng dẫn sử dụng Elaina Api
## Hưỡng dẫn cài
#### Không dùng replit
```
pip install git+https://github.com/duongtuan303030/elainaapi.git
```
#### Replit
```
python3 -m poetry add git+https://github.com/duongtuan303030/elainaapi.git
```
## Ví dụ
```python
import elainaapi
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='%')#thay `%` bằng cái gì cũng được

@bot.event
async def on_message(message):
  await bot.process_commands(message)
  if message.channel.id == 12332434513: #đổi 12332434513 bằng id kênh bạn muốn có chat bot
     out = elainaapi.chatbot(message.content, "Key chat bot")#Key chat bot lấy ở https://discord.gg/ff4FeE9gXc
     await message.reply(out)

client.run("Bot token")
```
