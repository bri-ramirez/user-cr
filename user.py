from mysqlconnection import connectToMySQL

class User:
    esquema = "users_schema"

    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.esquema).query_db(query)
        
        users = []
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( first_name , last_name , email ) VALUES ( %(fname)s , %(lname)s , %(email)s );"
        return connectToMySQL(cls.esquema).query_db( query, data )