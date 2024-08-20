# Boosting Customer Retention: Product Analysis of Eureka Math Educational Curriculum
### Objective
Boost customer retention for [Great Minds](https://greatminds.org/eurekamathsquared#eureka-math-builds-knowledge), an ed-tech company, by fixing issues that lead to churn. By conducting sentiment analysis of product reviews for two of their math curriculum products: "Eureka Math" and "Eureka Math<sup>2</sup>", we can quantify the success of Eureka products and identify areas for improvement. 

**Great Minds** defines 3 Key Qualities of Eureka products: **Accessible, Coherent, Engaging**. Product reviews were assessed based on these qualities in order to identify gaps between current performance and ideal performance. 

### Sentiment Analysis of Reviews 
Each review has a `Positive`, `Neutral`, `Negative`, and `Compound` score. 
- The `Compound` score is a measure of overall sentiment expressed by a review which provides a high-level view of how users feel about a product. See [VADERsentiment](https://github.com/cjhutto/vaderSentiment) for more information about scoring.

- The `Positive`, `Neutral`, and `Negative` scores represent the ratios of positive, neutral, and negative sentiment within a review. This provides more nuance since most reviews are a mixture of sentiments.

### Findings
Based on `Compound` scores, reviews from educators and parents generally indicate that positive sentiments outweigh negative sentiments. 

| | All Reviews | Reviews explicitly mentioning "Eureka" | 
| ----- | ----- | ----- |
| Total | 1490 | 140 |  
| Positive Compound Score | 876 (58.8%) | 104 (74.3%) |
| Neutral Compound Score | 344 (23.1%) | 27 (6.4%) |
| Negative Compound Score | 270 (18.1%) | 9 (19.3%) |
 
<img src="https://github.com/vitoperez117/Product_Analysis_for_Eureka_Math_Curriculum/blob/main/Assets/General/Total%20Sentiment%20Reviews%20(Pie).png" alt="Sentiment Breakdown (All Reviews)" width=375 float=left/> <img src="https://github.com/vitoperez117/Product_Analysis_for_Eureka_Math_Curriculum/blob/main/Assets/'Sentiment%20Review%20of%20All%20Entries%20Explicitly%20Mentioning%20'Eureka'%20(Pie).png" alt="Sentiment Breakdown (All Reviews)" width=375 float=right/> 

**Compound Scores Distribution** 

<img src="https://github.com/vitoperez117/Product_Analysis_for_Eureka_Math_Curriculum/blob/main/Assets/General/All%20COMPOUND%20Score%20Reviews.png" width=300 float=left/> <img src="https://github.com/vitoperez117/Product_Analysis_for_Eureka_Math_Curriculum/blob/main/Assets/COMPOUND%20Entries%20Explicitly%20Mentioning%20'Eureka'.png" width=300 float=right/> 

Both the `Positive` sentiment and `Negative` sentiment scores are weak. In other words, users moderately like the product but have mild to moderate complaints. To better understand potential causes of churn with existing customers, this study closely examines the reviews with a `Negative` Compound Score to identify the main problems with the product. 

**Positive Sentiment**

Although the vast majority of reviews lean `Positive`, the `Positive` scores mostly range from moderate to weak. This could potentially signal future churn if another product better fits their needs. Some Positive reviews based on `Compound` score also mention slightly unsatisfactory features that concur with issues mentioned in Negative reviews. 

<img src="https://github.com/vitoperez117/Product_Analysis_for_Eureka_Math_Curriculum/blob/main/Assets/General/All%20POS%20Score%20Reviews.png" width=300 float=left/> <img src="https://github.com/vitoperez117/Product_Analysis_for_Eureka_Math_Curriculum/blob/main/Assets/POS%20Entries%20Explicitly%20Mentioning%20'Eureka'.png" width=300 float=right/>

**Neutral Sentiment** 

Reviews showing strong Neutral scores possibly indicate lack of certainty with the product which could eventually lead to churn.

<img src="https://github.com/vitoperez117/Product_Analysis_for_Eureka_Math_Curriculum/blob/main/Assets/General/All%20NEU%20Score%20Reviews.png" width=300 float=left/> <img src="https://github.com/vitoperez117/Product_Analysis_for_Eureka_Math_Curriculum/blob/main/Assets/NEU%20Entries%20Explicitly%20Mentioning%20'Eureka'.png" width=300 float=right/> 

**Negative Sentiment**

The majority of `Negative` sentiments found across reviews are weak. Reviews with weak `Negative` sentiment identify unsatisfactory product issues but rarely reject the product as a whole. As a result, these users might be retained if the company gathers further feedback and resolve overarching issues. Main issues from Negative reviews that explicitly about "Eureka" have been extracted below.

<img src="https://github.com/vitoperez117/Product_Analysis_for_Eureka_Math_Curriculum/blob/main/Assets/General/All%20NEG%20Score%20Reviews.png" width=300 float=left/> <img src="https://github.com/vitoperez117/Product_Analysis_for_Eureka_Math_Curriculum/blob/main/Assets/NEG%20Entries%20Explicitly%20Mentioning%20'Eureka'.png" width=300 float=right/> 


#### Main Issues
1. Curriculum Rigor
   1. Difficulty is not appropriate for the prescribed grade level
2. Improper Implementation / Insufficient Support
Issues transitioning students into content for the next grade level
3. Pedagogical Challenges / Materials & Resources
  * Teaching techniques are too confusing
  * Pacing is too fast
  * Materials are not engaging. Lack of manipulatives.


### Recommendations
### Method
1. **Gather Product Reviews**: In lieu of publicy available customer reviews from **Great Minds**,
we can obtain product reviews using [PRAW](https://praw.readthedocs.io/en/stable/getting_started/quick_start.html)
to scrape the subreddit page **r/Teachers** for posts, comments, and replies from educators relating to "Eureka".
2. **Perform Sentiment Analysis**: Pre-processing product reviews using [NLTK](https://www.nltk.org/) prepares them for the [sentiment intensity analyzer](https://github.com/cjhutto/vaderSentiment) within NLTK to measure customer sentiment.
3. **Visualize Performance**: Visualizing the distribution of sentiment scores using [Matplotlib](https://matplotlib.org/) allows the Product team to get an intuitive sense of customer sentiment.
4. **Identify Improvement Areas**: Isolating negative reviews allows us to identify gaps in product performance to retain existing customers and prevent churn.


### Limits
1. Sample Size: 1,490 reviews collected from one forum (r/Teachers). Less than 10% of reviews explicitly mentioned "Eureka"
2. User Error vs. Product Deficiency
3. Demographic Information of Authors Unknown: reviews do not always explicitly indicate their geographic location, school district, or local context which may affect the implementation of Eureka curricula.
4. Uninformative comments: some reviews reflect the educator's sentiment about the product, which are useful. However, some do not identify features they find unsatisfactory.
### Next Steps
1. Train and test model on reviews not explicitly mentioning "Eureka".
2. Identify potential areas of improvement within "Positive" reviews.
