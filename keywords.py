text='''
Telangana Growth Analysis
Objective:
• Explore Stamp Registration, Transportation and Ts-Ipass Datasets.
Understand their attributes, categories and time period.
• Analyze trends and patterns within each department.
• Identify growth opportunities and areas needing attention.
• Find correlation among these departments and report the overall growth of the
state through insights and relevant visuals such as shape maps.
Primary Questions:
Stamp Registration
1. How does the revenue generated from document registration vary
across districts in Telangana? List down the top 5 districts that showed
the highest document registration revenue growth between FY 2019
and 2022.
2. How does the revenue generated from document registration compare
to the revenue generated from e-stamp challans across districts? List
down the top 5 districts where e-stamps revenue contributes
significantly more to the revenue than the documents in FY 2022?
3. Is there any alteration of e-Stamp challan count and document
registration count pattern since the implementation of e-Stamp
challan? If so, what suggestions would you propose to the
government?
4. Categorize districts into three segments based on their stamp
registration revenue generation during the fiscal year 2021 to 2022.
codebasics.ioTransportation
5. Investigate whether there is any correlation between vehicle sales and
specific months or seasons in different districts. Are there any months
or seasons that consistently show higher or lower sales rate, and if yes,
what could be the driving factors? (Consider Fuel-Type category only)
6. How does the distribution of vehicles vary by vehicle class
(MotorCycle, MotorCar, AutoRickshaw, Agriculture) across different
districts? Are there any districts with a predominant preference for a
specific vehicle class? Consider FY 2022 for analysis.
7. List down the top 3 and bottom 3 districts that have shown the highest
and lowest vehicle sales growth during FY 2022 compared to FY
2021? (Consider and compare categories: Petrol, Diesel and Electric)
Ts-Ipass (Telangana State Industrial Project Approval and Self
Certification System)
8. List down the top 5 sectors that have witnessed the most significant
investments in FY 2022.
9. List down the top 3 districts that have attracted the most significant
sector investments during FY 2019 to 2022? What factors could have
led to the substantial investments in these particular districts?
10. Is there any relationship between district investments, vehicles
sales and stamps revenue within the same district between FY 2021
and 2022?
11. Are there any particular sectors that have shown substantial
investment in multiple districts between FY 2021 and 2022?
12. Can we identify any seasonal patterns or cyclicality in the
investment trends for specific sectors? Do certain sectors
experience higher investments during particular months?
codebasics.ioSecondary Research: (Need additional research and get additional
data)
Note: These are just examples, you can add more questions
1. What are the top 5 districts to buy commercial properties in
Telangana? Justify your answer.
2. What significant policies or initiatives were put into effect to
enhance economic growth, investments, and employment in
Telangana by the current government? Can we quantify the
impact of these policies using available data?
3. Provide top 5 Insights & 5 recommendations to Telangana
government for sustained growth in the next 5 years based on
your analysis.
codebasics.io

'''

# Tokenize the text into words
words = text.split()

# Create a dictionary to store word frequencies
word_frequency = {}

# Define a list of common words to ignore (customize as needed)
common_words_to_ignore = ["the", "of", "is", "a", "it", "for", "and", "to", "in", "this"]

# Calculate word frequencies
for word in words:
    word = word.lower()
    if word not in common_words_to_ignore:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

# Extract keywords based on word frequency
top_n_keywords = 50  # You can adjust this to get more or fewer keywords
keywords = [word for word, freq in sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)[:top_n_keywords]]

# Print the extracted keywords
print("Keywords:", keywords)