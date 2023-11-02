# TODO:: Evolve - This is supposed to be a document in the format Chroma likes it
class ChromaDocument:
    def __init__(self, summary, title):
        self.page_content = summary
        self.metadata = {"title": title}

    # TODO:: There is an implicit type here, ChromaDocument makes some assumptions about the format of data
    @staticmethod
    def extract_fields(data):
        documents = []
        for item in data:
            if "summary" in item and "title" in item:
                summary = item["summary"]
                title = item["title"]
                document = ChromaDocument(summary, title)
                documents.append(document)
        return documents
