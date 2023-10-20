
text = """In the realm of mathematics, particularly in the field of algebra, 
	  we encounter a set of fundamental principles and rules that serve as 
          the building blocks for solving equations, simplifying expressions, and understanding 
          the relationships between variables. These principles encompass various concepts such as arithmetic 
          operations, variables, constants, equations, and inequalities. Could you provide a comprehensive explanation 
          of these core principles in algebra, and illustrate how they are applied to solve complex mathematical problems? 
          Furthermore, it would be immensely helpful to explore practical examples that showcase the real-world significance 
          and applications of algebraic concepts"""

import yake
kw_extractor = yake.KeywordExtractor()

language = "en"
max_ngram_size = 1
deduplication_threshold = 0.9
numOfKeywords = 20
custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)
keywords = custom_kw_extractor.extract_keywords(text)

for kw in keywords:
    print(kw)

