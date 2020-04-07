// class Cart{
//     //constructor(products) {
//     constructor(){
//        if (!this.storageSupported()){
//           throw "Browser doesn't support localStorage"
//        }
//        // this.products = products;
//        //this.items = JSON.parse(localStorage.getItem('cart'))
//     }
//     find(id, size, source){
//        for(var i = 0; i < source.length; i++){
//           if(source[i].id == id && source[i].size == size){
//              return source[i];
//           }
//        }
//        return false;
//     }
//     findSizeIndex(id, source, size){
//        for(var i = 0; i < source.length; i++){
//           if(source[i].id == id && source[i].size == size){
//              return i;
//           }
//        }
//        return false;
//     }
//     /*
//     *Add items to cart
//     */         
//     add(id, quantity = 1, size, price, name, page, brand, image, category = 'men'){
//        //Find product from catalog, build object, add to storage
//        if (localStorage.getItem('cart') === undefined || localStorage.getItem('cart') === null || JSON.parse(localStorage.getItem('cart')).length === 0){
//           var item = Object.assign({}, {id: id, quantity: quantity, size: size, price: price, name: name, page: page, brand: brand, image: image, category: category});
//           localStorage.setItem('cart', JSON.stringify([item]))
//        }else if(this.find(id, size, JSON.parse(localStorage.getItem('cart'))) != false){
//           //Item already exists in cart, increase quantity
//           var cartObj = JSON.parse(localStorage.getItem('cart'));
//           var oldItem = this.find(id, size, cartObj);
//           var itemIndex = this.findSizeIndex(id, cartObj, size);
//           var newItem = Object.assign({}, oldItem, {quantity: (quantity + oldItem.quantity), size: size, price: price, name: name, page: page, brand: brand, image: image, category: category});
//           cartObj[itemIndex] = newItem;
//           localStorage.setItem('cart', JSON.stringify(cartObj));
//        }else{
//           var item = Object.assign({}, {id: id, quantity: quantity, size: size, price: price, name: name, page: page, brand: brand, image: image, category: category});
//           var cartObj =  JSON.parse(localStorage.getItem('cart'));
//           cartObj.push(item)
//           localStorage.setItem('cart', JSON.stringify(cartObj))
//        }
//     }
//     /*
//     *Show single item from cart
//     */
//     show(id){
//        return this.find(id, JSON.parse(localStorage.getItem('cart')))
//     }
//     /*
//     *List all items in cart
//     */
//     all(){
//        return  JSON.parse(localStorage.getItem('cart'));
//     }
//     /*
//     *Sum cost of items in cart
//     *TODO - get price into object
//     */
//     sum(){
//        var sum = 0;
//        var items = JSON.parse(localStorage.getItem('cart'));
//        for (var i = 0; i < items.length; i++) {
//           sum += (items[i].price * items[i].quantity)
//        }
//        return sum;
//     }
//     /*
//     *Remove an item from cart
//     */
//     remove(id, size){
       
//        var items = JSON.parse(localStorage.getItem('cart'));
//        var index = this.findSizeIndex(id, items, size)

//        if (index >= 0){
//           items.splice(index, 1)
//           localStorage.setItem('cart', JSON.stringify(items));
//        }
//     }
//     /*
//     *Update cart item by its quantity
//     */
//     update(id, quantity, size){
//        var cartObj = JSON.parse(localStorage.getItem('cart'));

//        var oldItem = this.find(id, size, cartObj)
//        var itemIndex = this.findSizeIndex(id, cartObj, size)
//        var updatedItem = Object.assign({}, oldItem, {quantity: quantity})
//        cartObj[itemIndex] = updatedItem;

//        //Save back to storage
//        localStorage.setItem('cart', JSON.stringify(cartObj))
//     }
//     /**
//     *Remove all items from cart
//     */
//     clear(){
//        localStorage.removeItem('cart')
//     }
//     storageSupported(){
//        return (typeof(Storage) !== "undefined") ? true : false;
//     }
// };

var miniCart = new Cart();
var miniCartData = miniCart.all();

function loadMiniCart(){
    var cartCount = '<span>'+ miniCartData.length.toString() +' items</span><span>Cart Subtotal</span>'
    var cartTotal = 'RM' + miniCart.sum().toString();
    var miniCartHTML = '';

    if (miniCartData.length !=0){
      for (i=0; i<miniCartData.length; i++){
         miniCartHTML += '<div class="item01 d-flex"><div class="thumb"><a onclick="openPage(\'' + miniCartData[i].page + '\')"><img src="'+ miniCartData[i].image +'"></a></div>';
         miniCartHTML += '<div class="content"><h6><a onclick="openPage(\'' + miniCartData[i].page + '\')">'+ miniCartData[i].name +'</a></h6><span class="prize">RM '+ miniCartData[i].price +'</span>';
         miniCartHTML += '<div class="product_prize d-flex justify-content-between"><span class="qun">Quantity: ' + miniCartData[i].quantity + '</span>';
         miniCartHTML += '<ul class="d-flex justify-content-end"><li><a onclick="removeFromCart(\''+ miniCartData[i].id + '\', \''+ miniCartData[i].size +'\')"><i class="zmdi zmdi-delete"></i></a></li></ul></div></div></div>';
      }
    }
    else {
        miniCartHTML = '<div class="item01 d-flex">Cart is empty!</div>'
    }
    document.getElementById('cart_total').innerHTML = cartTotal;
    document.getElementById('cart_count').innerHTML = cartCount;
    document.getElementById('mini_cart').innerHTML = miniCartHTML;
}

loadMiniCart();

function openPage(id){
    link = 'http://custlrwa.ddns.net:8000/page/' + id.toString() + '/';
    openLink(link, "pageRespData");
};
function openLink(url, storage){ //sends search request to backend for JSON response
    // Create a request variable and assign a new XMLHttpRequest object to it.
    var request = new XMLHttpRequest()
    
    // Open a new connection, using the GET request on the URL endpoint
    request.open('GET', url, true)

    request.onload = function loadHTML(){
        var resultText = request.responseText;
        sessionStorage.setItem(storage, resultText);
        var pageCategory = JSON.parse(resultText)
        var page = 'single-product-' + pageCategory.category.toLowerCase() + '.html';
        window.location.replace(page);
    }
    // Send request
    request.send();
}

function removeFromCart(id, size){
    cart.remove(id, size);
    loadMiniCart();
}