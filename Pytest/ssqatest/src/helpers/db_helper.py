# import pymysql

# def read_from_db(sql):

#     connection = pymysql.connect('123.0.0.1', port=8889,
#                                 user='root', password='root') # creates a connection to the database

#     # execute the query
#     try:
#         cursor = connection.cursor(pymysql.cursors.DictCursor) # this will return a dictionary
#         cursor.execute(sql) # execute the sql
#         db_data = cursor.fetchall() # this will return a list of dictionaries
#         cursor.close() # close the connection
#     finally:
#         connection.close() # close the connection no matter what

#     return db_data

# def get_order_from_db_by_order_number(order_no):

#     sql = f"SELECT * FROM localdemostore.wp_posts WHERE ID = {order_no} AND post_type = 'shop_order';"

#     db_order = read_from_db(sql)
    
#     return db_order
