# Boosting Customer Retention: Product Analysis of Eureka Math Educational Curriculum
### Objective
Boost customer retention for [Great Minds](https://greatminds.org/eurekamathsquared#eureka-math-builds-knowledge), an ed-tech company, by fixing issues that lead to churn. By conducting sentiment analysis of product reviews for two of their math curriculum products: "Eureka Math" and "Eureka Math<sup>2</sup>", we can quantify the success of Eureka products and identify areas for improvement.

### Findings
**Great Minds** defines 3 Key Qualities of Eureka products: **Accessible, Coherent, Engaging**. Product reviews were assessed based on these qualities in order to identify gaps between current performance and ideal performance. 

#### Sentiment
#### Main Issues
1. Curriculum Rigor
  * Difficulty is not appropriate for the prescribed grade level
2. Improper Implementation / Insufficient Support
  * Issues transitioning students into content for the next grade level
3. Pedagogical Challenges / Materials & Resources
  * Teaching techniques are too confusing
  * Pacing is too fast
  * Materials are not engaging. Lack of manipulatives.


### Recommendations
### Method
1. **Gather Product Reviews**: In lieu of publicy available customer reviews from **Great Minds**,
we can obtain product reviews using [PRAW](https://praw.readthedocs.io/en/stable/getting_started/quick_start.html)
to scrape the subreddit page **r/Teachers** for posts, comments, and replies from educators.
2. **Perform Sentiment Analysis**: Pre-processing product reviews using [NLTK](https://www.nltk.org/) prepares them for the [sentiment intensity analyzer](https://github.com/cjhutto/vaderSentiment) within NLTK to measure customer sentiment.
3. **Visualize Performance**: Visualizing the distribution of sentiment scores using [Matplotlib](https://matplotlib.org/) allows the Product team to get an intuitive sense of customer sentiment.
4. **Identify Improvement Areas**: Isolating negative reviews allows us to identify gaps in product performance to retain existing customers and prevent churn. 
### Limits
1. User Error vs. Product Deficiency
2. Demographic Information of Authors Unknown: reviews do not always explicitly indicate their geographic location, school district, or local context which may affect the implementation of Eureka curricula.
3. Uninformative comments: some reviews reflect the educator's sentiment about the product, which are useful. However, some do not identify features they find unsatisfactory.
### Next Steps
1. Train and test model on reviews not explicitly mentioning "Eureka".
2. Identify potential areas of improvement within "Positive" reviews.
