from newspaper import Article
from common_util import split

url = "https://www.mayoclinic.org/diseases-conditions/acl-injury/symptoms-causes/syc-20350738"



class Reader:
    def __init__(self, final_url_file, key_word):
        self.final_url_file = final_url_file
        self.key_word = key_word

    def get_name(self, url):
        parts = split(url)
        name = parts.path.split('/')[2] or 'XXXXXXX'
        return f"{name}.txt"


    def start_url_crawler(self):
        count = 0
        for url in self.final_url_file:
            if self.key_word not in url:
                continue
            article = Article(url)
            article.download()
            article.parse()
            file_name = self.get_name(url)
            with open(file_name, "w+", encoding='utf-8') as fp:
                fp.write(article.text)

            count += 1
            if count > 10:
                break
            
            




if __name__ == "__main__":
    fp = open("final_urls.txt", "r+", encoding='utf-8')
    key_word = "symptoms-causes"
    reader = Reader(fp, key_word)
    reader.start_url_crawler()
