const updateBtns = document.getElementsByClassName('update-cart')

for (let i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(){
        let productId = this.dataset.product;
        let action = this.dataset.action;
        console.log('productId', productId, 'action:', action);

        console.log('USER:', user);
        if(user == 'AnonymousUser'){
            addCookieItem(productId, action)
        } else {
            updateUserOrder(productId, action);
        }
    });
}

function addCookieItem(productId, action){
    console.log('not signed in')
    if (action === 'add'){
        if (cart[productId] == undefined){
            cart[productId] ={'quantity':1};
        } else{
            cart[productId]['quantity'] += 1;
        }
    }
}


function updateUserOrder(productId, action){
    console.log('authenticated user');
    let url = '/update_item/'
    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken':csrftoken,
        }, 
        body:JSON.stringify({'productId':productId, 'action':action})
    })
    .then((response)=>{
        return response.json()
    })
    .then((data)=>{
        location.reload();
    });
}