<script setup>
import Chat from '../components/Chat.vue';
import Navbar from '../components/Navbar.vue'
import CodeBlocks from '../components/CodeBlocks.vue'
import 'bootstrap-icons/font/bootstrap-icons.css';
import SimulationView from '../components/SimulationView.vue';
</script>

<template>
  <main>
    <Navbar />
    <div class="d-flex" style="height:90%;">
        <div id="maze-div" class="w-50" style="height: 100%; border-right: 2px solid black;">
            <div class="h-100" style="display: flex; flex-direction: column;" ref="cont1">
                <div class="box p-3" ref="topBox1" style="height: 30%; overflow: auto;" id="topBox1">
                    <h3>
                        Problem broj {{ +$route.params.id + 1}}
                    </h3>
                    <p>
                        {{ task.description }}
                    </p>

                    <!-- Navigation Arrows -->
                    <div class="navigation-arrows-container d-flex justify-content-end">
                        <button  @click="listTask(-1)" :disabled="currentTaskIndex === 0" class="btn btn-light">
                            <i class="bi bi-arrow-left-circle-fill fs-3" style="color: green;"></i>
                        </button>
                        <button @click="listTask(1)" :disabled="currentTaskIndex === tasks.length - 1" class="btn btn-light">
                            <i class="bi bi-arrow-right-circle-fill fs-3" style="color: green;"></i>
                        </button>
                    </div>

                </div>
                <div class="resizer" @mousedown="startResize" id="resizer-left"></div>
                <div class="box p-3 d-flex w-100" style="height: 69%; justify-content: center;" ref="bottomBox1" id="bottomBox1">
                    <!-- <img src="https://as2.ftcdn.net/jpg/01/36/00/76/1000_F_136007620_CnJyQqcd3giJLsJGsHsLEXl5E9oA56X7.jpg" style="max-height: 100%; max-width: 100%;" class="mx-0" /> -->
                    <SimulationView></SimulationView>
                </div>
            </div>
        </div>
        <div id="code-div" class="w-50" style="height: 100%;">
            <div class="h-100" style="display: flex; flex-direction: column;" ref="cont2">
                <div class="box p-1" ref="topBox2" id="topBox2">
                    <Chat @newMessage="onMessageSent"/>
                </div>
                <div style="display: flex; flex: 1;">
                    <div class="box p-2" style="flex: 1;" ref="bottomLeftBox2" id="bottomLeftBox2">
                        <h5>Rezultujući kod</h5>
                        <pre v-highlightjs>
                            <code class="javascript"> {{ code }}
                            </code>
                        </pre>
                    </div>

                <div class="box p-2" style="flex: 1;" ref="bottomRightBox2" id="bottomRightBox2">
                    <h5>Rezultujući graf</h5>
                    <CodeBlocks ref="codeBlocks"></CodeBlocks>
                </div>
            </div>

              <!-- Resizer -->
              <div class="resizer" @mousedown="startResize" id="resizer-right"></div>
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
  flex: 0 0 35%; /* flex-grow, flex-shrink, flex-basis */
}

#code-div {
  flex: 0 0 65%; /* flex-grow, flex-shrink, flex-basis */
}

#bottomRightBox2 {
  overflow: auto;
}

#topBox2 {
    height: 45%;
    min-height: 45%;
}


</style>

<script>
export default {
    data() {
        return {
            tasks: [
                {
                    id: 0,
                    description: `Potrebno je da se krećete napred do desnog kraja lavirinta, zatim da promenite boju sijalice 
                    u vašu omiljenu, a zatim se vratite na početnu poziciju `,
                    imageUrl: "https://as2.ftcdn.net/jpg/01/36/00/76/1000_F_136007620_CnJyQqcd3giJLsJGsHsLEXl5E9oA56X7.jpg",
                },
                {
                    id: 1,
                    description: `Kreirati promenljivu 'brzina' i dodeliti joj vrednost 20. Zatim se kretati 3 sekunde pravo tom brzinom`,
                    imageUrl: "https://as2.ftcdn.net/jpg/01/36/00/76/1000_F_136007620_CnJyQqcd3giJLsJGsHsLEXl5E9oA56X7.jpg",
                },
                {
                    id: 2,
                    description: `Majka vodi sina Peru i ćerku Milicu u prodavnicu igračaka.
                    Deo prodavnice u koji idu odrediće igra kamen-papir-makaze. Ako Milica pobedi, majka će ih odvesti do dela
                    sa lutkicama, a ako Pera pobedi, odvešće ih u deo sa sportskim igračkama.
                    Napisati program koji će pokriti oba slučaja, s tim da će pobednik biti određen nasumično.
                    `,
                    imageUrl: "https://as2.ftcdn.net/jpg/01/36/00/76/1000_F_136007620_CnJyQqcd3giJLsJGsHsLEXl5E9oA56X7.jpg",
                },
                {
                    id: 3,
                    description: `Postavite robotića na početnu zelenu tačku. U ovom zadatku
                    potrebno je kretati se sivom putanjom a potom 4 puta obići kvadrat
                    oko narandžaste tačkice. Koristite loop blok! Nakon toga nastaviti
                    kretanje do crvene tačkice`,
                    imageUrl: "https://as2.ftcdn.net/jpg/01/36/00/76/1000_F_136007620_CnJyQqcd3giJLsJGsHsLEXl5E9oA56X7.jpg",
                },
                {
                    id: 4,
                    description: `Neki dodatni`,
                    imageUrl: "https://as2.ftcdn.net/jpg/01/36/00/76/1000_F_136007620_CnJyQqcd3giJLsJGsHsLEXl5E9oA56X7.jpg",
                },
            ],
            currentTaskIndex: 0,
            code: ''
        };
    },

    mounted()
    {
    },

    methods: {
        startResize(element) {
            // remove css align items stretch
            document.addEventListener("mousemove", this.performResize);
            document.addEventListener("mouseup", this.stopResize);
        },
        performResize(event) {
            console.log(event);
            let id = event.target.id;
            event.stopPropagation();
            if (id == "resizer-left" || id == "bottomBox1" || id == "topBox1") {
                const rect = this.$refs.topBox1.getBoundingClientRect();
                const newHeight = event.clientY - rect.top;
                this.$refs.topBox1.style.height = `${newHeight}px`;
                this.$refs.bottomBox1.style.height = `${this.$refs.cont1.clientHeight - newHeight}px`;
            }
            else if (id == "resizer-right" || id == "bottomBox2" || id == "topBox2") {
                const rect = this.$refs.topBox2.getBoundingClientRect();
                const newHeight = event.clientY - rect.top;
                this.$refs.topBox2.style.height = `${newHeight}px`;
                this.$refs.bottomBox2.style.height = `${this.$refs.cont2.clientHeight - newHeight}px`;
            }
        },
        stopResize() {
            document.removeEventListener("mousemove", this.performResize);
            document.removeEventListener("mouseup", this.stopResize);
        },

        onMessageSent(value) {
            this.code = value[0];
            //   TODO ovdje sada pozvati iscrtavanje oblika
            let stringList = value[1].slice(0, -1);
            const jsonString = '[' + stringList.replace(/'/g, '"') + ']';
            const listOfLists = JSON.parse(jsonString);

            this.$refs.codeBlocks.drawCustomShape(listOfLists);
        },
        listTask(direction) {
            this.currentTaskIndex += direction;
            this.$router.push('/problem/' + this.currentTaskIndex);
            
        }
    },
    computed: {
        task() {
            this.currentTaskIndex = +this.$route.params.id;
            return this.tasks[this.currentTaskIndex] || {};
        }
    },
    //components: { CodeBlocks }
}
</script>
