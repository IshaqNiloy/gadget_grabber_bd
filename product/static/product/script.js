var quantity = 1;
function plus(){
    quantity++;
    document.getElementById("display-quantity").value = quantity;
}

function minus(){
    quantity--;
    if(quantity >=1 ){
        document.getElementById("display-quantity").value = quantity;
    }
    else{
        quantity = 1
        document.getElementById("display-quantity").value = quantity;
    }

}

function showAlert(){
    document.GetElementById("cart-message").style.display = 'block';

}


















