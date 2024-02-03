<script>
import axios from 'axios'

export default{
    props: ['addToBasket'],
    data(){
        return{
            items: [],
        }
    },
    async mounted(){
        try{
            const res = await axios.get('http://127.0.0.1:8000/api/items/?format=json');
            this.items = res.data;
        }catch(error){
            console.error(error);
        }
    },
}
</script>

<template>
    <div class="items">
        <div class="item" v-for="el in items" key="el.slug">
            <img :src="'/img/' + el.image" :alt="el.title" class="photos">
            <h3>{{ el.title }}</h3>
            <p>{{ el.desc }}</p>
            <div class="bottom">
                <span>{{ el.price }} $</span>
                <img src="/img/kosz.svg" :alt="el.title" @click="addToBasket(el)">
            </div>
        </div>
    </div>
</template>

<style scoped>
.items{
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
}

.items .item{
    margin-bottom: 100px;
    width: 350px;
    padding: 15px;
    background: #f4f4f4;
}

.items .item img.photos{
    width: 100%;
}

.items .item h3{
    margin: 12px 0;
    font-size: 20px;
}

.items .item p{
    margin: 10px 0;
    font-size: 15px;
    width: 90%;
}

.items .item .bottom{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 10px;
}

.items .item .bottom span{
    color: #216e5b;
    font-weight: 700;  
}

.items .item .bottom img{
    cursor: pointer;
    transition: all 600ms ease;
}

.items .item .bottom img:hover{
    transform: scale(1.2);
}

</style>