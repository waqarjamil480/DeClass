// MongoDB Queries Solution for Restaurants Collection
// These queries are designed to work in the mongo shell

// ====================================================================================
// 1. Write a MongoDB query to display all the documents in the collection restaurants
// ====================================================================================

db.restaurants.find()

// Alternative with pretty formatting:
db.restaurants.find().pretty()

// ====================================================================================
// 2. Write a MongoDB query to display the fields restaurant_id, name, borough and 
//    cuisine for all the documents in the collection restaurant
// ====================================================================================

db.restaurants.find({}, {
    "restaurant_id": 1,
    "name": 1,
    "borough": 1,
    "cuisine": 1
})

// ====================================================================================
// 3. Write a MongoDB query to display the fields restaurant_id, name, borough and 
//    cuisine, but exclude the field _id for all the documents in the collection restaurant
// ====================================================================================

db.restaurants.find({}, {
    "_id": 0,
    "restaurant_id": 1,
    "name": 1,
    "borough": 1,
    "cuisine": 1
})

// ====================================================================================
// 4. Write a MongoDB query to find the restaurants which locate in latitude value 
//    less than -95.754168
// ====================================================================================

db.restaurants.find({
    "address.coord.1": {$lt: -95.754168}
})

// Alternative notation (coord is an array where index 0 = longitude, index 1 = latitude):
db.restaurants.find({
    "address.coord": {$elemMatch: {$lt: -95.754168}}
})

// ====================================================================================
// 5. Write a MongoDB query to find the restaurants that do not prepare any cuisine of 
//    'American' and their grade score more than 70 and latitude less than -65.754168
// ====================================================================================

db.restaurants.find({
    $and: [
        {"cuisine": {$ne: "American"}},
        {"grades.score": {$gt: 70}},
        {"address.coord.1": {$lt: -65.754168}}
    ]
})

// ====================================================================================
// 6. Write a MongoDB query to find the restaurants which do not prepare any cuisine of 
//    'American' and achieved a score more than 70 and located in the longitude less than 
//    -65.754168. Note: Do this query without using $and operator
// ====================================================================================

db.restaurants.find({
    "cuisine": {$ne: "American"},
    "grades.score": {$gt: 70},
    "address.coord.0": {$lt: -65.754168}
})

// ====================================================================================
// 7. Write a MongoDB query to find the restaurants which do not prepare any cuisine of 
//    'American' and achieved a grade point 'A' not belongs to the borough Brooklyn. 
//    The document must be displayed according to the cuisine in descending order
// ====================================================================================

db.restaurants.find({
    "cuisine": {$ne: "American"},
    "grades.grade": "A",
    "borough": {$ne: "Brooklyn"}
}).sort({"cuisine": -1})

// ====================================================================================
// 8. Write a MongoDB query to find the restaurant Id, name, borough and cuisine for 
//    those restaurants which contain 'Wil' as first three letters for its name
// ====================================================================================

db.restaurants.find(
    {"name": /^Wil/},
    {
        "_id": 0,
        "restaurant_id": 1,
        "name": 1,
        "borough": 1,
        "cuisine": 1
    }
)

// Alternative using $regex:
db.restaurants.find(
    {"name": {$regex: "^Wil"}},
    {
        "_id": 0,
        "restaurant_id": 1,
        "name": 1,
        "borough": 1,
        "cuisine": 1
    }
)

// ====================================================================================
// 9. Write a MongoDB query to find the restaurant Id, name, borough and cuisine for 
//    those restaurants which contain 'ces' as last three letters for its name
// ====================================================================================

db.restaurants.find(
    {"name": /ces$/},
    {
        "_id": 0,
        "restaurant_id": 1,
        "name": 1,
        "borough": 1,
        "cuisine": 1
    }
)

// Alternative using $regex:
db.restaurants.find(
    {"name": {$regex: "ces$"}},
    {
        "_id": 0,
        "restaurant_id": 1,
        "name": 1,
        "borough": 1,
        "cuisine": 1
    }
)

// ====================================================================================
// 10. Write a MongoDB query to find the restaurant Id, name, borough and cuisine for 
//     those restaurants which contain 'Reg' as three letters somewhere in its name
// ====================================================================================

db.restaurants.find(
    {"name": /Reg/},
    {
        "_id": 0,
        "restaurant_id": 1,
        "name": 1,
        "borough": 1,
        "cuisine": 1
    }
)

// Alternative using $regex:
db.restaurants.find(
    {"name": {$regex: "Reg"}},
    {
        "_id": 0,
        "restaurant_id": 1,
        "name": 1,
        "borough": 1,
        "cuisine": 1
    }
)

// ====================================================================================
// MONGODB AGGREGATION PRACTICE QUESTIONS
// ====================================================================================

/*
The following are practice questions for MongoDB Aggregation Pipeline.
Solutions can be found in the mongodb_aggregation_solutions.js file.

BASIC AGGREGATION QUESTIONS (1-5):
1. Count the total number of restaurants in each borough
2. Find the average score of all restaurants  
3. Group restaurants by cuisine type and count how many serve each cuisine
4. Find the highest scoring restaurant in each borough
5. Calculate the total number of grades given across all restaurants

INTERMEDIATE AGGREGATION QUESTIONS (6-10):
6. Find the top 5 boroughs with the most restaurants
7. Find restaurants with average score greater than 15
8. Count how many restaurants received each grade (A, B, C, etc.)
9. Find cuisine types with more than 100 restaurants in Manhattan
10. Find the restaurant with lowest average score in each cuisine

ADVANCED AGGREGATION QUESTIONS (11-15):
11. Find restaurants that improved their grades over time
12. Calculate percentage distribution of restaurants across boroughs
13. Find cuisine types with above-average scores
14. Find restaurants graded 5+ times with never worse than 'B'
15. Find the most common grade for each cuisine type

COMPLEX AGGREGATION QUESTIONS (16-20):
16. Find restaurants above their borough's average score
17. Create borough summary report (count, avg score, top cuisine, best restaurant)
18. Find 'Pizza' restaurants grouped by borough with stats
19. Find seasonal inspection patterns by month
20. Find cuisine types that exist in all 5 boroughs

GEOSPATIAL & TEXT QUESTIONS (21-25):
21. Find restaurants within specific coordinate ranges
22. Group restaurants by first letter of name
23. Find restaurants with names longer than 20 characters
24. Calculate average coordinates by borough
25. Find restaurants with 'Street' in address by cuisine

TIME-BASED QUESTIONS (26-30):
26. Find the year with most restaurant inspections
27. Find restaurants inspected in 2014 with only 'A' grades
28. Calculate average time between inspections
29. Find restaurants not inspected in last 2 years
30. Group inspections by quarter and year

STATISTICAL QUESTIONS (31-35):
31. Calculate standard deviation of scores by cuisine
32. Create score ranges and count restaurants in each
33. Find outlier restaurants (scores > 2 std deviations from mean)
34. Calculate median score by borough
35. Analyze correlation between violations and cuisine

RANKING & COMPARISON (36-40):
36. Rank restaurants within each borough by average score
37. Find top 3 restaurants in each cuisine category  
38. Compare restaurant performance before/after 2013
39. Find cuisine types with highest score variance
40. Create top 10 overall restaurant leaderboard

MULTI-COLLECTION QUESTIONS (41-45):
41-45. Various $lookup operations with hypothetical collections

BUSINESS INTELLIGENCE (46-50):
46. Identify market gaps (borough-cuisine with <5 restaurants)
47. Analyze restaurant density per square mile
48. Find characteristics of consistently high-scoring restaurants
49. Identify inspection trends over time
50. Create risk assessment for next inspection failures
*/

// ====================================================================================
// ADDITIONAL NOTES:
// ====================================================================================

/*
Structure assumptions for restaurants collection:
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
    "coord": [longitude, latitude]  // Array where index 0 = longitude, index 1 = latitude
  },
  "grades": [
    {
      "date": ISODate,
      "grade": "string",
      "score": number
    }
  ]
}

To run these queries in mongo shell:
1. Connect to MongoDB: mongo
2. Use your database: use your_database_name
3. Execute any of the above queries

For queries involving coordinates:
- address.coord.0 refers to longitude
- address.coord.1 refers to latitude

For regex patterns:
- ^ means start of string
- $ means end of string
- No anchors means anywhere in the string
*/
