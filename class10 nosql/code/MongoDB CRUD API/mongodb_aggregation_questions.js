// MongoDB Aggregation Pipeline Practice Questions
// Restaurant Collection Based Questions

// ====================================================================================
// BASIC AGGREGATION QUESTIONS
// ====================================================================================

// 1. Write an aggregation query to count the total number of restaurants in each borough.

// 2. Write an aggregation query to find the average score of all restaurants.

// 3. Write an aggregation query to group restaurants by cuisine type and count how many restaurants serve each cuisine.

// 4. Write an aggregation query to find the highest scoring restaurant in each borough.

// 5. Write an aggregation query to calculate the total number of grades given across all restaurants.

// ====================================================================================
// INTERMEDIATE AGGREGATION QUESTIONS
// ====================================================================================

// 6. Write an aggregation query to find the top 5 boroughs with the most restaurants, sorted in descending order.

// 7. Write an aggregation query to find restaurants that have an average score greater than 15 across all their grades.

// 8. Write an aggregation query to count how many restaurants have received each grade (A, B, C, etc.).

// 9. Write an aggregation query to find the cuisine types that have more than 100 restaurants in Manhattan.

// 10. Write an aggregation query to find the restaurant with the lowest average score in each cuisine category.

// ====================================================================================
// ADVANCED AGGREGATION QUESTIONS
// ====================================================================================

// 11. Write an aggregation query to find restaurants that have improved their grades over time (latest grade is better than the first grade).

// 12. Write an aggregation query to calculate the percentage distribution of restaurants across different boroughs.

// 13. Write an aggregation query to find cuisine types where the average score is above the overall average score of all restaurants.

// 14. Write an aggregation query to find restaurants that have been graded more than 5 times and have never received a grade worse than 'B'.

// 15. Write an aggregation query to find the most common grade for each cuisine type.

// ====================================================================================
// COMPLEX AGGREGATION QUESTIONS
// ====================================================================================

// 16. Write an aggregation query to find restaurants in each borough that are above the borough's average score.

// 17. Write an aggregation query to create a summary report showing for each borough: total restaurants, average score, most common cuisine, and best restaurant name.

// 18. Write an aggregation query to find restaurants whose name contains 'Pizza' and group them by borough, showing the count and average score for each borough.

// 19. Write an aggregation query to find the seasonal pattern of restaurant inspections by extracting month from grade dates and counting inspections per month.

// 20. Write an aggregation query to find cuisine types that exist in all 5 boroughs (assuming 5 boroughs: Manhattan, Brooklyn, Queens, Bronx, Staten Island).

// ====================================================================================
// GEOSPATIAL AND TEXT AGGREGATION QUESTIONS
// ====================================================================================

// 21. Write an aggregation query to find restaurants within a specific coordinate range (latitude between 40.7 and 40.8, longitude between -74.1 and -73.9).

// 22. Write an aggregation query to group restaurants by the first letter of their name and count how many start with each letter.

// 23. Write an aggregation query to find restaurants with names longer than 20 characters and group them by borough.

// 24. Write an aggregation query to find the average coordinates (latitude and longitude) of restaurants in each borough.

// 25. Write an aggregation query to find restaurants that have 'Street' in their address and group by cuisine type.

// ====================================================================================
// TIME-BASED AGGREGATION QUESTIONS
// ====================================================================================

// 26. Write an aggregation query to find the year with the most restaurant inspections.

// 27. Write an aggregation query to find restaurants that were inspected in 2014 and received only 'A' grades.

// 28. Write an aggregation query to calculate the average time between inspections for each restaurant.

// 29. Write an aggregation query to find restaurants that haven't been inspected in the last 2 years (from 2015).

// 30. Write an aggregation query to group inspections by quarter and year, showing the count of inspections per quarter.

// ====================================================================================
// STATISTICAL AGGREGATION QUESTIONS
// ====================================================================================

// 31. Write an aggregation query to find the standard deviation of scores for each cuisine type.

// 32. Write an aggregation query to create score ranges (0-10, 11-20, 21-30, etc.) and count how many restaurants fall in each range.

// 33. Write an aggregation query to find outlier restaurants (restaurants with scores more than 2 standard deviations from the mean).

// 34. Write an aggregation query to calculate the median score for restaurants in each borough.

// 35. Write an aggregation query to find the correlation between the number of violations (low scores) and cuisine type.

// ====================================================================================
// RANKING AND COMPARISON QUESTIONS
// ====================================================================================

// 36. Write an aggregation query to rank restaurants within each borough based on their average score.

// 37. Write an aggregation query to find the top 3 restaurants in each cuisine category based on average score.

// 38. Write an aggregation query to compare restaurant performance before and after 2013 (average scores).

// 39. Write an aggregation query to find cuisine types where the score variance is highest (most inconsistent quality).

// 40. Write an aggregation query to create a leaderboard of the top 10 restaurants overall based on average score and number of inspections.

// ====================================================================================
// MULTI-COLLECTION AGGREGATION QUESTIONS (Advanced)
// ====================================================================================

// Assuming additional collections exist:

// 41. Write an aggregation query to join restaurant data with a hypothetical 'owners' collection to find owners with multiple restaurants.

// 42. Write an aggregation query to join restaurant data with a 'neighborhoods' collection to get neighborhood demographics for each restaurant.

// 43. Write an aggregation query to join restaurant data with a 'violations' collection to get detailed violation information.

// 44. Write an aggregation query to create a comprehensive report joining restaurants with reviews from a 'reviews' collection.

// 45. Write an aggregation query to find restaurants that appear in both a 'featured_restaurants' collection and have high scores.

// ====================================================================================
// BUSINESS INTELLIGENCE QUESTIONS
// ====================================================================================

// 46. Write an aggregation query to identify market gaps: find borough-cuisine combinations that have fewer than 5 restaurants.

// 47. Write an aggregation query to analyze restaurant density: find the number of restaurants per square mile for each borough (assuming area data).

// 48. Write an aggregation query to predict restaurant success: find common characteristics of restaurants with consistently high scores.

// 49. Write an aggregation query to identify inspection trends: are restaurants getting better or worse scores over time?

// 50. Write an aggregation query to create a risk assessment: identify restaurants likely to fail their next inspection based on historical patterns.

// ====================================================================================
// NOTES FOR PRACTICE:
// ====================================================================================

/*
Collection Structure Reminder:
{
  "_id": ObjectId,
  "restaurant_id": "string",
  "name": "string", 
  "borough": "string",
  "cuisine": "string",
  "address": {
    "street": "string",
    "zipcode": "string",
    "building": "string", 
    "coord": [longitude, latitude]
  },
  "grades": [
    {
      "date": ISODate,
      "grade": "string", 
      "score": number
    }
  ]
}

Common Aggregation Operators to Practice:
- $match: Filter documents
- $group: Group documents and perform calculations
- $sort: Sort documents
- $project: Include/exclude/transform fields
- $unwind: Deconstruct arrays
- $lookup: Join collections
- $addFields: Add computed fields
- $limit/$skip: Pagination
- $sample: Random sampling
- $bucket: Create buckets for analysis
- $facet: Multi-faceted aggregation
- $graphLookup: Recursive lookup
- $geoNear: Geospatial queries

Aggregation Accumulators:
- $sum, $avg, $min, $max, $count
- $push, $addToSet
- $first, $last
- $stdDevPop, $stdDevSamp

Date Operators:
- $year, $month, $dayOfMonth
- $dayOfWeek, $dayOfYear
- $dateToString, $dateDiff

String Operators:  
- $concat, $substr
- $toUpper, $toLower
- $strLenCP, $indexOfCP

Math Operators:
- $add, $subtract, $multiply, $divide
- $mod, $abs, $ceil, $floor
- $sqrt, $pow

Conditional Operators:
- $cond, $ifNull
- $switch, $case
*/
