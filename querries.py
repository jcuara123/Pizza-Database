# Menu list 
Menu = ''' Select one of the following
    1:
    2:
    3:
    4:
    5:
    6:
    7:
    8:
    9:
    10:
    '''

# -- 1) Count how many stores that sell Wings Deliver as well 
Count_Wings_AND_Deliver ='''
 SELECT COUNT(DISTINCT st_name) 
  FROM sides,
       store,
       Orders
 WHERE s_storekey = st_storekey AND 
       s_name LIKE "%Wings%" AND 
       st_orderkey = o_orderkey AND 
       o_dev = 1;
'''
#-- 2) for each store that carries beer, count how many delivery orders have been made
Count_Store_WithBeer = '''
SELECT COUNT(DISTINCT order_id) 
  FROM drink,
       Orders,
       store,
       Delivery
 WHERE order_id = o_orderkey AND 
       d_type = "beer" AND 
       o_drink = d_key
 GROUP BY st_storekey;
 ''' 
#-- 3) Count how many ordered pizzas that have mushrooms are in each type of pizza at Pizza Factory
Count_MushroomPizzas_Factory = '''
SELECT COUNT( * ) 
  FROM store,
       Orders,
       entree,
       toppings
 WHERE st_orderkey = o_orderkey AND 
       o_entree = e_key AND 
       e_ingredients LIKE "%Mushroom%" AND 
       st_name = "Pizza Factory";
 '''
 #-- 4) For each store, which drink is least ordered (which has the most stock)
ListStores_MostSoldDrink = ''' 
SELECT st_name,
       d_brand
  FROM store,
       drink
 WHERE d_storekey = st_storekey
 GROUP BY st_name
HAVING MAX(d_stock);
'''
#-- 5) For each customer that Dominos delivers to, find their order (entree, drink, side)
ListDeliveredOrder_FromCustomerDominos = '''
SELECT e_name,
       d_brand,
       s_name
  FROM Customer,
       entree,
       sides,
       drink,
       Orders,
       store,
       Delivery
 WHERE order_id = st_orderkey AND 
       st_orderkey = o_orderkey AND 
       o_custkey = c_key AND 
       o_drink = d_key AND 
       o_entree = e_key AND 
       o_side = s_key AND 
       st_name = "Dominos"
 GROUP BY c_name;
'''