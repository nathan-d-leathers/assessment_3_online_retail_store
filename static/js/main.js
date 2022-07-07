document.getElementById('search-form').addEventListener('submit', (event)=>{
    event.preventDefault()
    const searchTerm = document.getElementById('product')

    axios.get('/products', {params:{query: searchTerm.value}}).then((response)=>{
        console.log('response?')
        console.log(response)
        document.getElementById('item_image').src = response.data.url
        document.getElementById('item_name').innerText ="Sorry, We're All Sold Out!"
    })
})