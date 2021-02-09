from os import path, makedirs
from dupecheck.sliding_window2 import dupecheck
from dupecheck.preprocess import pre_process_text

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
The sky was growing red in the morning light. The planet was hidden, but how far away it was, and with this little wedge-shaped lake in the center of the southern part of the mountain that seemed like a piece of broken rock lifted by a wind, it was so dark that the stars were not quite visible. The clouds of black smoke huddled in the northwest corner of the plain as far as they could be seen. The clouds and smoke were so thick that they could not be seen above the plain, but their intensity made the plain a unique texture, like a grid of crystal.



Duncan's hand dipped across the fire - the kind of hand that he, in his own country, had held, back in Scotland, but had not thought of, and grasped with more than casual ease. Even here in the wild country of Caves, where fires had so recently been added to the dull gray-green rock of the rock, the sort of hand that he grasped was better than this rough one, better than a man who walked upon quartz lead.



He reached down out of the darkness, that tremor that was so deeply felt. He slid his hand down the edge of the pit and held it there within his hand even as he watched the black smoke swirl at the far horizon.



For the first time in such a short time, he was able to breathe deeply. The hot, dehydrated air of the Caves was different beyond what it had ever known before or since. It brought back to him the senses of home, of the land that had known its former life, the memories of the one hundredth day of his birth, the first man who had ever come upon his own planet.



He squatted once more, holding the flint and steel that he had found beneath the surface of the lake, and then he slowly worked the flint and steel together. No more cracking of rock came from the pit, he saw. The water was simply too dry. He splashed the fire into the lake and then worked to smooth out the worst of it in the flint and steel until a lumpy mass fell upon the surface and in an instant reeked of carbon dioxide and gas.



He worked another lumpy lumpy mass into the fire with an axillary flame, but the lump was too flimsy and the flame died without seeing any of any trace of warmth or fire. The temperature was simply too dull, and the smoke that fell so thickly was so thick that he could see little or see much, even when a gust of wind or the sudden onset of lightning threw a dancing dust-storm of flint and dust into the air. He worked the flint like a cat stirring fire with a mouse.



He went back to the fire, but now it was burning with a green color, the liquid on the bottom coming up very rapidly, he could see little of the flames, but he could tell by the glistening greenness of the ash that the flames had good source of heat. He did not try to move the flint to charcoal-black, that would not give more flame striking the surface something of the burn of charcoal. He watched the cloud of water cloud up above him, but it was still there and did not even seem to move.



He looked around and saw that some of the other fires were gone, that a cloud of water had settled, obscuring the entire camp. Only this one blazing still held water, although he could see where it spilled out most of the night - there below the water, and the first few trees were black now. But the whole place of camp was still burning, the smoke so thick that he could see no sign of fire. The dead leaves that had fallen from the trees in the forest were blackened now by the cold wind that he had not felt today.



He scrambled up and peeped more intently at the source of the flame from the lake.



No fire.



Not yet, he thought, and began to run toward the lake. For a long time that stood out for him was a puzzling, haunting fear because he had the feeling, and yet - he had not the slightest doubt, for so far as he could recall, the fear had been something that he could not accept.



But that particular fear, he knew, had not been entirely unreasonable. Once it had been convinced, the fear had become a taint that was almost painful, almost irritating. It had not been that he had done little more than brush against the flames of his childhood, then, but that he had not been able to escape from the maelstrom of his unconsciousness and thereby relinquish the blame of deadly guilt for the death he had the illness to face.

"""


def make_dir(dirpath):
    if not path.exists(dirpath):
        makedirs(dirpath)


def write_to_file(write_path, text):
    file = open(write_path, "w")
    file.write(text)


root_path = path.abspath(
    path.join(path.dirname(__file__), "/home/jakob/writer/datasets/")
)

dataset_path = path.join(root_path, datasetName + ".txt")

# cache previously cleaned datasets
cleaned_root_path = path.join(root_path, "cleaned_for_comparison")
make_dir(cleaned_root_path)
cleaned_dataset_path = path.join(cleaned_root_path, datasetName + "_cleaned.txt")

dataset_is_cleaned = False
if path.exists(cleaned_dataset_path):
    print("Dataset is cleaned already. Using cached version for comparison")
    dataset_is_cleaned = True
    dataset_path = cleaned_dataset_path


with open(dataset_path, "r") as fin:
    dataset = fin.read()
    print("got dataset!")
    if dataset_is_cleaned == False:
        print("cleaning dataset...")
        dataset = pre_process_text(dataset)
        print("dataset cleaned, writing to file...")
        write_to_file(cleaned_dataset_path, dataset)
    print("cleaning text...")
    text = pre_process_text(text)

    duplicates = dupecheck(
        min=5, max=6, text=text, dataset=dataset, cleaned=True, verbose=True
    )
    print("duplicates:********************************\n\n")
    print(duplicates)
    # for dupe in duplicates:
    #     print(dupe, "\n")
