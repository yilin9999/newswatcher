db.auth('root', 'root5566')
db = db.getSiblingDB('newswatcher')

db.createUser(
{
    user: "david",
    pwd: "newsgogogo",
    roles: [
      { role: "readWrite", db: "newswatcher" }
    ]
})
