# Dupecheck

Analyze your generated text for plagiarizing your dataset

Use this to prevent ["Thomas Riker" situations](https://memory-alpha.fandom.com/wiki/Thomas_Riker), when generating text with machine learning systems.

At [Eclectic Beams](https://eclecticbeams.com/), when generating stories from finetuned GPT-2 models, I kept finding nice stories, but whole segments of them were just copied verbatim from the dataset text. I started battling this by using my editor's "find" feature on each line of generated text, or random subsequences against the dataset. It was time-consuming, and caused much eye pain and frustration, each time I'd read a story I liked, only to find out it had large sections copied verbatim.

Time to automate the tedious away.

Dupecheck will search for substrings of given length in a larger text dataset for you.
Use this to validate uniqueness before saving generated text, and you'll save yourself a huge headache.

It compares word series without punctuation.

```sh
pip install dupecheck
```

```py
from dupecheck import chunks, sliding_window, sliding_window2
```

## Chunking method
Find word series at least 5 words long in dataset. 
(Prone to mid-pattern window-splitting false negatives, since the window doesn't slide. Your pattern might get cut and split between two chunks, then not found even if it should match)
```py
duplicates = chunks.dupecheck(
              min=5,
              max=10, 
              text=my_gen_text, 
              dataset=my_dataset, 
              verbose=False
            )
```

## Sliding window `find`, try 1
- find word series at least 5 words long of your text string in dataset string
```py
duplicates = sliding_window.dupecheck(
              min=5, 
              max=10, 
              text=my_gen_text, 
              dataset=my_dataset,
            )
```

## Sliding window `find` try 2 
- find word series at least 5 words long of your text string in dataset string.
- cleans text and dataset for you if you don't provide cleaned and specify `cleaned=True`. 
- Cleaning is currently VERY slow.
```py
duplicates = sliding_window2.dupecheck(
              min=5, 
              max=10, 
              text=my_gen_text, 
              dataset=my_dataset,
              cleaned=False,
              verbose=False
            )
```

## Preprocessing helpers
```py
from dupecheck.preprocess import pre_process_text

dataset = pre_process_text(dataset)
text = pre_process_text(text)
```
