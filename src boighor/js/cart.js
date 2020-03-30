class Cart{

	constructor(products) {
		if (!this.storageSupported()){
			throw "Browser doesn't support localStorage"
		}

		this.products = products;
		//this.items = JSON.parse(localStorage.getItem('cart'))
	}

	find(id, source){

		for(var i = 0; i < source.length; i++){
			if(source[i].id == id){
				return source[i];
			}
		}
		return false;
	}

	/*
	*Add items to cart
	*/
	add(id, quantity = 1){

		//Find product from catalog, build object, add to storage
		if (localStorage.getItem('cart') === null || JSON.parse(localStorage.getItem('cart')).length === 0){
			var tempItem = this.find(id, this.products);
			var item = Object.assign({}, tempItem, {quantity: quantity});

			localStorage.setItem('cart', JSON.stringify([item]))

		}else if(this.find(id, JSON.parse(localStorage.getItem('cart')))){
			//Item already exists in cart, increase quantity

			var cartObj = JSON.parse(localStorage.getItem('cart'));

			var oldItem = this.find(id, JSON.parse(localStorage.getItem('cart')));
			var itemIndex = cartObj.findIndex(x => x.id === id);
			var newItem = Object.assign({}, oldItem, {quantity: (quantity + oldItem.quantity)});

			cartObj[itemIndex] = newItem;
			localStorage.setItem('cart', JSON.stringify(cartObj))
		
		}else{
			var tempItem = this.find(id, this.products);
			var item = Object.assign({}, tempItem, {quantity: quantity});

			var cartObj = JSON.parse(localStorage.getItem('cart'));
			cartObj.push(item)
			localStorage.setItem('cart', JSON.stringify(cartObj))
		}
		
	}

	/*
	*Show single item from cart
	*/
	show(id){
		return this.find(id, JSON.parse(localStorage.getItem('cart')))
	}

	/*
	*List all items in cart
	*/
	all(){
		return  JSON.parse(localStorage.getItem('cart'));
	}

	/*
	*Sum cost of items in cart
	*/
	sum(){
		var sum = 0;
		var items = JSON.parse(localStorage.getItem('cart'));

		for (var i = 0; i < items.length; i++) {
			sum += (items[i].price * items[i].quantity)
		}
		return sum;
	}

	/*
	*Remove an item from cart
	*/
	remove(id){
		
		var items = JSON.parse(localStorage.getItem('cart'));
		var index = items.findIndex(x => x.id == id);

		if (index >= 0){
			items.splice(index, 1)
			localStorage.setItem('cart', JSON.stringify(items));
		}
	}

	/*
	*Update cart item by its quantity
	*/
	update(id, quantity){
		var cartObj = JSON.parse(localStorage.getItem('cart'));

		var oldItem = this.find(id, cartObj)
		var itemIndex = cartObj.findIndex(x => x.id === id);
		var updatedItem = Object.assign({}, oldItem, {quantity: quantity})
		cartObj[itemIndex] = updatedItem;

		//Save back to storage
		localStorage.setItem('cart', JSON.stringify(cartObj))
	}

	/**
	*Remove all items from cart
	*/
	clear(){
		localStorage.removeItem('cart')
	
	}

	storageSupported(){

		return (typeof(Storage) !== "undefined") ? true : false;
	}
}

export default Cart;
