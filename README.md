# 📰 Fake News Detection

This project detects whether a given news article is **fake** or **genuine** using machine learning classifiers trained on a labeled dataset.

## 📂 Dataset Used

- `True.csv` and `Fake.csv` from Kaggle
- `True.csv` contains real news articles
- `Fake.csv` contains fabricated news articles
- Labels: `1` for Genuine, `0` for Fake

> ⚠️ This model only works well on news articles similar to the dataset provided. Performance may vary with external or unrelated data.

---

## 🧠 Models Used

1. **Logistic Regression**
2. **Random Forest Classifier**
3. **Gradient Boosting Classifier**

---

## 🔧 Tools & Libraries

- **Python**
- `pandas` for data manipulation
- `scikit-learn` for model training and evaluation
- `TfidfVectorizer` for converting text to numerical features
- `re` for text cleaning
- `classification_report` for evaluation

---

## 🧽 Text Preprocessing

The following steps were used to clean the text:
- Convert to lowercase
- Remove URLs
- Remove HTML tags
- Remove punctuation
- Remove digits and newline characters

---

## 🧪 Manual Testing

You can enter a news article as input and get predictions from all three models.

### 📥 Example Input

 Enter a news article to test: As U.S. budget fight looms, Republicans flip their fiscal script","WASHINGTON (Reuters) - The head of a conservative Republican faction in the U.S. Congress, who voted this month for a huge expansion of the national debt to pay for tax cuts, called himself a “fiscal conservative” on Sunday and urged budget restraint in 2018. In keeping with a sharp pivot under way among Republicans, U.S. Representative Mark Meadows, speaking on CBS’ “Face the Nation,” drew a hard line on federal spending, which lawmakers are bracing to do battle over in January. When they return from the holidays on Wednesday, lawmakers will begin trying to pass a federal budget in a fight likely to be linked to other issues, such as immigration policy, even as the November congressional election campaigns approach in which Republicans will seek to keep control of Congress. President Donald Trump and his Republicans want a big budget increase in military spending, while Democrats also want proportional increases for non-defense “discretionary” spending on programs that support education, scientific research, infrastructure, public health and environmental protection. “The (Trump) administration has already been willing to say: ‘We’re going to increase non-defense discretionary spending ... by about 7 percent,’” Meadows, chairman of the small but influential House Freedom Caucus, said on the program. “Now, Democrats are saying that’s not enough, we need to give the government a pay raise of 10 to 11 percent. For a fiscal conservative, I don’t see where the rationale is. ... Eventually you run out of other people’s money,” he said. Meadows was among Republicans who voted in late December for their party’s debt-financed tax overhaul, which is expected to balloon the federal budget deficit and add about $1.5 trillion over 10 years to the $20 trillion national debt. “It’s interesting to hear Mark talk about fiscal responsibility,” Democratic U.S. Representative Joseph Crowley said on CBS. Crowley said the Republican tax bill would require the  United States to borrow $1.5 trillion, to be paid off by future generations, to finance tax cuts for corporations and the rich. “This is one of the least ... fiscally responsible bills we’ve ever seen passed in the history of the House of Representatives. I think we’re going to be paying for this for many, many years to come,” Crowley said. Republicans insist the tax package, the biggest U.S. tax overhaul in more than 30 years,  will boost the economy and
 job growth. House Speaker Paul Ryan, who also supported the tax bill, recently went further than Meadows, making clear in a radio interview that welfare or “entitlement reform,” as the party often calls it, would be a top Republican priority in 2018. In Republican parlance, “entitlement” programs mean food stamps, housing assistance, Medicare and Medicaid health insurance for the elderly, poor and disabled, as well as other programs created by Washington to assist the needy. Democrats seized on Ryan’s early December remarks, saying they showed Republicans would try to pay for their tax overhaul by seeking spending cuts for social programs. But the goals of House Republicans may have to take a back seat to the Senate, where the votes of some Democrats will be needed to approve a budget and prevent a government shutdown. Democrats will use their leverage in the Senate, which Republicans narrowly control, to defend both discretionary non-defense programs and social spending, while tackling the issue of the “Dreamers,” people brought illegally to the country as children. Trump in September put a March 2018 expiration date on the Deferred Action for Childhood Arrivals, or DACA, program, which protects the young immigrants from deportation and provides them with work permits. The president has said in recent Twitter messages he wants funding for his proposed Mexican border wall and other immigration law changes in exchange for agreeing to help the Dreamers. Representative Debbie Dingell told CBS she did not favor linking that issue to other policy objectives, such as wall funding. “We need to do DACA clean,” she said.  On Wednesday, Trump aides will meet with congressional leaders to discuss those issues. That will be followed by a weekend of strategy sessions for Trump and Republican leaders on Jan. 6 and 7, the White House said. Trump was also scheduled to meet on Sunday with Florida Republican Governor Rick Scott, who wants more emergency aid. The House has passed an $81 billion aid package after hurricanes in Florida, Texas and Puerto Rico, and wildfires in California. The package far exceeded the $44 billion requested by the Trump administration. The Senate has not yet voted on the aid. ",politicsNews,"December 31, 2017 "

### OUTPUT :
LR Prediction: It is a Genuine News
GBC Prediction: It is a Genuine News
RFC Prediction: It is a Genuine News
### input
📝 Enter a news article to test: Donald Trump Sends Out Embarrassing New Year’s Eve Message
### output :
LR Prediction: It is a Fake News
GBC Prediction: It is a Fake News
RFC Prediction: It is a Fake News


---

Let me know if you want me to add this to your project directory or push it to your GitHub repo directly.

  

