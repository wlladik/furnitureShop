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
    <h1>O nas: </h1>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing
         elit. Vel tempora aut laborum doloribus ea, vero aperiam
          eius ipsa iusto eos saepe soluta doloremque 
        quasi reprehenderit aliquid explicabo commodi at? Officiis!
    <br><br>
    Lorem ipsum, dolor sit amet consectetur adipisicing elit. Impedit vero dolore quisquam.
    <br><br>
    Lorem ipsum dolor sit amet consectetur, adipisicing elit. Sunt?
    </p>
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