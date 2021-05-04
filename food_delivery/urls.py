from django.contrib import admin
from django.urls import path,include

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

from city import views as city
from order import views as order
from menu import views as menu
from restaurant import views as restaurant
from accounts import views as accounts
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('admin/', admin.site.urls),
   
    path('token/refresh/', TokenRefreshView.as_view(),name="token_refresh"),
    path('token/verify/', TokenVerifyView.as_view(),name="token_verify"),
    # ---------------------------------------------------------------For Customers-----------------------------------------------------------------------
    
    path('accounts/login/', accounts.customer_login, name='login'),
    path('accounts/register/', accounts.customer_register, name = 'customer'),
    path('accounts/logout/', accounts.BlacklistTokenView, name='logout'),
    path('accounts/profile/',accounts.profile),

    #  Detail of Available Restaurants with their detail menu with category and sub category from the selected City
    path('detail/cities/',city.detail_city, name='detail_city'),

    # for Viewing the Available restaurants in the city
    path('detail/cities/<int:city>/', restaurant.detailed_restaurant, name='detailed_restaurants'),

    path('cart/', order.cart, name='cart'),

    path('cart/<int:id>/', order.cart_delete, name='delete item'),

    path('cart/place_order/', order.place_order, name = 'place order'),

    path('myorders/', order.myorders, name='My Orders'),

    # For Viewing the Available Cities
    path('cities/',city.city,name='city'),

    # for Viewing all the Available restaurants in the city
    path('cities/<int:city>/', restaurant.restaurant, name='restaurants'),

    path('cities/<int:city>/res/<int:restaurant>/', restaurant.rate_restaurant, name='rate restaurants'),

    # for Viewing all the Available Veg only restaurants in the city
    path('cities/<int:city>/restaurant/veg_only/', restaurant.veg_restaurant, name='veg restaurants'),

    # Detail view of Restaurant's Menu
    path('cities/<int:city>/restaurant/<int:restaurant>/', order.create_cart, name='create order'),

    path('cities/<int:city>/restaurant/<int:restaurant>/item/<int:id>/', menu.rate_item, name='rating item'),

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
   
    path('cities/<int:city>/restaurant/<int:restaurant>/staff/login/', accounts.staff_login, name='staff login'),    
    path('cities/<int:city>/restaurant/<int:restaurant>/staff/register/', accounts.staff_register, name="staff register"),
    # for  viewing and updating orders from staff end 

    path('cities/<int:city>/restaurant/<int:restaurant>/staff/orders/all/',order.allorders,name='Orders'),

    # For Restaurant's DashBoard
    path('cities/<int:city>/restaurant/<int:restaurant>/staff/orders/today/', order.order_received,name='orders received'),

    # For Updating Received Order's Status
    path('cities/<int:city>/restaurant/<int:restaurant>/staff/orders/<int:id>/', order.order_update,name='update order'),

    # for viewing,updating and deleting menu items from staff end
    # Detail View of restaurant's menu
    path('cities/<int:city>/restaurant/<int:restaurant>/staff/menu/', menu.detail_menu, name='restaurant_menu'),


    path('cities/<int:city>/restaurant/<int:restaurant>/staff/menu/allitems/', menu.allitems, name='all_items'),


    path('cities/<int:city>/restaurant/<int:restaurant>/staff/menu/allsubs/', menu.allsub, name='all_subcategory'),

    # View or Add Category
    path('cities/<int:city>/restaurant/<int:restaurant>/staff/menu/category/', menu.category,name='category'),

    # Update or Delete Category
    path('cities/<int:city>/restaurant/<int:restaurant>/staff/menu/category/<int:category>/update/', menu.update_category,name='update category'),

    # View or Add Sub_Category
    path('cities/<int:city>/restaurant/<int:restaurant>/staff/menu/category/<int:category>/subcategory/', menu.subcategory,name='category_subcategory'),

    # Update or Delete Sub_Category
    path('cities/<int:city>/restaurant/<int:restaurant>/staff/menu/category/<int:category>/subcategory/<int:subcategory>/', menu.update_subcategory,name='update_subcategory'),
    
    # Add new Item in the menu
    path('cities/<int:city>/restaurant/<int:restaurant>/staff/menu/category/<int:category>/subcategory/<int:subcategory>/items/', menu.add_item,name='category_subcategory_item_add'),

    # Update or Delete Menu Item
    path('cities/<int:city>/restaurant/<int:restaurant>/staff/menu/category/<int:category>/subcategory/<int:subcategory>/item/<int:item>/', menu.update_item,name='category_subcategory_item_update'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
