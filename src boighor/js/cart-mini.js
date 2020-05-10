var miniCart = new Cart();

// loads minicart popup
function loadMiniCart(){
    var miniCartData = miniCart.all();
    if (miniCartData != null || miniCartData != undefined){
        var cartCount = '<span>'+ miniCartData.length.toString() +' items</span><span>Cart Subtotal</span>'
        var cartTotal = 'RM' + miniCart.sum().toFixed(2).toString();
        var miniCartHTML = '';
        for (i=0; i<miniCartData.length; i++){
            miniCartHTML += '<div class="item01 d-flex"><div class="thumb"><a onclick="openPage(\'' + miniCartData[i].page + '\')"><img src="'+ miniCartData[i].image +'"></a></div>';
            miniCartHTML += '<div class="content"><h6><a onclick="openPage(\'' + miniCartData[i].page + '\')">'+ miniCartData[i].name +'</a></h6><span class="prize">RM '+ miniCartData[i].price +'</span>';
            miniCartHTML += '<div class="product_prize d-flex justify-content-between"><span class="qun">Quantity: ' + miniCartData[i].quantity + '</span>';
            miniCartHTML += '<ul class="d-flex justify-content-end"><li><a onclick="removeFromCart(\''+ miniCartData[i].id + '\', \''+ miniCartData[i].size +'\')"><i class="zmdi zmdi-delete"></i></a></li></ul></div></div></div>';
        }
        document.getElementById('cart_total').innerHTML = cartTotal;
        document.getElementById('cart_count').innerHTML = cartCount;
    }
    else {
        miniCartHTML = '<div class="item01 d-flex">Cart is empty!</div>'
    }
    document.getElementById('mini_cart').innerHTML = miniCartHTML;
    // update cart notif here
    getCartNotification();
}

// updates cart icon in header
function getCartNotification() {
    var empty = '';
    var miniCartData = miniCart.all();
    if (miniCartData != null) {
        if (miniCartData.length != 0){
            document.getElementById("shopcart").innerHTML = '<span class="product_qun">' + miniCartData.length + '</span>';
        }
        else {
            empty = '';
            document.getElementById("shopcart").innerHTML = empty;
        }
    }
}

loadMiniCart();

// opens specific product in cart
function openPage(id){
    link = 'http://custlrwa.ddns.net:8000/page/' + id.toString() + '/';
    openCartLink(link, "pageRespData");
};
function openCartLink(url, storage){ //sends search request to backend for JSON response
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

// removes item from cart
function removeFromCart(id, size){
    cart.remove(id, size);
    loadMiniCart();
}