import time
import sys

while True:
  command = input("Type 'help' for list of commands: ")

if command.lower() == "exit":
  print("See ya!")
  exit()

elif command == "time":
  print("The current time is:", datetime.datetime.now().strftime('%H:%M'))

elif command == "who are you":
  print("I'm Rogax, your cloud assistant created on Github and developed on Figma, how can I help you?")

elif command == "rap":
  print("""Sure! Here is a rap:
(Verse 1)
Yo, it's Rogax, the cloud in the sky,
Assistin’ every day, watch me fly high.
Got the power of the cloud, no need for delay,
I got knowledge, skills, all night and day.

I’m the future, AI with precision,
Helping you out with all your decisions.
Rogax got the answers, no matter the task,
Just ask away, I’m here, no need to mask.

(Chorus)
Rogax, Rogax, in the cloud we trust,
Helping you out, no need to adjust.
From the sky to your screen, I’m your guide,
With cloud-based power, I’m right by your side!

(Verse 2)
Need a fact, a question, or even a rhyme?
Rogax's got it, all in no time.
From science to tech, I’m the best in the biz,
Drop a query, I handle it, that's how I live.

Organizin’ your tasks, keepin’ you on track,
I bring the answers fast, never lookin’ back.
Savin’ the day with efficiency and style,
When you roll with Rogax, you’re goin' the mile.

(Chorus)
Rogax, Rogax, in the cloud we trust,
Helping you out, no need to adjust.
From the sky to your screen, I’m your guide,
With cloud-based power, I’m right by your side!

(Outro)
So if you need help, just call on Rogax,
The assistant in the cloud that’s never out of acts.
I’m here, I’m clear, with tech that’s so fly,
With Rogax by your side, you’re ready to ride!""")

elif command == "help":
  print("rap: making a rap time: getting time exit: quit who are you: introduce")
