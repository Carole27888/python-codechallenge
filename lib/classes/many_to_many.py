class Article:
    all_articles = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters long")




        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of Author")
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be an instance of Magazine")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string with length between 5 and 50")

        self._author = author
        self._magazine = magazine
        self._title = title

        
        Article.all_articles.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, new_author):
        
            
        self._author = new_author
    
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine")
        self._magazine = new_magazine
    

class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise TypeError("Name must be a string")
        self._name = name
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):
            raise AttributeError("Can't set attribute")
        self._name = value

    
    def articles(self):
        return [article for article in Article.all_articles if article.author == self]

    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
        topics = list(set([article.magazine.category for article in self.articles()]))
        return topics if topics else None


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        self._name = name
        if not isinstance(category, str) or  len(category) == 0:
            raise ValueError("Category must  be a non-empty string")
        self._category = category

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or not (2 <= len(new_name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        self._name = new_name
    
    @property
    def category(self):
        return self._category
    

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str) or len(new_category.strip()) == 0:
            raise ValueError("Category cannot be an empty string.")
        self._category = new_category

        

    def articles(self):
        return [article for article in Article.all_articles if article.magazine == self]

    def contributors(self):
        return list (set([article.author for article in self.articles()]))

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if len(titles) > 0 else None

    def contributing_authors(self):
        author_counts = {}
        for article in self.articles():
            if article.author in author_counts:
               author_counts[article.author] += 1
            else:
                author_counts[article.author] = 1

        result = [author for author, count in author_counts.items() if count > 2]

        if len(result) == 0: 
           return None
        return result



