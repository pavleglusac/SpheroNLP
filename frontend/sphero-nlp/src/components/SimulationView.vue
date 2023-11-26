<template>
    <div class="content" style="height: 70%;">
      <div id="drawhere" style="max-width: 100%; max-height: 100%;"></div>
    </div>
</template>
  
<script>
import Matter from "matter-js";
import { executeCode } from './block_code_executor.js';



export default {

    mounted() {
        // module aliases
        var Engine = Matter.Engine,
            Render = Matter.Render,
            Runner = Matter.Runner,
            Bodies = Matter.Bodies,
            Composite = Matter.Composite;
        const Mouse = Matter.Mouse;
        const MouseConstraint = Matter.MouseConstraint;
        const World = Matter.World;
        const Body = Matter.Body;
        const Events = Matter.Events;
        // create an engine
        var engine = Engine.create();

        // set gravity to zero
        engine.world.gravity.y = 0;

        // create a renderer
        var render = Render.create({
            element: document.getElementById('drawhere'),
            engine: engine,
            options: {
                width: 900,
                height: 680,
                background: 'white',
                wireframes: false
            }
        });

        // create two boxes and a ground
        var robot = Bodies.circle(45, 45, 30);

        // set weight to 1
        robot.mass = 1;

        var grounds = [];

        var ground_params = [
            [0, 100, 500, 20],
            [400, 0, 20, 440],
            [260, 220, 300, 20],
            [0, 350, 500, 20],
            [650, 350, 500, 20],
            [150, 580, 900, 20],
            [380, 520, 20, 100],
            [265, 470, 250, 20],

            //square
            [680, 80, 150, 20],
            [680, 220, 150, 20],
            [615, 150, 20, 150],
            [745, 150, 20, 150],

            [510, 400, 20, 120],
            [800, 480, 220, 20],

            // sorrounding
            [450, 0, 900, 20],
            [450, 680, 900, 20],
            [0, 340, 20, 680],
            [900, 340, 20, 680],


        ];

        for (var i = 0; i < ground_params.length; i++) {
            var ground = Bodies.rectangle(...ground_params[i], { isStatic: true });
            ground.friction = 0;
            grounds.push(ground);
        }

        const goal = Bodies.rectangle(660, 240, 50, 50, {
            render: {
                sprite: {
                texture: 'https://pngimg.com/d/coin_PNG36871.png',
                xScale: 0.15,
                yScale: 0.15
                }
            }
        });

        function forwardDirection(body) {
            return {
                x: Math.cos(body.angle),
                y: Math.sin(body.angle)
            };
        }

        function desiredVelocity(body, speed) {
            return {
                x: Math.cos(body.angle) * speed,
                y: Math.sin(body.angle) * speed
            };
        }

        // set boxA to be yellow
        robot.render.fillStyle = '#0093D0';

        // make boxes draggable on mouse
        robot.plugin.draggable = true;
        var isSpinning = false;

        Events.on(engine, 'afterUpdate', function() {
            if (isSpinning) {
                console.log("Spinning");
                Body.setAngularVelocity(robot, 0.05);
                // Body.setVelocity(robot, { x: 0, y: 0 });
            } else {
                // Body.setVelocity(robot, { x: 0, y: 0 });
                Body.setAngularVelocity(robot, 0);
            }
        });

        // Toggle spinning with the Enter key
        document.addEventListener('keydown', function(event) {
            if (event.key === 'Enter') {
                isSpinning = !isSpinning;
            }
            if (event.key === 'ArrowUp') {
                const speed = 2; // adjust this value for desired speed
                const velocity = desiredVelocity(robot, speed);
                Body.setVelocity(robot, velocity);
            }
        });

        document.addEventListener('keyup', function(event) {
            if (event.key === 'ArrowUp') {
                Body.setVelocity(robot, { x: 0, y: 0 });
            }
        });




        const mouse = Mouse.create(render.canvas);
        const mouseConstraint = MouseConstraint.create(engine, {
            mouse: mouse
        });

        World.add(engine.world, mouseConstraint);



        // add all of the bodies to the world
        Composite.add(engine.world, [robot, ...grounds]);

        
        Matter.Events.on(render, 'afterRender', function() {
        const context = render.context;

        engine.world.bodies.forEach(body => {
                const x = body.position.x;
                const y = body.position.y;

                let endPointX, endPointY;

                if (body.circleRadius) {
                    // If the body is a circle
                    endPointX = x + body.circleRadius * Math.cos(body.angle);
                    endPointY = y + body.circleRadius * Math.sin(body.angle);
                    context.beginPath();
                    context.moveTo(x, y);
                    context.lineTo(endPointX, endPointY);
                    context.strokeStyle = 'red';
                    context.lineWidth = 2;
                    context.stroke();
                }

            });
        });

        this.$eventBus.on('code', async (code) => {
            console.log(code);
            await executeCode(code, this);
        })

        this.$eventBus.on('roll', (params) => {
            console.log(params);
            let degrees = params['degrees'];
            let speed = params['speed'];
            let seconds = params['seconds'];
            console.log(degrees, speed, seconds);

            speed = 4 * (speed / 255);
            
            degrees = degrees * Math.PI / 180;

            const velocity = {
                x: Math.cos(robot.angle + degrees) * speed,
                y: Math.sin(robot.angle + degrees) * speed
            };
            console.log(velocity);
            Body.setVelocity(robot, velocity);
            setTimeout(() => {
                Body.setVelocity(robot, { x: 0, y: 0 });
            }, seconds * 1000);

        });

        
        this.$eventBus.on('led', (params) => {
            let r = params['r'];
            let g = params['g'];
            let b = params['b'];
            console.log(r, g, b);
            robot.render.fillStyle = `rgb(${r}, ${g}, ${b})`;
        });


        Render.run(render);

        // set friction to zero
        robot.frictionAir = 0;
        robot.friction = 1;

        
        var runner = Runner.create();

        Runner.run(runner, engine);
    },
}
    
  
</script>
  
  
<style scoped>
</style>
  