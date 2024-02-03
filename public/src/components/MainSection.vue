<script>
export default{}
</script>

<template>
<div class="wrapper">
    <img src="/img/main_shop.svg" alt="main">
    <aside>
        <img src="/img/star.svg" alt="star">
        <h1>Shoppy</h1>
        <h2>twoje najliepsze</h2>
        <h3>mebli!</h3>
        <p>Kup teraz i otrzymaj gratis od nas!</p>
        <button>Zaczynamy zakup</button>
    </aside>
</div>
</template>

<style scoped>
.wrapper{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 150px;
}

.wrapper aside{
    margin-left: 50px;
    color: #373845;
}

.wrapper aside h1{
    font-weight: 400;
    font-size: 90px;
}

.wrapper aside h2,
.wrapper aside h3{
    font-weight: 400;
    font-size: 70px;
}

.wrapper aside h3{
    color: #5cddbc;
}

.wrapper aside p{
    font-size: 18px;
    widows: 500px;
    margin: 20px 0;
}

.wrapper aside button{
    font-weight: 700;
    font-size: 18px;
    color: #2f323a;
    background: #5cddbc;
    border-radius: 25px;
    border: 0;
    padding: 15px 25px;
    cursor: pointer;
    transition: all 600ms ease;
}

.wrapper aside button:hover{
    transform: translateY(-5px);
}
</style>