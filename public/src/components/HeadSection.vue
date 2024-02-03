<script>
export default{}
</script>

<template>
<div class="wrapper">
    <div>
        <h1>Shoppy</h1>
        <h2>wybierz sobie najlepsze meble!</h2>
    </div>
    <div>
        <img src="/img/main_shop.svg" alt="main">
    </div>
</div>
</template>

<style scoped>
.wrapper{
    background: #5cddbc;
    width: 104%;
    position: relative;
    right: 13%;
    display: flex;
    padding: 0 12%;
    justify-content: space-between;
    align-items: center;
    height: 240px;
    color: #216F5b;
    margin: 60px 0;
}

.wrapper h1{
    font-size: 70px;
    font-weight: 700;
}

.wrapper h2{
    font-size: 30px;
    font-weight: 400;
    margin-top: 15px;
}

.wrapper img {
    height: 230px;
    position: relative;
    top: 8px;
    right: 30px;
}

</style>