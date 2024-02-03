<script>
import Header from '../components/Header.vue'

export default{
    props: ['basket', 'addToBasket'],
    components: { Header }
}
</script>

<template>
    <div>
        <Header :basket="basket"/>
        <h1>Dostawa:</h1>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ab in
             odit, reiciendis fugit voluptate, dolore architecto beatae voluptates aliquam 
            quae delectus repudiandae explicabo, dignissimos
             labore consectetur temporibus saepe perspiciatis velit.</p>
    </div>
</template>

<style scoped>
div h1{
    font-size: 90px;
    margin-top: 150px;
    font-weight: 400;
}

p{
    font-size: 18px;
    margin: 20px 0;
}
</style>