<template>
    <div class="content" style="height: 50%;">
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
                height: 540,
                background: 'white',
                wireframes: false
            }
        });

        // create two boxes and a ground
        var robot = Bodies.circle(60, 60, 40);

        // set weight to 1
        robot.mass = 1;

        var groundA = Bodies.rectangle(0, 150, 600, 30, { isStatic: true });
        console.log(groundA.friction);
        groundA.friction = 0;
        var groundB = Bodies.rectangle(450, 0, 30, 570, { isStatic: true });
        groundB.friction = 0;
        var groundC = Bodies.rectangle(450, 300, 630, 30, { isStatic: true });
        groundC.friction = 0;
        var groundD = Bodies.rectangle(750, 230, 30, 150, { isStatic: true });
        groundD.friction = 0;
        var groundE = Bodies.rectangle(680, 170, 150, 30, { isStatic: true });
        groundE.friction = 0;
        var groundF = Bodies.rectangle(450, 500, 30, 150, { isStatic: true });
        groundF.friction = 0;

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
        Composite.add(engine.world, [robot, groundA, groundB, groundC, groundD, groundE, groundF, goal]);

        
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
  