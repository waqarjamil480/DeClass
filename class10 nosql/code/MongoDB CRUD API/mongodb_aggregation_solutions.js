// MongoDB Aggregation Pipeline Solutions
// Solutions for Restaurant Collection Practice Questions

// ====================================================================================
// BASIC AGGREGATION SOLUTIONS
// ====================================================================================

// 1. Count the total number of restaurants in each borough
db.restaurants.aggregate([
    {
        $group: {
            _id: "$borough",
            count: {$sum: 1}
        }
    },
    {$sort: {count: -1}}
])

// 2. Find the average score of all restaurants
db.restaurants.aggregate([
    {$unwind: "$grades"},
    {
        $group: {
            _id: null,
            averageScore: {$avg: "$grades.score"}
        }
    }
])

// 3. Group restaurants by cuisine type and count
db.restaurants.aggregate([
    {
        $group: {
            _id: "$cuisine",
            count: {$sum: 1}
        }
    },
    {$sort: {count: -1}}
])

// 4. Find the highest scoring restaurant in each borough
db.restaurants.aggregate([
    {$unwind: "$grades"},
    {
        $group: {
            _id: {
                borough: "$borough",
                restaurant_id: "$restaurant_id",
                name: "$name"
            },
            avgScore: {$avg: "$grades.score"}
        }
    },
    {$sort: {"_id.borough": 1, avgScore: -1}},
    {
        $group: {
            _id: "$_id.borough",
            topRestaurant: {$first: "$_id.name"},
            topScore: {$first: "$avgScore"}
        }
    }
])

// 5. Count total number of grades given across all restaurants
db.restaurants.aggregate([
    {$unwind: "$grades"},
    {
        $group: {
            _id: null,
            totalGrades: {$sum: 1}
        }
    }
])

// ====================================================================================
// INTERMEDIATE AGGREGATION SOLUTIONS
// ====================================================================================

// 6. Top 5 boroughs with the most restaurants
db.restaurants.aggregate([
    {
        $group: {
            _id: "$borough",
            count: {$sum: 1}
        }
    },
    {$sort: {count: -1}},
    {$limit: 5}
])

// 7. Restaurants with average score greater than 15
db.restaurants.aggregate([
    {$unwind: "$grades"},
    {
        $group: {
            _id: "$restaurant_id",
            name: {$first: "$name"},
            avgScore: {$avg: "$grades.score"}
        }
    },
    {$match: {avgScore: {$gt: 15}}}
])

// 8. Count how many restaurants received each grade
db.restaurants.aggregate([
    {$unwind: "$grades"},
    {
        $group: {
            _id: "$grades.grade",
            count: {$sum: 1}
        }
    },
    {$sort: {"_id": 1}}
])

// 9. Cuisine types with more than 100 restaurants in Manhattan
db.restaurants.aggregate([
    {$match: {borough: "Manhattan"}},
    {
        $group: {
            _id: "$cuisine",
            count: {$sum: 1}
        }
    },
    {$match: {count: {$gt: 100}}},
    {$sort: {count: -1}}
])

// 10. Restaurant with lowest average score in each cuisine category
db.restaurants.aggregate([
    {$unwind: "$grades"},
    {
        $group: {
            _id: {
                cuisine: "$cuisine",
                restaurant_id: "$restaurant_id",
                name: "$name"
            },
            avgScore: {$avg: "$grades.score"}
        }
    },
    {$sort: {"_id.cuisine": 1, avgScore: 1}},
    {
        $group: {
            _id: "$_id.cuisine",
            worstRestaurant: {$first: "$_id.name"},
            lowestScore: {$first: "$avgScore"}
        }
    }
])

// ====================================================================================
// ADVANCED AGGREGATION SOLUTIONS
// ====================================================================================

// 11. Restaurants that improved their grades over time
db.restaurants.aggregate([
    {$unwind: "$grades"},
    {$sort: {"restaurant_id": 1, "grades.date": 1}},
    {
        $group: {
            _id: "$restaurant_id",
            name: {$first: "$name"},
            firstGrade: {$first: "$grades.grade"},
            lastGrade: {$last: "$grades.grade"},
            grades: {$push: "$grades"}
        }
    },
    {
        $addFields: {
            gradeValues: {
                $map: {
                    input: ["$firstGrade", "$lastGrade"],
                    as: "grade",
                    in: {
                        $switch: {
                            branches: [
                                {case: {$eq: ["$$grade", "A"]}, then: 4},
                                {case: {$eq: ["$$grade", "B"]}, then: 3},
                                {case: {$eq: ["$$grade", "C"]}, then: 2}
                            ],
                            default: 1
                        }
                    }
                }
            }
        }
    },
    {
        $match: {
            $expr: {
                $gt: [
                    {$arrayElemAt: ["$gradeValues", 1]},
                    {$arrayElemAt: ["$gradeValues", 0]}
                ]
            }
        }
    },
    {
        $project: {
            name: 1,
            firstGrade: 1,
            lastGrade: 1,
            improved: true
        }
    }
])

// 12. Percentage distribution of restaurants across boroughs
db.restaurants.aggregate([
    {
        $group: {
            _id: "$borough",
            count: {$sum: 1}
        }
    },
    {
        $group: {
            _id: null,
            boroughs: {$push: {borough: "$_id", count: "$count"}},
            total: {$sum: "$count"}
        }
    },
    {$unwind: "$boroughs"},
    {
        $project: {
            _id: 0,
            borough: "$boroughs.borough",
            count: "$boroughs.count",
            percentage: {
                $multiply: [
                    {$divide: ["$boroughs.count", "$total"]},
                    100
                ]
            }
        }
    },
    {$sort: {percentage: -1}}
])

// 13. Cuisine types with above-average scores
db.restaurants.aggregate([
    // First, calculate overall average
    {$unwind: "$grades"},
    {
        $group: {
            _id: null,
            overallAvg: {$avg: "$grades.score"}
        }
    },
    // Store the overall average for comparison
    {
        $lookup: {
            from: "restaurants",
            pipeline: [
                {$unwind: "$grades"},
                {
                    $group: {
                        _id: "$cuisine",
                        avgScore: {$avg: "$grades.score"}
                    }
                }
            ],
            as: "cuisineAvgs"
        }
    },
    {$unwind: "$cuisineAvgs"},
    {
        $match: {
            $expr: {
                $gt: ["$cuisineAvgs.avgScore", "$overallAvg"]
            }
        }
    },
    {
        $project: {
            _id: 0,
            cuisine: "$cuisineAvgs._id",
            avgScore: "$cuisineAvgs.avgScore",
            overallAverage: "$overallAvg"
        }
    }
])

// ====================================================================================
// COMPLEX AGGREGATION SOLUTIONS
// ====================================================================================

// 16. Restaurants above their borough's average score
db.restaurants.aggregate([
    {$unwind: "$grades"},
    {
        $group: {
            _id: {
                borough: "$borough",
                restaurant_id: "$restaurant_id",
                name: "$name"
            },
            restaurantAvg: {$avg: "$grades.score"}
        }
    },
    {
        $group: {
            _id: "$_id.borough",
            boroughAvg: {$avg: "$restaurantAvg"},
            restaurants: {
                $push: {
                    restaurant_id: "$_id.restaurant_id",
                    name: "$_id.name",
                    avgScore: "$restaurantAvg"
                }
            }
        }
    },
    {$unwind: "$restaurants"},
    {
        $match: {
            $expr: {
                $gt: ["$restaurants.avgScore", "$boroughAvg"]
            }
        }
    },
    {
        $project: {
            borough: "$_id",
            restaurant: "$restaurants.name",
            restaurantScore: "$restaurants.avgScore",
            boroughAverage: "$boroughAvg"
        }
    }
])

// 17. Borough summary report
db.restaurants.aggregate([
    {$unwind: "$grades"},
    {
        $group: {
            _id: {
                borough: "$borough",
                restaurant_id: "$restaurant_id",
                name: "$name",
                cuisine: "$cuisine"
            },
            avgScore: {$avg: "$grades.score"}
        }
    },
    {
        $group: {
            _id: "$_id.borough",
            totalRestaurants: {$sum: 1},
            avgScore: {$avg: "$avgScore"},
            cuisines: {$push: "$_id.cuisine"},
            restaurants: {
                $push: {
                    name: "$_id.name",
                    score: "$avgScore"
                }
            }
        }
    },
    {
        $addFields: {
            mostCommonCuisine: {
                $arrayElemAt: [
                    {
                        $map: {
                            input: {
                                $slice: [
                                    {
                                        $sortByCount: {
                                            $unwind: "$cuisines"
                                        }
                                    },
                                    1
                                ]
                            },
                            as: "cuisine",
                            in: "$$cuisine._id"
                        }
                    },
                    0
                ]
            },
            bestRestaurant: {
                $arrayElemAt: [
                    {
                        $map: {
                            input: {
                                $slice: [
                                    {$sortArray: {input: "$restaurants", sortBy: {score: -1}}},
                                    1
                                ]
                            },
                            as: "rest",
                            in: "$$rest.name"
                        }
                    },
                    0
                ]
            }
        }
    },
    {
        $project: {
            borough: "$_id",
            totalRestaurants: 1,
            avgScore: {$round: ["$avgScore", 2]},
            mostCommonCuisine: 1,
            bestRestaurant: 1
        }
    }
])

// ====================================================================================
// GEOSPATIAL AND TEXT AGGREGATION SOLUTIONS
// ====================================================================================

// 21. Restaurants within coordinate range
db.restaurants.aggregate([
    {
        $match: {
            "address.coord.1": {$gte: 40.7, $lte: 40.8},
            "address.coord.0": {$gte: -74.1, $lte: -73.9}
        }
    },
    {
        $group: {
            _id: "$borough",
            count: {$sum: 1},
            restaurants: {$push: "$name"}
        }
    }
])

// 22. Group restaurants by first letter of name
db.restaurants.aggregate([
    {
        $group: {
            _id: {$substr: ["$name", 0, 1]},
            count: {$sum: 1}
        }
    },
    {$sort: {"_id": 1}}
])

// 24. Average coordinates by borough
db.restaurants.aggregate([
    {
        $group: {
            _id: "$borough",
            avgLongitude: {$avg: {$arrayElemAt: ["$address.coord", 0]}},
            avgLatitude: {$avg: {$arrayElemAt: ["$address.coord", 1]}},
            count: {$sum: 1}
        }
    }
])

// ====================================================================================
// TIME-BASED AGGREGATION SOLUTIONS
// ====================================================================================

// 26. Year with most restaurant inspections
db.restaurants.aggregate([
    {$unwind: "$grades"},
    {
        $group: {
            _id: {$year: "$grades.date"},
            inspectionCount: {$sum: 1}
        }
    },
    {$sort: {inspectionCount: -1}},
    {$limit: 1}
])

// 27. Restaurants inspected in 2014 with only 'A' grades
db.restaurants.aggregate([
    {$unwind: "$grades"},
    {
        $match: {
            $expr: {$eq: [{$year: "$grades.date"}, 2014]}
        }
    },
    {
        $group: {
            _id: "$restaurant_id",
            name: {$first: "$name"},
            grades: {$addToSet: "$grades.grade"}
        }
    },
    {
        $match: {
            grades: {$size: 1, $all: ["A"]}
        }
    }
])

// ====================================================================================
// STATISTICAL AGGREGATION SOLUTIONS
// ====================================================================================

// 32. Score ranges analysis
db.restaurants.aggregate([
    {$unwind: "$grades"},
    {
        $bucket: {
            groupBy: "$grades.score",
            boundaries: [0, 11, 21, 31, 41, 51, 61, 71, 81, 91, 101],
            default: "Other",
            output: {
                count: {$sum: 1},
                restaurants: {$addToSet: "$name"}
            }
        }
    }
])

// ====================================================================================
// RANKING AND COMPARISON SOLUTIONS
// ====================================================================================

// 37. Top 3 restaurants in each cuisine category
db.restaurants.aggregate([
    {$unwind: "$grades"},
    {
        $group: {
            _id: {
                cuisine: "$cuisine",
                restaurant_id: "$restaurant_id",
                name: "$name"
            },
            avgScore: {$avg: "$grades.score"}
        }
    },
    {$sort: {"_id.cuisine": 1, avgScore: -1}},
    {
        $group: {
            _id: "$_id.cuisine",
            topRestaurants: {
                $push: {
                    name: "$_id.name",
                    score: "$avgScore"
                }
            }
        }
    },
    {
        $project: {
            cuisine: "$_id",
            top3: {$slice: ["$topRestaurants", 3]}
        }
    }
])

// ====================================================================================
// BUSINESS INTELLIGENCE SOLUTIONS
// ====================================================================================

// 46. Market gaps analysis
db.restaurants.aggregate([
    {
        $group: {
            _id: {
                borough: "$borough",
                cuisine: "$cuisine"
            },
            count: {$sum: 1}
        }
    },
    {$match: {count: {$lt: 5}}},
    {
        $project: {
            _id: 0,
            borough: "$_id.borough",
            cuisine: "$_id.cuisine",
            restaurantCount: "$count",
            opportunity: "Market Gap"
        }
    },
    {$sort: {borough: 1, cuisine: 1}}
])

// ====================================================================================
// UTILITY AGGREGATIONS
// ====================================================================================

// Sample aggregation for data exploration
db.restaurants.aggregate([
    {$sample: {size: 5}},
    {
        $project: {
            name: 1,
            borough: 1,
            cuisine: 1,
            gradeCount: {$size: "$grades"},
            coordinates: "$address.coord"
        }
    }
])

// Count distinct values
db.restaurants.aggregate([
    {
        $group: {
            _id: null,
            uniqueBoroughs: {$addToSet: "$borough"},
            uniqueCuisines: {$addToSet: "$cuisine"}
        }
    },
    {
        $project: {
            _id: 0,
            boroughCount: {$size: "$uniqueBoroughs"},
            cuisineCount: {$size: "$uniqueCuisines"},
            boroughs: "$uniqueBoroughs"
        }
    }
])

// ====================================================================================
// PERFORMANCE TIPS
// ====================================================================================

/*
Performance Optimization Tips:

1. Use $match early in the pipeline to reduce document count
2. Use indexes on fields used in $match, $sort, and $group
3. Use $project to exclude unnecessary fields early
4. Consider using $allowDiskUse: true for large datasets
5. Use $limit after $sort when you only need top N results
6. Use $unwind carefully as it can significantly increase document count
7. Consider using $facet for multiple parallel aggregations

Example with performance optimizations:
db.restaurants.aggregate([
    {$match: {borough: "Manhattan"}},  // Filter early
    {$project: {name: 1, cuisine: 1, "grades.score": 1}}, // Project only needed fields
    {$unwind: "$grades"},
    {$group: {_id: "$cuisine", avgScore: {$avg: "$grades.score"}}},
    {$sort: {avgScore: -1}},
    {$limit: 10}
], {allowDiskUse: true})

Index suggestions:
- db.restaurants.createIndex({borough: 1})
- db.restaurants.createIndex({cuisine: 1})  
- db.restaurants.createIndex({"grades.score": 1})
- db.restaurants.createIndex({"grades.date": 1})
- db.restaurants.createIndex({name: "text"})
*/
