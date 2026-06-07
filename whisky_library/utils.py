class WhiskyLibrary:
    """
    Manages a collection of whiskies.
    """

    def __init__(self):
        self.whiskies = []

    def add_whisky(self, whisky):
        """
    Add a whisky to the collection.
    """
        self.whiskies.append(whisky)
        

    def remove_whisky(self, name):
        """
    Remove a whisky by name.
    """
        self.whiskies = [
             whisky
             for whisky in self.whiskies
             if whisky.name != name
        ]
        
        
    def search_by_country(self, country):
        """
    Search whiskies by country.
    """
        return [
            whisky
            for whisky in self.whiskies
            if whisky.country.lower()
            == country.lower()
        ]
    
    def average_abv(self):
        """
    Calculate average ABV.
    """
        if not self.whiskies:
            return 0
        return (
            sum(
                whisky.abv
                for whisky in self.whiskies
            )
            / len(self.whiskies)
        )
    
    def total_value(self):
        """
    Calculate total collection value.
    """
        return sum(
            whisky.price
            for whisky in self.whiskies
        )
    
    def most_expensive(self):
        """
    Return the most expensive whisky.
    """
        if not self.whiskies:
            return None
        return max(
            self.whiskies,
            key=lambda whisky: whisky.price
        )