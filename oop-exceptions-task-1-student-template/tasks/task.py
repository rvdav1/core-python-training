class Pagination:
    def __init__(self, data, items_on_page):
        if items_on_page <= 0:
            raise ValueError("items_on_page must be a positive integer")
        self.data = data
        self.items_on_page = items_on_page
        self.pages = [data[i:i + items_on_page] for i in range(0, len(data), items_on_page)]

    @property
    def page_count(self):
        return len(self.pages)

    @property
    def item_count(self):
        return len(self.data)

    def count_items_on_page(self, page_number):
        if page_number < 0 or page_number >= self.page_count:
            raise Exception("Invalid index. Page is missing.")
        return len(self.pages[page_number])

    def find_page(self, data):
        results = self.find_all_containing_indices(data)
        if not results:
            raise Exception(f"'{data}' is missing on the pages")
        return results

    def display_page(self, page_number):
        if page_number < 0 or page_number >= self.page_count:
            raise Exception("Invalid index. Page is missing.")
        return self.pages[page_number]
    
    def find_all_containing_indices(self, data):
        concatenated = "".join(self.pages)
        start_indices = []
        start_idx = concatenated.find(data)
        while start_idx != -1:
            start_indices.append(start_idx)
            start_idx = concatenated.find(data, start_idx + 1)

        results = []
        for start_idx in start_indices:
            current_idx = 0
            for i, string in enumerate(self.pages):
                end_idx = current_idx + len(string)
                if start_idx < end_idx and start_idx + len(data) > current_idx:
                    results.append(i)
                current_idx = end_idx
        return results