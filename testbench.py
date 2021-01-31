import os
from lib.sliding_window import copycheck

datasetName = "adult_fiction"
# datasetName = "aynrand-anthem"
# datasetName = "beat_generation_novels"
# datasetName = "beat_generation_poems"
# datasetName = "beowulf"
# datasetName = "cyberpunk"
# datasetName = "douglasadams"
# datasetName = "fiction-plot-all"
# datasetName = "fiction"
# datasetName = "grimmsfairytales"
# datasetName = "hanschristiananderson"
# datasetName = "harukimurakami"
# datasetName = "henrydavidthorough-walden"
# datasetName = "hfwells-waroftheworlds"
# datasetName = "josephconrad-heartofdarkness"
# datasetName = "kafka-metamorphosis"
# datasetName = "maryshelly-frankenstein"
# datasetName = "murakami-novels"
# datasetName = "mythology"
# datasetName = "picturebooks"
# datasetName = "synthwave-chords"

text = """
“He’s in trouble,” said Skeet.

Kemper seemed to be impressed. “Maybe he should have a drink of water, or some kind of crack.”

Outside, someone in the crowd shouted, “For Dr. Arroway!” and for Dr. Stringson.

quickShip”He wouldn’t drink his beer,” Laurel said.

And with that, the conversation seemed to be abruptly broken off.

reportprint”Have to go,” Charles Freck said. seemed to be abruptly broken off.

reportprint”Have to go,” Charles Freck said. “I can’t talk, about this; you’ll have to carry on, meek as I am.” He managed, half-smile, to extricate himself and walk beside the flag captain, whom the captain over the flapple had promoted to “First Lieutenant” — in response to a hint that Charley might be about to tell a falsehood.

The vidphone booth operator, a female, said, “You are still on the flag, sir, but you are a hint that Charley might be about to tell a falsehood.

The vidphone booth operator, a female, said, “You are still on the flag, sir, but you are seeing a Miss Smith at the projector. Her brother is there and he made it clear by doing something that your flag says on the flagpole.”

The message Beresher held up and Charley turned to her. “Why?” he said. “How could they miss a connection with you?”

�Charley said, “I’ll tell you something,” and hung up the phone. The screen became dark and then it flicked on once more and Charley’s face filled it with message Beresher held up and Charley turned to her. “Why?” he said. “How could they miss a connection with you?”

�Charley said, “I’ll tell you something,” and hung up the phone. The screen became dark and then it flicked on once more and Charley’s face filled it with anguish. “Don’t blame me,” he said. “They had no choice; they got stuck in the prob system. And it’s infectious. The damn vistermans sure as hell didn’t have an idea what it was doing to people in my family! God, what a chance you had! But I guess they— the damn fools—letting the rest of us out … there’s a great biological advantage in intuition, don’t you agree?” He ceased talking, then, me,” he said. “They had no choice; they got stuck in the prob system. And it’s infectious. The damn vistermans sure as hell didn’t have an idea what it was doing to people in my family! God, what a chance you had! But I guess they— the damn fools—letting the rest of us out … there’s a great biological advantage in intuition, don’t you agree?” He ceased talking, then, and sat facing them. His arms, his shoulders—they were broad, muscular, on his good leg, but he sagged.

“What’s wrong, Captain?”

He looked at her.

Dong said, “He says, ‘No.’ .”

“But—he doesn’t mean that he doesn’t.”

“They mean it to him, I guess. Don’t you see? They’re all of us a lot older than he is— what it was doing to people in my family! God, what a chance you had! But I guess they— the damn fools—letting the rest of us out … there’s a great biological advantage in intuition, don’t you agree?” He ceased talking, then, and sat facing them. His arms, his shoulders—they were broad, muscular, on his good leg, but he sagged.

“What’s wrong, Captain?”

He looked at her.

Dong said, “He says, ‘No.’ .”

“But—he doesn’t mean that he doesn’t.”

“They mean it to him, I guess. Don’t you see? They’re all of us a lot older than he is—don’t we—you know.”

“I’m sorry,” Ben said, and crossed his face, covering his mouth.

�The Ship’s cop drew her gun. “I’ll kill him. I don’t think there’s any point in killing him.”

“But,” Dong said, “this is the middle of town; nobody will fire at anyone, now that he’s there. You have the direct conduit from this planet; if he dies—”

“It
"""

filepath = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), "/home/jakob/writer/datasets/" + datasetName + ".txt"
    )
)
with open(filepath, "r") as fin:
    dataset = fin.read()
    print("got dataset!")

    duplicates = copycheck(min=5, max=6, text=text, dataset=dataset)
    print("duplicates:********************************\n\n")
    for dupe in duplicates:
        print(dupe, "\n")
