# imports
from dupecheck.preprocess import pre_process_text
from dupecheck.utils import v_print
from tqdm import trange, tqdm

# config
DEFAULT_MIN = 5
DEFAULT_MAX = 10

# comparison
def compare(text, data):
    text = " ".join(text)
    found = data.find(text)
    if found != -1:
        return text


# sliding window
def token_sliding_window(str, size):
    tokens = str.split(" ")
    for i in range(len(tokens) - size + 1):
        yield tokens[i : i + size]


# runner
def run(window_length, text, dataset, cleaned=False, verbose=False):
    # clean text if haven't cleaned in dupecheck yet
    if cleaned != True:
        v_print(verbose, "Cleaning text in runner: " + str(window_length))
        dataset = pre_process_text(dataset)
        text = pre_process_text(text)
    matches = []
    # sliding window iter
    v_print(verbose, "Building iterators...")
    iters = token_sliding_window(text, window_length)
    v_print(verbose, "Running processors...")
    for txt in tqdm(iters):
        # compare
        match = compare(txt, dataset)
        if match != None:
            # append to matches
            matches.append(match)
    v_print(verbose, "Done processing.")
    if len(matches) > 0:
        # sort them for niceness
        matches = sorted(matches, key=len)
    v_print(verbose, "matches: " + str(matches))
    return {"matches": matches, "count": len(matches)}


# launch jobs for all window sizes in range
def dupecheck(
    min=DEFAULT_MIN,
    max=DEFAULT_MAX,
    text=None,
    dataset=None,
    cleaned=False,
    verbose=False,
):
    # guard
    assert text != None
    assert dataset != None
    # clean text
    v_print(verbose, "Cleaning text...")
    if cleaned == False:
        dataset = pre_process_text(dataset)
        text = pre_process_text(text)
    matches = []  # maybe dict if more complex return data
    # for window_lengths in range
    v_print(verbose, "Starting ranges with runner")
    for win_len in trange(max, min - 1, -1):
        res = run(win_len, text, dataset, True, verbose)
        # if matches, append matches
        if res["count"] > 0:
            matches.append(res)
    return matches
