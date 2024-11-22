async function apirearch() {
    const res = await fetch('https://api.bx33661.com/');
    const data = await res.json();
    return
}

apirearch().then(res => {
    console.log(res)
}).catch(err => {
    console.error('Error:', err)
})