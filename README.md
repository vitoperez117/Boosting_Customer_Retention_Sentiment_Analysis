# Product Analysis of Eureka Math Educational Curriculum
To boost customer retention for Ed-Tech company [Great Minds](https://greatminds.org/eurekamathsquared#eureka-math-builds-knowledge), we analyze product reviews for two of their math curriculum products: "Eureka Math" and "Eureka Math<sup>2</sup>".
By conducting sentiment analysis of product reviews from educators, we can identify the success of Eureka products and areas for improvement.

### Findings
Success Metrics: **Great Minds** defines 3 Key Qualities for Eureka products: Accessible, Coherent, Engaging. These qualities will be the success metrics against which product reviews are measured to identify gaps between current performance and ideal performance. 

Sentiment:
### Recommendations
### Method
1. **Gather Product Reviews**: In lieu of publicy available customer reviews from **Great Minds**,
we can obtain product reviews using [PRAW](https://praw.readthedocs.io/en/stable/getting_started/quick_start.html)
to scrape the subreddit page **r/Teachers** for posts, comments, and replies.

2. **Perform Sentiment Analysis**: Once gathered, product reviews are pre-processed using [NLTK](https://www.nltk.org/) then analyzed for customer sentiment using the [sentiment intensity analyzer](https://github.com/cjhutto/vaderSentiment) within NLTK.
3. **Visualize Performance**: The distribution of sentiment scores are visualized using [Matplotlib](https://matplotlib.org/) to get an intuitive sense of customer sentiment.
4. **Identify Improvement Areas**: Isolating negative reviews allows us to identify gaps in product performance to retain existing customers and prevent churn. 
### Limits
