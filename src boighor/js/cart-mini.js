var miniCart = new Cart();

function loadMiniCart(){
    var miniCartData = miniCart.all();
    if (miniCartData !== null || miniCartData !== undefined){
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

function getCartNotification() {
    var empty = '';
    var miniCartData = miniCart.all();
    if (miniCartData !== null) {
        document.getElementById("cart_noti").innerHTML = miniCartData.length;
    }
    else {
        empty += '<a class="cartbox_active" href="#"></a>';
        document.getElementById("shopcart").innerHTML = empty;
    }
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