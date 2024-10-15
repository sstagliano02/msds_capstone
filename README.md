# Capstone Tracker

## 2024-06-01
-Set up markdown file to track Capstone progress. Would like to improve on soft-technical skills through this Status Report vs using a simple Google Doc <br>
-Set up Github repository for project <br>
-Practiced pushing changes from local file to GitHub, using VSCode <br>
-I struggled with the initial set up and cloning, but eventually succeeded in being able to update this markdown file and push directly to the GitHub page <br>
-**Goal for next sprint**: Assemble Mission Statement and Requirements Slides <br>


## 2024-06-07
-**Mission Statement:  Sharpen big data and machine learning skills by ingesting earnings call transcripts and creating an "uncertainty" dictionary via neural networks, using Paul Soto's previous work as a guideline.** <br>
-Ultimately I want to recreate the first half of Paul Soto's work, which uses the Skip Gram Word Embedding technique to find words in close "proximity" to the seed word "Uncertainty". This forms the basis of the dictionary from which to score transcript uncertainty. <br>
-Given time I would also like to see how transcript uncertainty scores impact future loan/deposit movements.<br>

## 2024-06-11
-Refamiliarized myself with the source paper: Soto, Paul. Breaking the Word Bank: Measurement and Effects of Bank Level Uncertainty. Journal of Financial Services Research, 59:1–45, 2020. (December 1, 2019). (https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3347329)<br>
-Focused on understanding how the Word Embedding was done to ensure machine learning algorithms are reproducible. <br>
-[Requirements Slides](https://docs.google.com/presentation/d/1kJGZvuGkIB1E4net2ipg81y3v-zn55AepvC93jrRlPs/edit#slide=id.p) <br>
-**Goal for next sprint**: Kick off process of getting transcript dataset from S&P Global downloaded to personal laptop and practice basic SQL queries to pull data.


## 2024-06-16
-Reviewed Neural Network fundamentals <br>
-Using this video as a guide for hand-coded neural net [https://www.youtube.com/watch?v=w8yWXqWQYmU&ab_channel=SamsonZhang], as well as ML135 Videos.<br>
-Hand calcs for Neural Net [https://towardsdatascience.com/training-a-neural-network-by-hand-1bcac4d82a6e]<br>
-I am losing track of the gradient descent process--need to spend more time reviewing.<br>
-**Goal for next sprint**: Understand each part of the neural network, get Snowflake account set up from S&P and discuss credit limitations. Learn Tensorflow and PyTorch.<br>


## 2024-06-25
-Continued Review of NeuralNetworks<br>
-Worked on use Brown corpus to create bigrams using this tutorial [https://www.udemy.com/share/1023z43@h_yYHNiZa4OPC92zqPpgZ9bzuhmxrpILIkft6Q-JXZQT3BWmFr-oPgjdzjEKPAyOQQ==/]<br>
-Struggling a bit with preprocessing, in particular where to split up bigrams by punctuation and eliminate stopwords without getting rid of context<br>
-Got set up with S&P's Transcript data on Snowflake. Took about a week of back and forth with product to get tables full set up.<br>
-Worked on filtering out banks and earnings calls from the total transcript population. Currently the data lives in SQL tables, with a single transcript having multiple component rows (every time the speaker changes creates a new row).<br>
-**Goal for next sprint**: Concantenate the transcript compenents and export as a csv with each record being a different transcript, and separate by date. I also want finish the bigram tutorial and move on to skip grams with the brown corpus.<br>

## 2024-07-09
-Was out of country for a week so progress slowed since last update.<br>
-Struggling with understanding the data format that needs to be created to feed skip grams to neural net. My understanding right now is that I need a matric of each word pair in a window that shows probability of appearance of that word pair (a window of 5 means 5 words before and after a target word).<br>
-Also struggling to understand what is meant by "features" of the hidden layer and how that relates to real life features in the data.<br>
-**Goal for next sprint**: Use Word2Vec library to run basic skip gram model on Brown corpus sample.<br>

## 2024-07-15
-Worked through Word2Vec library with Chris McCormick's ebook and documentation<br>
-ebook: [https://mccormickml.com/2016/04/19/word2vec-tutorial-the-skip-gram-model/] docs: [https://radimrehurek.com/gensim/auto_examples/tutorials/run_word2vec.html]<br>
-Struggled with processing and remove punctuation, but was able to work through a basic example. Will need to dive deeper and experiment with different process techniques.<br>
-Initial uncertainty results OK, but not great. Some intutively make sense but not all.<br>
-**Goal for next sprint**: Outline design document. <br>

## 2024-07-15
-**Demo**: [https://share.vidyard.com/watch/YHs5cqYbNGKTgddrYkjjRY?]<br>
-Code: [https://github.com/sstagliano02/msds_capstone/blob/main/gensim_brown.ipynb]<br>


## 2024-08-6
-Spent last few weeks working on design document--submitted via canvas.<br>
-Majority of time spent researching the best preprocessing techniques to use--negation handling looks like it will lead to the best results but be difficult.<br>
-Read through several Mikolov papers to full understand word2vec. <br>

## 2024-09-07
-Negation handling: [https://towardsdatascience.com/increasing-accuracy-of-sentiment-classification-using-negation-handling-9ed6dca91f53] <br>
-Custom Implementation : [https://www.geeksforgeeks.org/implement-your-own-word2vecskip-gram-model-in-python/#what-is-skipgram]
-  :[https://datajenius.com/2022/03/13/a-deep-dive-into-nlp-tokenization-encoding-word-embeddings-sentence-embeddings-word2vec-bert/]
-initial preprocessing took 5 hours on the full data set (punctuation, lowercase, stopwords), 5 minutes on gensim<br>


## 2024-09-12
-New processing took 6 seconds on gensim with the same level of token reduction (1,161,192 to 686,163)<br>
-On live data new processing took 15 min<br>
-Kept words with hyphens<br>

## 2024-09-13
-Think about measuring uncertainty by speaker<br>
-Look at false positives/false<br>
-Look at cnns to deal with longer sentences and topics<br>

## 2024-09-21
-working with S&P to get Loan data in Snowflake environment. Pulling data from Y9C Filings to mimic Soto report and tie data to entity attached to the transcript<br>
-first pass the team added call report data, but the tables don't have the line items I need<br>
-Reading about how to actually calculate the sentiment, and Frank Zhao uses a simple count of uncertain words/total words<br>


## 2024-10-06
-reworked code to build model for all document years grab uncerainty lists for each year (previously looked at all text)<br>
-created class to hold each model and associated corpus, word list, etc.<br>
-created coutner to see which words only appeared in 1 or 2 document years, but final list was much larger than expected (ie words like "outrun" or "evolves" appear in only one year, but have no intuitive macroeconomic meaning). I need to figure out how to futher narrow down the word list to just import topics--considering using a tf idf score with each year being one document<br>


## 2024-10-13
-Focused on loading in loan data. had difficulties getting the right data, but was helped by S&P support.
-Loaded in loan data in one file, and then had to pull CIQ to SNL ID mapping in another file.
-Also pulled in a new file that just had all transcript IDs in one place rather than across multiple years
-Worked on creating a blank dataframe and then iterating over the the transcript data base, grabbing connections/maps from each data set.
-Created an uncertainty score, looking at the count of uncertainty words/over transcript length


