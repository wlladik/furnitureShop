<script >
import axios from 'axios';

export default{
    props: ['basket', 'deleteFromBasket'],
    data(){
        return{
            error: '',
            name: '',
            surname: '',
            email: '',
            phone: '',
        }
    },
    computed: {
        getSuma(){
            return this.basket.reduce((total, next) => total + parseFloat(next.price), 0)
        }
    },
    methods: {
        sendData(){

            if(this.name.length < 2)
                this.error = 'Znaczenie pola jest za krótke';
            else if(this.surname.length < 2)
             this.error = 'Znaczenie pola jest za krótke';
            else if(!this.email.includes('@') || !this.email.includes('.'))
                this.error = 'Email mieści bląd';
            else if(this.phone.length < 9 || typeof this.phone == 'number')
                this.error = 'Znaczenie pola jest za krótke, lub mieści nie dozwolone znaki';
            else if(this.basket.length == 0 || this.getSumma == 0)
                this.error = 'Kosz jest pusty...';
            else {
                this.error = ''

                
                const data = {
                    'name': this.name,
                    'surname': this.surname,
                    'email': this.email,
                    'phone': this.phone,
                    'suma': this.getSuma,
                    'basket': JSON.stringify(this.basket)
                }
                axios.post('http://127.0.0.1:8000/api/order-add/', data)
                    .then(res => {
                        this.error = res.data.result;
                        setTimeout(() =>{
                            location.href = res.data.url
                        }, 800)
                    })
            }
    
        }    
    }    
}
</script>

<template>
    <div>
        <h1>Order confirmation</h1>
        <div class="data">
            <div class="basket" v-if="this.basket.length > 0">
                <div class="item" v-for="el in basket" :key="el.slug">
                    <img :src="'/img/' + el.image" :alt="el.title" class="photos">
                    <h3>{{ el.title }}</h3>
                    <span>{{ el.price }} $</span>
                    <button @click="deleteFromBasket(el.slug)">Usunąć</button>
                </div>
                <hr>
                <span>Do spłaty: {{ getSuma }}$</span>
            </div>        
            <div v-else>
                <p>Niestety nie dodałesz żadnego produktu do kosza...</p>
            </div>    
            <form>
                <p class="error">{{ error }}</p>
                <input type="text" v-model="name" placeholder="Twoje imię">
                <input type="text" v-model="surname" placeholder="Twoje nazwisko">
                <input type="email" v-model="email" placeholder="Twój email">
                <input type="phone" v-model="phone" placeholder="Telefon">
                <button type="button" @click="sendData()">Kupuję</button>
            </form>
        </div>
    </div>
</template>

<style scoped>
.data {
    display: flex;
    justify-content: space-around;
    align-items: center;
    margin: 50px 0;
}

.data > div {
    width: 40%;
}

h1 {
    margin-top: 150px;
    font-weight: 400;
    font-size: 90px;
    text-align: center;
}
.item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
}
.item img {
    width: 60px;
}
.item h3 {
    color: #52585c;
    font-size: 15px;
    text-align: center;
}
.item span {
    font-weight: 600;
    color: #323232;
}

.item button, form button {
    border: 0;
    background: rgb(186, 43, 43);
    border-radius: 5px;
    padding: 7px 12px;
    cursor: pointer;
    color: #fff;
}

.item button:hover {
    background: rgb(133, 28, 28);
}

.items > span {
    font-weight: 600;
    color: #206E5B;
}

form input {
    width: 300px;
    padding: 10px 15px;
    border: 1.5px solid #575d61;
    border-radius: 2px;
    background: #d2d6d8;
    margin-bottom: 20px;
    display: block;
    color: #000000;
    outline: none;
    font-size: 15px;
}

form input::placeholder {
    color: rgba(64, 64, 64, 0.531);
}

form input:focus {
    border-color: #242424;
}

form button {
    background: #206E5B;
}

form button:hover {
    background: #134438;
}

.error {
    margin-bottom: 10px;
    color: rgb(181, 46, 46);
}

</style>