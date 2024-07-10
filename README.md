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