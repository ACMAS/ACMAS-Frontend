# Content Search Engine Documentation
The content search engine is composed of two different implementations for the two search features,“Search By Question" and "Search By Course”.

## "Search By Course”
-  Based on filtering for university, department and course
-  Found by querying the PostgreSQL tables associated with each feature
-  Helps the user narrow down the location of course material
## "Search By Question”
-  Implemented a full-text search engine built on open source search platform Elasticsearch with Kibana for analytics

-  More Information about Elasticsearch can be found here: [Elasticsearch](https://www.elastic.co/)

-  More Information about Kibana can be found here: [Kibana](https://www.elastic.co/kibana/)

-  Makes use of fuzzy searching to handle typos, n-grams for query expansion, and an inverted index for fast results

-  The text for each query is preprocessed by performing

-  Lowercasing
  -  Ascii-folding - converting non ascii characters to ascii equivalents
  -  Removing stop words - low info words like \[but, and, is, I, ...\]

-  Each question is indexed using n-gram tokenizer ranging from length 2 to 9

-  The results for each query are ranked and sorted by a scoring function based on tf-idf (term frequency and inverse document frequency)

-  The Elasticsearch server can be accessed at [http://localhost:5601](http://localhost:5601)

-  The Kibana analytics server can be accessed at [http://localhost:9200](http://localhost:9200)

-  Both rely on Docker containers built for each application
