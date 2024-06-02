
class Article:
    all = [] 
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self) 
    
    
    def get_author(self):
        return self._author

    
    def set_author(self, author):
        if not isinstance(author, Author):
            raise ValueError("Author must be of type Author")
        self._author = author
    author=property(get_author,set_author)
    
    def get_magazine(self):
        return self._magazine

    
    def  set_magazine(self, magazine):
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be of type Magazine")
        self._magazine = magazine 

    magazine=property(get_magazine,set_magazine)
    def get_title(self):
        return self._title
    
    def set_title(self, title):
        if hasattr(self, '_title'):
            print("Cannot change the title after the article is instantiated.")
        elif isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title
        else:
            print("Title must be a string between 5 and 50 characters, inclusive.")

    title = property(get_title, set_title)   
        
class Author:
    def __init__(self,name='Unknown' ):
        self.name = name
        self._articles = []
        self._magazines = set()

    def get_name(self):
        return self._name
     
    def set_name(self, name):
        if hasattr(self, '_name'):
            print("Cannot change the name after the author is instantiated.")
        elif isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            print("Name must be a non-empty string.")

    name = property(get_name, set_name)
   
 

    def articles(self):
    
     return [article for article in Article.all if article.author == self]

     pass

    
    def magazines(self):
     return list({article.magazine for article in self.articles()})

     pass

    def add_article(self, magazine, title):
     return Article(self, magazine, title)

     
     pass

    def topic_areas(self):
         if not self.articles():
            return None
         categories = set()
         for article in self.articles():
            categories.add(article.magazine.category)
         return list(categories)

         pass

class Magazine:
    _all_magazines = []
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []
        Magazine._all_magazines.append(self)

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            print("Name must be a string between 2 and 16 characters, inclusive.")

    name = property(get_name, set_name)

    def get_category(self):
        return self._category
    
    def set_category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            print("Category must be a non-empty string.")
    category = property(get_category ,set_category) 

    def articles(self):
        return [article for article in Article.all if article.magazine == self]
        
        pass

    def contributors(self):
        return list({article.author for article in self.articles()})
        pass

    def article_titles(self):
        return [article.title for article in self.articles()] if self.articles() else None
    pass
    
    def contributing_authors(self):
        author_counts = {}
        for article in self.articles():
            author = article.author
            if author in author_counts:
                author_counts[author] += 1
            else:
                author_counts[author] = 1
        contributing_authors = [author for author, count in author_counts.items() if count > 2]
        return contributing_authors if contributing_authors else None
    @classmethod
    def top_publisher(cls):
        if not cls._all_magazines:
            return None
        return max(cls._all_magazines, key=lambda magazine: len(magazine.articles), default=None)