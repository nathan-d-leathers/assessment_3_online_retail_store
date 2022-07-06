document.getElementById('search-form').addEventListener('submit', (event)=>{
    event.preventDefault()
    const searchTerm = document.getElementById('product')

    axios.get('/products', {params:{query: searchTerm.value}}).then((response)=>{
        console.log('response?')
        console.log(response)
        // newImage = document.createElement('img')
        // newImage.src = response.data.url
        // const soldOut = document.createElement('h1')
        // soldOut.innerText = 'Sorry! Sold Out!'
        // soldOut.style.display = "inline-block"
        // document.body.appendChild(newImage)
        // document.body.appendChild(soldOut)
        document.getElementById('item_image').src = response.data.url
        document.getElementById('item_name').innerText ="Sorry, We're All Sold Out!"
        // console.log(return_statement)
    })
})