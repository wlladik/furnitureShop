<script>
import Header from '../components/Header.vue'
import OrderForm from '../components/OrderForm.vue';

export default{
  props: ['basket', 'deleteFromBasket'],
  components: { Header, OrderForm }
}

</script>

<template>
  <div>
    <Header :basket="basket"/>
    <OrderForm :basket="basket" :deleteFromBasket="deleteFromBasket"/>
  </div>
</template>
