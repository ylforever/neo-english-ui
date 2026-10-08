import edge_tts
import asyncio

# 【二年级上册】定义课本音频文件参数
towfirs_array = [
    ["./src/audio/twofirst/unit6/", "How do people celebrate the Mid-Autumn Festival?", "1-how-do.mp3"],
    ["./src/audio/twofirst/unit6/", "Ready? Go!", "2-ready-go.mp3"],
    ["./src/audio/twofirst/unit6/", "Listen. Then point and say", "3-listen-then-point-and-say.mp3"],
    ["./src/audio/twofirst/unit6/", "play with lanterns", "4-play-with-lanterns.mp3"],
    ["./src/audio/twofirst/unit6/", "eat mooncakes", "5-eat-mooncakes.mp3"],
    ["./src/audio/twofirst/unit6/", "solve riddles", "6-solve-riddles.mp3"],
    ["./src/audio/twofirst/unit6/", "look at the moon", "7-look at the moon.mp3"],
    ["./src/audio/twofirst/unit6/", "Listen and chant", "8-Listen-and-chant.mp3"],
    ["./src/audio/twofirst/unit6/", "Read and guess", "9-read-and-guess.mp3"],
    ["./src/audio/twofirst/unit6/", "Sometimes it's a \"C\".", "10-sometimes-its-a-c.mp3"],
    ["./src/audio/twofirst/unit6/", "Sometimes it's an \"O\".", "11-sometimes-its-an-o.mp3"],
    ["./src/audio/twofirst/unit6/", "Sometimes you can see it", "12-sometimes-you-can-see-it.mp3"],
    ["./src/audio/twofirst/unit6/", "But sometimes you can't", "13-but-sometimes-you-cant.mp3"],
    ["./src/audio/twofirst/unit6/", "What is it?", "14-what-is-it.mp3"],
    ["./src/audio/twofirst/unit6/", "Story", "15-story.mp3"],
    ["./src/audio/twofirst/unit6/", "Guess and tick", "16-guess-and-tick.mp3"],
    ["./src/audio/twofirst/unit6/", "What may be in the story?", "17-what-may-be.mp3"],
    ["./src/audio/twofirst/unit6/", "The Mid-Autumn Festival", "18-the-mid-autumn-festival.mp3"],
    ["./src/audio/twofirst/unit6/", "The Mid‑Autumn Festival is a traditional Chinesefestival.", "19-the-mid-autumn-estivalis.mp3"],
    ["./src/audio/twofirst/unit6/", "Read and check", "20-read-and-check.mp3"],
    ["./src/audio/twofirst/unit6/", "We play with lanterns", "21-we-play-with-lanterns.mp3"],
    ["./src/audio/twofirst/unit6/", "Families have a big dinner together", "22-families-have-a.mp3"],
    ["./src/audio/twofirst/unit6/", "We eat mooncakes too.", "23-we-eat-mooncakes-too.mp3"],
    ["./src/audio/twofirst/unit6/", "They taste good.", "24-they-taste-good.mp3"],
    ["./src/audio/twofirst/unit6/", "At night, we look at themoon.", "25-at-night-we.mp3"],
    ["./src/audio/twofirst/unit6/", "It is big and bright.", "26-it-is-big-and-bright.mp3"],
    ["./src/audio/twofirst/unit6/", "What do you like about the Mid-Autumn Festival?", "27-what-do-you.mp3"],
    ["./src/audio/twofirst/unit6/", "Read and tick", "28-read-and-tick.mp3"],
    ["./src/audio/twofirst/unit6/", "What do people do at the Mid-Autumn Festival?", "29-what-do-people.mp3"],
    ["./src/audio/twofirst/unit6/", "Think and say", "30-think-and-say.mp3"],
    ["./src/audio/twofirst/unit6/", "What do you do with your parents at the Mid-Autumn Festival?", "31-what-do-you.mp3"],
    ["./src/audio/twofirst/unit6/", "I ... with my parents at theMid‑Autumn Festival. We ...", "32-i-with-my.mp3"],
    ["./src/audio/twofirst/unit6/", "Communicate", "33-communicate.mp3"],
    ["./src/audio/twofirst/unit6/", "Draw and say.", "34-draw-and-say.mp3"],
    ["./src/audio/twofirst/unit6/", "This is my mooncake.", "35-this-is-my-mooncake.mp3"],
    ["./src/audio/twofirst/unit6/", "There's a rabbit on it.", "36-theres-a-rabbit.mp3"],
    ["./src/audio/twofirst/unit6/", "This is my mooncake.", "37-this-is-my-mooncake.mp3"],
    ["./src/audio/twofirst/unit6/", "There's a(n) ... on it.", "38-theres-an.mp3"],
    ["./src/audio/twofirst/unit6/", "What kind of mooncakes do you like?", "39-what-kind-of.mp3"],
    ["./src/audio/twofirst/unit6/", "Extend", "40-extend.mp3"],
    ["./src/audio/twofirst/unit6/", "The story of Chang o", "41-the-story-of-change.mp3"],
    ["./src/audio/twofirst/unit6/", "Yi shoots down nine of the suns.", "42-yi-shoots-down.mp3"],
    ["./src/audio/twofirst/unit6/", "It's a pill to live forever.", "43-its-a-pill.mp3"],
    ["./src/audio/twofirst/unit6/", "There's only one pill.", "44-theres-only-one.mp3"],
    ["./src/audio/twofirst/unit6/", "You can't have it!", "45-you-cant-have.mp3"],
    ["./src/audio/twofirst/unit6/", "Chang o takes the pill.", "46-change-takes.mp3"],
    ["./src/audio/twofirst/unit6/", "She flies to the moon", "47-she-flies-to-the-moon.mp3"],
    ["./src/audio/twofirst/unit6/", "Now we look at the moon at the Mid-Autumn Festival.", "48-now-we-look.mp3"],
    ["./src/audio/twofirst/unit6/", "Can you see Chang o?", "49-can-you-see.mp3"],
    ["./src/audio/twofirst/unit6/", "What do you like about the story?", "50-what-do-you-like.mp3"],
    ["./src/audio/twofirst/unit6/", "", ".mp3"],
    ["./src/audio/twofirst/unit6/", "", ".mp3"],
    ["./src/audio/twofirst/unit6/", "", ".mp3"],
    ["./src/audio/twofirst/unit6/", "", ".mp3"],
    ["./src/audio/twofirst/unit6/", "", ".mp3"],
    ["./src/audio/twofirst/unit6/", "", ".mp3"],
    ["./src/audio/twofirst/unit6/", "", ".mp3"],
    ["./src/audio/twofirst/unit6/", "", ".mp3"],

];

# 【七年级上册】定义 生成语音文件的数据参数
words_array = [
    ["./src/audio/sevenfirst/words/unit2/", "diary", "17-diary.mp3"],
    ["./src/audio/sevenfirst/words/unit2/", "project", "18-project.mp3"],
    ["./src/audio/sevenfirst/words/unit2/", "poster", "19-poster.mp3"],
    ["./src/audio/sevenfirst/words/unit2/", "realize", "20-realize.mp3"],
    ["./src/audio/sevenfirst/words/unit2/", "luckily", "21-luckily.mp3"],
    ["./src/audio/sevenfirst/words/unit2/", "just", "22-just.mp3"],
    ["./src/audio/sevenfirst/words/unit2/", "presentation", "23-presentation.mp3"],
    ["./src/audio/sevenfirst/words/unit2/", "mood", "24-mood.mp3"],
    ["./src/audio/sevenfirst/words/unit2/", "mind", "25-mind.mp3"],
    ["./src/audio/sevenfirst/words/unit2/", "pack", "26-pack.mp3"],
    ["./src/audio/sevenfirst/words/unit2/", "celebrate", "27-celebrate.mp3"],
    ["./src/audio/sevenfirst/words/unit2/", "success", "28-success.mp3"],
    ["./src/audio/sevenfirst/words/unit2/", "rocky", "29-rocky.mp3"],
    ["./src/audio/sevenfirst/words/unit2/", "do the dishes", "30-do-the-dishes.mp3"],
    ["./src/audio/sevenfirst/words/unit2/", "junior high school", "31-junior-high-school.mp3"],
    ["./src/audio/sevenfirst/words/unit2/", "take part in", "32-take-part-in.mp3"],
    ["./src/audio/sevenfirst/words/unit2/", "look forward to", "33-look-forward-to.mp3"],
    ["./src/audio/sevenfirst/words/unit2/", "daily life", "34-daily-life.mp3"],
    ["./src/audio/sevenfirst/words/unit2/", "go to bed", "35-go-to-bed.mp3"],
    ["./src/audio/sevenfirst/words/unit2/", "get up", "36-get-up.mp3"],
    ["./src/audio/sevenfirst/words/unit2/", "on foot", "37-on-foot.mp3"],
    ["./src/audio/sevenfirst/words/unit2/", "full of energy", "38-full-of-energy.mp3"],
    ["./src/audio/sevenfirst/words/unit2/", "get … ready for", "39-get-ready-for.mp3"],
    ["./src/audio/sevenfirst/words/unit2/", "put on", "40-put-on.mp3"],
    ["./src/audio/sevenfirst/words/unit2/", "clean up", "41-clean-up.mp3"],
    ["./src/audio/sevenfirst/words/unit2/", "pick up", "42-pick-up.mp3"],
    
    # 第三单元单词和短语
    ["./src/audio/sevenfirst/words/unit3/", "footprint", "1-footprint.mp3"],
    ["./src/audio/sevenfirst/words/unit3/", "wet", "2-wet.mp3"],
    ["./src/audio/sevenfirst/words/unit3/", "deep", "3-deep.mp3"],
    ["./src/audio/sevenfirst/words/unit3/", "sandy", "4-sandy.mp3"],
    ["./src/audio/sevenfirst/words/unit3/", "kick", "5-kick.mp3"],
    ["./src/audio/sevenfirst/words/unit3/", "town", "6-town.mp3"],
    ["./src/audio/sevenfirst/words/unit3/", "feature", "7-feature.mp3"],
    ["./src/audio/sevenfirst/words/unit3/", "south", "8-south.mp3"],
    ["./src/audio/sevenfirst/words/unit3/", "clear", "9-clear.mp3"],
    ["./src/audio/sevenfirst/words/unit3/", "loudly", "10-loudly.mp3"],
    ["./src/audio/sevenfirst/words/unit3/", "thunder", "11-thunder.mp3"],
    ["./src/audio/sevenfirst/words/unit3/", "lightning", "12-lightning.mp3"],
    ["./src/audio/sevenfirst/words/unit3/", "fresh", "13-fresh.mp3"],
    ["./src/audio/sevenfirst/words/unit3/", "gather", "14-gather.mp3"],
    ["./src/audio/sevenfirst/words/unit3/", "peaceful", "15-peaceful.mp3"],
    ["./src/audio/sevenfirst/words/unit3/", "snake", "16-snake.mp3"],
    ["./src/audio/sevenfirst/words/unit3/", "through", "17-through.mp3"],
    ["./src/audio/sevenfirst/words/unit3/", "part", "18-part.mp3"],
    ["./src/audio/sevenfirst/words/unit3/", "article", "19-article.mp3"],
    ["./src/audio/sevenfirst/words/unit3/", "reason", "20-reason.mp3"],
    ["./src/audio/sevenfirst/words/unit3/", "alive", "21-alive.mp3"],
    ["./src/audio/sevenfirst/words/unit3/", "sandcastle", "22-sandcastle.mp3"],
    ["./src/audio/sevenfirst/words/unit3/", "follow", "23-follow.mp3"],
    ["./src/audio/sevenfirst/words/unit3/", "divide", "24-divide.mp3"],
    ["./src/audio/sevenfirst/words/unit3/", "decide", "25-decide.mp3"],
    ["./src/audio/sevenfirst/words/unit3/", "crop", "26-crop.mp3"],
    ["./src/audio/sevenfirst/words/unit3/", "culture", "27-culture.mp3"],
    ["./src/audio/sevenfirst/words/unit3/", "local", "28-local.mp3"],
    ["./src/audio/sevenfirst/words/unit3/", "tradition", "29-tradition.mp3"],
    ["./src/audio/sevenfirst/words/unit3/", "continue", "30-continue.mp3"],
    
    ["./src/audio/sevenfirst/words/unit3/", "have picnics", "31-have-picnics.mp3"],
    ["./src/audio/sevenfirst/words/unit3/", "work one's land", "32-work-ones-land.mp3"],
    ["./src/audio/sevenfirst/words/unit3/", "take a trip", "33-take-a-trip.mp3"],
    ["./src/audio/sevenfirst/words/unit3/", "solar term", "34-solar-term.mp3"],
    ["./src/audio/sevenfirst/words/unit3/", "in fact", "35-in-fact.mp3"],
    ["./src/audio/sevenfirst/words/unit3/", "be divided into", "36-be-divided-into.mp3"],
    ["./src/audio/sevenfirst/words/unit3/", "be based on", "37-be-based-on.mp3"],
    ["./src/audio/sevenfirst/words/unit3/", "play an important part in", "38-play-an-important-part-in.mp3"],

]

# voice="en-GB-SoniaNeural" 英式发音
# voice="en-US-JennyNeural" 美式发音

async def createAudioFile(arrays):
    for i in range(len(arrays)):
        ssml_text = arrays[i][1]
        if ssml_text == "":
            continue
        communicate = edge_tts.Communicate(ssml_text, voice="en-GB-SoniaNeural", rate="-40%")
        await communicate.save(arrays[i][0] + arrays[i][2])
        print(arrays[i][0] + "  "+ arrays[i][2])

async def run():
    # 创建七年级上册词语表音频文件 
    #await createAudioFile(words_array);
    await createAudioFile(towfirs_array);

asyncio.run(run())