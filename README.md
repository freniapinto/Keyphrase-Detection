(Folder: Results)
File : train.combined.stem.txt is the author+reader assignned keyphrases
Folder: TFIDF
	File: Precision.txt
	File: Recall.txt
	File: Keyphrases.txt
Folder: TopicRank
	File: Precision.txt
	File: Recall.txt
	File: Keyphrases.txt

The Precision.txt, Recall.txt and Keyphrases.txt stores the precision, recall and keyphrases assigned for each of the document in the document for each approach as the folder name.

(Folder: Code)
HOW TO RUN THE PROGRAM 
- All the files are written in Python(Version 2.7). No external libraries have been used.
- The command to run each of the files is written at the end of file. Update the location of the corpus.
- Using CMD, these files can be executed using the command python filename.py
- TFIDF.py implements the TFIDF approach. Graph.py implements the TopicRank.
