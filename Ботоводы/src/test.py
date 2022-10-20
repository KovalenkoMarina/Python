import db_api

db = db_api.Database('db_api/database/shop_database.db')
# db.add_item(id=1, name = 'Помидоры', count = 30, photo_path = 'db_api/database/product_photo/tomat.jpg')
# db.add_item(id=2, name = 'Огурцы', count = 20, photo_path = 'db_api/database/product_photo/cocunber.jpg')
# db.add_item(id=3, name = 'Тыква', count = 45, photo_path = 'db_api/database/product_photo/pumpkin.jpg')
# db.add_item(id=4, name = 'Кабачки', count = 15, photo_path = 'db_api/database/product_photo/marrow.jpg')


print(db.select_all_items())

print(db.get_items_count())