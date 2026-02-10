import json

todo_list_json = '''{
    "todos": [
        { 
            "id": 1,
            "todo": "Do something nice for someone you care about",
            "completed": false,
            "userId": 152
        },
        {
            "id": 2,
            "todo": "Memorize a poem",
            "completed": true,
            "userId": 13
        },
        {
            "id": 3,
            "todo": "Watch a classic movie",
            "completed": true,
            "userId": 68
        },
        {
            "id": 4,
            "todo": "Watch a documentary",
            "completed": false,
            "userId": 84
        },
        {
            "id": 5,
            "todo": "Invest in cryptocurrency",
            "completed": false,
            "userId": 163
        },
        {
            "id": 6,
            "todo": "Contribute code or a monetary donation to an open-source software project",
            "completed": false,
            "userId": 69
        },
        {
            "id": 7,
            "todo": "Solve a Rubik's cube",
            "completed": true,
            "userId": 76
        },
        {
            "id": 8,
            "todo": "Bake pastries for yourself and neighbor",
            "completed": true,
            "userId": 198
        },
        {
            "id": 9,
            "todo": "Go see a Broadway production",
            "completed": false,
            "userId": 7
        },
        {
            "id": 10,
            "todo": "Write a thank you letter to an influential person in your life",
            "completed": true,
            "userId": 9
        },
        {
            "id": 11,
            "todo": "Invite some friends over for a game night",
            "completed": false,
            "userId": 104
        },
        {
            "id": 12,
            "todo": "Have a football scrimmage with some friends",
            "completed": false,
            "userId": 32
        },
        {
            "id": 13,
            "todo": "Text a friend you haven't talked to in a long time",
            "completed": true,
            "userId": 2
        },
        {
            "id": 14,
            "todo": "Organize pantry",
            "completed": false,
            "userId": 46
        },
        {
            "id": 15,
            "todo": "Buy a new house decoration",
            "completed": true,
            "userId": 105
        },
        {
            "id": 16,
            "todo": "Plan a vacation you've always wanted to take",
            "completed": true,
            "userId": 162
        },
        {
            "id": 17,
            "todo": "Clean out car",
            "completed": false,
            "userId": 71
        },
        {
            "id": 18,
            "todo": "Draw and color a Mandala",
            "completed": true,
            "userId": 6
        },
        {
            "id": 19,
            "todo": "Create a cookbook with favorite recipes",
            "completed": true,
            "userId": 53
        },
        {
            "id": 20,
            "todo": "Bake a pie with some friends",
            "completed": false,
            "userId": 162
        },
        {
            "id": 21,
            "todo": "Create a compost pile",
            "completed": false,
            "userId": 13
        },
        {
            "id": 22,
            "todo": "Take a hike at a local park",
            "completed": true,
            "userId": 37
        },
        {
            "id": 23,
            "todo": "Take a class at local community center that interests you",
            "completed": true,
            "userId": 65
        },
        {
            "id": 24,
            "todo": "Research a topic interested in",
            "completed": true,
            "userId": 130
        },
        {
            "id": 25,
            "todo": "Plan a trip to another country",
            "completed": false,
            "userId": 140
        },
        {
            "id": 26,
            "todo": "Improve touch typing",
            "completed": false,
            "userId": 178
        },
        {
            "id": 27,
            "todo": "Learn Express.js",
            "completed": false,
            "userId": 194
        },
        {
            "id": 28,
            "todo": "Learn calligraphy",
            "completed": false,
            "userId": 80
        },
        {
            "id": 29,
            "todo": "Have a photo session with some friends",
            "completed": true,
            "userId": 91
        },
        {
            "id": 30,
            "todo": "Go to the gym",
            "completed": true,
            "userId": 142
        }
    ],
    "total": 254,
    "skip": 0,
    "limit": 30
}'''
type(todo_list_json)

# todo_list_json[10:50] this is a string and we can slice it like a string but it will not give us the expected result because it is not a python dictionary it is a json data which is a string representation of a python dictionary
# Converting json data to python dictionary
todo_list_dict = json.loads(todo_list_json)

type(todo_list_json)
type(todo_list_dict)

print(todo_list_json)
print(todo_list_dict)

todo_list_dict['todos'][0]
todo_list_dict['todos'][0]['id']

#for todo in todo_list_dict.values():  this is the main parent have 4 child
for todo in todo_list_dict['todos']:
    todo_format = 'Id = {}\nTodo = {}\nStatus = {}\nUserId = {}'
    todo_format = todo_format.format(todo['id'], todo['todo'], todo['completed'], todo['userId'])
    print(todo_format+"\n")
    # print(f"Id = {todo['id']}\nTodo = {todo['todo']}\n")
    
# iterating over python dictionary
developer_data_dict = {
    "name": "John Doe",
    "age": 30,
    "email": "johndoe@example.com",
    "is_active": True,
    "skills": ["Python", "Django", "REST API"],
    "address": {
        "street": "123 Main Street",
        "city": "Karachi",
        "country": "Pakistan"
    }
}

# Converting python dictionary to json data
developer_data_json = json.dumps(developer_data_dict)

type(developer_data_dict)
type(developer_data_json)

print(developer_data_dict)
print(developer_data_json)

# writing json to a file
with open('todo.json', 'w') as f:
    json.dump(obj=developer_data_dict, fp=f)


# reading json from a file
with open('todo.json', 'r') as f:
    json_data = json.load(fp=f)

print(json_data)
type(json_data)