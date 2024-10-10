from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load example document


def split_text(file_path):
    with open(file_path, errors="ignore") as f:
        state_of_the_union = f.read()
    text_splitter = RecursiveCharacterTextSplitter(
        # Set a really small chunk size, just to show.
        chunk_size=128 * 1024,
        chunk_overlap=20,
        length_function=len,
        is_separator_regex=False,
    )
    texts = text_splitter.create_documents([state_of_the_union])
    return texts


if __name__ == "__main__":
    text = split_text(
        "D:\Desktop\Orange stage MFE\orange stage\ServerLog\log-ex\data\Linux.txt"
    )
    print(len(text))
