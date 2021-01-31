# Dupecheck

Use this to prevent ["Thomas Riker" situations](https://memory-alpha.fandom.com/wiki/Thomas_Riker), when generating text with machine learning systems.

At [Eclectic Beams](https://eclecticbeams.com/), when generating stories from finetuned GPT-2 models, I kept finding nice stories, but whole segments of them were just copied verbatim from the dataset text. I started battling this by using my editor's "find" feature on each line of generated text, or random subsequences against the dataset. It was time-consuming, and caused much eye pain and frustration, each time I'd read a story I liked, only to find out it had large sections copied verbatim.

Time to automate the tedious away.

Dupecheck will search for substrings of given length in a larger text dataset for you.
Use this to validate uniqueness before saving generated text, and you'll save yourself a huge headache.

It compares word series without punctuation.

```sh
pip install https://github.com/spacerockzero/dupecheck/archive/v0.5.3.zip
```

```python
import sliding_window from dupecheck

...
# find word series at least 5 words long of your text string in dataset string
duplicates = sliding_window.dupecheck(
              min=5, 
              max=10, 
              text=my_gen_text, 
              dataset=my_dataset,
            )
```
