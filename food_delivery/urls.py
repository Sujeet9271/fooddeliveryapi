"""Food__Delivery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include


from city import views as city
from order import views as order
from menu import views as menu
from restaurant import views as restaurant


# urlpatterns = [

#             path('admin/',admin.site.urls),
#             path('cities/',include('city.urls')),
#             path('cities/<int:city>/', include('restaurant.urls')),
#             path('cities/<int:city>/restaurant/<int:restaurant>/', include('menu.urls')),


# ]


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('',city.index),
    # ---------------------------------------------------------------For Customers-----------------------------------------------------------------------
    
    

    #  Detail of Available Restaurants with their detail menu with category and sub category from the selected City
    path('detail/cities/',city.detail_city, name='detail_city'),

    # for Viewing the Available restaurants in the city
    path('detail/cities/<int:city>/', restaurant.detailed_restaurant, name='detailed_restaurants'),

    path('cart/', order.cart, name='cart'),

    path('cart/create_order/', order.create_order, name = 'create order'),

    # For Viewing the Available Cities
    path('cities/',city.city,name='city'),

    # for Viewing all the Available restaurants in the city
    path('cities/<int:city>/', restaurant.restaurant, name='restaurants'),

    # for Viewing all the Available Veg only restaurants in the city
    path('cities/<int:city>/restaurants/veg_only/', restaurant.veg_restaurant, name='veg restaurants'),

    # Detail view of Restaurant's Menu
    path('cities/<int:city>/restaurant/<int:restaurant>/', order.create_cart, name='create order'),

    # Restaurant Menu's Available Categories
    path('cities/<int:city>/restaurant/<int:restaurant>/category/', menu.restaurant_category, name='restaurant_category'),

    # Restaurant Menu's Detail view of selected category
    path('cities/<int:city>/restaurant/<int:restaurant>/category/<int:category>/', menu.restaurant_category_detail, name='restaurant_category_detail'),

    # Restaurant Menu's Available Sub_Categories of selected category
    path('cities/<int:city>/restaurant/<int:restaurant>/category/<int:category>/subcategory/', menu.restaurant_category_subcategory, name='restaurant_category_subcategory'),

    # Restaurant Menu's Detail view of selected Sub_category 
    path('cities/<int:city>/restaurant/<int:restaurant>/category/<int:category>/subcategory/<int:subcategory>/', menu.restaurant_category_subcategory_detail, name='restaurant_category_subcategory_detail'),

    # Restaurant Menu's Available Item from selected Sub_Category
    path('cities/<int:city>/restaurant/<int:restaurant>/category/<int:category>/subcategory/<int:subcategory>/item/', menu.restaurant_menu, name='restaurant_category_subcategory_items'),

    path('cities/<int:city>/restaurant/<int:restaurant>/category/<int:category>/subcategory/<int:subcategory>/item/<int:item>/', menu.restaurant_category_subcategory_item_detail, name='restaurant_category_subcategory_item_detail'),
    
    # -------------------------------------------------------------For Restaurants-----------------------------------------------------------------------
   
    # for  viewing and updating orders from staff end 

    # For Restaurant's DashBoard
    path('cities/<int:city>/restaurant/<int:restaurant>/staff/orders/', order.order_received,name='orders received'),

    # For Updating Received Order's Status
    path('cities/<int:city>/restaurant/<int:restaurant>/staff/orders/<int:id>/', order.order_update,name='update order'),

    # for viewing,updating and deleting menu items from staff end
    # Detail View of restaurant's menu
    path('cities/<int:city>/restaurant/<int:restaurant>/staff/menu/', menu.detail_menu, name='restaurant_menu'),

    # View or Add Category
    path('cities/<int:city>/restaurant/<int:restaurant>/staff/menu/category/', menu.category,name='category'),

    # Update or Delete Category
    path('cities/<int:city>/restaurant/<int:restaurant>/staff/menu/category/<int:category>/update/', menu.update_category,name='update category'),

    # View or Add Sub_Category
    path('cities/<int:city>/restaurant/<int:restaurant>/staff/menu/category/<int:category>/subcategory/', menu.subcategory,name='subcategory'),

    # Update or Delete Sub_Category
    path('cities/<int:city>/restaurant/<int:restaurant>/staff/menu/category/<int:category>/subcategory/<int:subcategory>/', menu.update_subcategory,name='update_subcategory'),
    
    # Add new Item in the menu
    path('cities/<int:city>/restaurant/<int:restaurant>/staff/menu/category/<int:category>/subcategory/<int:subcategory>/item/', menu.add_menu,name='add menu'),

    # Update or Delete Menu Item
    path('cities/<int:city>/restaurant/<int:restaurant>/staff/menu/category/<int:category>/subcategory/<int:subcategory>/item/<int:item>/', menu.update_item,name='subcategory_item_detail'),

    

    

    

    

    
]
