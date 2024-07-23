import nltk
from gensim.summarization import summarize

# Ensure you have the required nltk packages
nltk.download('punkt')

def summarize_text(file_path, summary_ratio=0.2):
    """
    Summarize the text from a file.

    :param file_path: Path to the text file.
    :param summary_ratio: Ratio of sentences to keep in the summary.
    :return: Summarized text.
    """
    with open(file_path, 'r') as file:
        text = file.read()
    
    summary = summarize(text, ratio=summary_ratio)
    return summary

# Example usage
file_path = 'path_to_your_text_file.txt'
summary = summarize_text(file_path, summary_ratio=0.2)
print(summary)
