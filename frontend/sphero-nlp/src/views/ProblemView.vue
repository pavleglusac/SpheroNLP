<script setup>
import Chat from '../components/Chat.vue';
import Navbar from '../components/Navbar.vue'
</script>

<template>
  <main>
    <Navbar />
    <div class="d-flex" style="height:90%;">
        <div id="maze-div" class="w-50" style="height: 100%; border-right: 2px solid black;">
            <div class="h-100" style="display: flex; flex-direction: column;" ref="cont1">
                <div class="box p-3" ref="topBox1" style="height: 30%;" id="topBox1">
                    <h3>
                        Problem broj {{ $route.params.id }}
                    </h3>
                    <p>
                        Potrebno je da napravite 5 krugova oko stola. Sto je oznacen crvenom bojom.

                    </p>
                </div>
                <div class="resizer" @mousedown="startResize" id="resizer-left"></div>
                <div class="box p-3 d-flex w-100" style="height: 69%; justify-content: center;" ref="bottomBox1" id="bottomBox1">
                    <img src="https://as2.ftcdn.net/jpg/01/36/00/76/1000_F_136007620_CnJyQqcd3giJLsJGsHsLEXl5E9oA56X7.jpg" style="max-height: 100%; max-width: 100%;" class="mx-0" />
                </div>
            </div>
        </div>
        <div id="code-div" class="w-50" style="height: 100%;">
            <div class="h-100" style="display: flex; flex-direction: column;" ref="cont2">
                <div class="box p-1" ref="topBox2" style="height: 50%;" id="topBox2">
                    <Chat />
                </div>
                <div class="resizer" @mousedown="startResize" id="resizer-right"></div>
                <div class="box p-2" style="height: 49%;" ref="bottomBox2" id="bottomBox2">
                    <h5>Rezultujući kod</h5>
                    <pre v-highlightjs>
                        <code class="javascript">
async function startProgram() {
    setMainLed({ r: 0, g: 0, b: 255 });
    await speak("Hello Square", true);
    await delay(1);
    for (var _i1 = 0; _i1 &lt; 4; _i1++) {
        setMainLed(getRandomColor());
        await Sound.Game.Coin.play(true);
        await roll((getHeading() + 90), 60, 1);
        await delay(1);
    }

}

                        </code>
                    </pre>
                </div>
            </div>
        </div>
    </div>
  </main>
</template>

<style scoped>
.box {
  background-color: #e9ecef;
  /* flex-grow: 1; */
}

.resizer {
  height: 2px;
  background: #000;
  cursor: ns-resize;
}

#maze-div {
  flex: 0 0 40%; /* flex-grow, flex-shrink, flex-basis */
}

#code-div {
  flex: 0 0 60%; /* flex-grow, flex-shrink, flex-basis */
}

</style>

<script>
export default {
  methods: {
    startResize(element) {
        // remove css align items stretch
      document.addEventListener('mousemove', this.performResize);
      document.addEventListener('mouseup', this.stopResize);
    },
    performResize(event) {
        console.log(event);
        let id = event.target.id;
        event.stopPropagation();
        if(id == "resizer-left" || id == "bottomBox1" || id == "topBox1") {
            const rect = this.$refs.topBox1.getBoundingClientRect();
            const newHeight = event.clientY - rect.top;
            this.$refs.topBox1.style.height = `${newHeight}px`;
            this.$refs.bottomBox1.style.height = `${this.$refs.cont1.clientHeight - newHeight}px`;
        } else if(id == "resizer-right" || id == "bottomBox2" || id == "topBox2") {
            const rect = this.$refs.topBox2.getBoundingClientRect();
            const newHeight = event.clientY - rect.top;
            this.$refs.topBox2.style.height = `${newHeight}px`;
            this.$refs.bottomBox2.style.height = `${this.$refs.cont2.clientHeight - newHeight}px`;
        }
    },
    stopResize() {
      document.removeEventListener('mousemove', this.performResize);
      document.removeEventListener('mouseup', this.stopResize);
    }
  }
}
</script>
