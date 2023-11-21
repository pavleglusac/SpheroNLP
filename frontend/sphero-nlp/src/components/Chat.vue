<template>
    <div class="h-100 w-100">
        <section ref="chatArea" class="chat-area">
            <p v-for="(message, index) in messages" class="message" :class="{ 'message-out': message.author === 'you', 'message-in': message.author !== 'you' }" :key="index">
            {{ message.body }}
            </p>
            <p class="mb-5"></p>
        </section>
        <div style="display: flex; justify-content: center; margin-top: -5%;">
            <div class="input-group w-75" style="">
                <input type="text" class="form-control rounded-extra" placeholder="Type your message..." 
                aria-label="Chat message input" v-model="youMessage" @keydown.enter.prevent="sendMessage('out')">
                <button class="btn btn-primary rounded-end" type="button" @click="sendMessage('out')">Send</button>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

    export default {
        data() {
            return {
                messages: [
                    {
                        body: 'Dobrodošli, ja sam SpheroBot! Tu sam da pretvorim Vaše rečenice u programski kod!',
                        author: 'bob'
                    },
                    /*{
                        body: 'U redu, idi dole jedno 50cm, zatim se rotiraj za 90 stepeni ulevo i idi pravo 1m.',
                        author: 'you'
                    },
                    {
                        body: 'Izvršavam...',
                        author: 'bob'
                    }*/
                ],
                bobMessage: '',
                youMessage: ''
            }
        },
        methods: {
            async sendMessage(direction) {
                let code = await this.sendRequest();
                this.$eventBus.emit('code', code);
                this.$emit('newMessage', code);
                this.addToChat(direction);
            },

            clearAllMessages() {
                this.messages = []
            },

            async sendRequest() {
                try {
                    const response = await axios.post('http://localhost:8000/translate', {
                        text: this.youMessage
                    });
                    console.log(response.data);
                    return response.data;
                } catch (error) {
                    console.error('Error fetching data:', error);
                    throw error;
                }
            },

            addToChat(direction) {
                if (!this.youMessage && !this.bobMessage) {
                    return
                }
                if (direction === 'out') {
                    this.messages.push({body: this.youMessage, author: 'you'})
                    this.youMessage = ''
                } else if (direction === 'in') {
                    this.messages.push({body: this.bobMessage, author: 'bob'})
                    this.bobMessage = ''
                } else {
                    alert('something went wrong')
                }
                this.$nextTick(() => {
                    this.$refs.chatArea.scrollTop = this.$refs.chatArea.scrollHeight;
                });
            }
        }
    }

</script>

<style scoped>
.chat-area {
/*   border: 1px solid #ccc; */
  background: white;
  height: 100%;
  width: 100%;
  padding: 1em;
  overflow: auto;
  box-shadow: 2px 2px 5px 2px rgba(0, 0, 0, 0.3)
}
.message {
  width: 45%;
  border-radius: 10px;
  padding: .7em;
  font-size: .9em;
}
.message-out {
  background: #0090CD;
  color: white;
  margin-left: 55%;
}
.message-in {
  background: #212529;
  color: white;
}
.chat-inputs {
  display: flex;
  justify-content: space-between;
}

</style>