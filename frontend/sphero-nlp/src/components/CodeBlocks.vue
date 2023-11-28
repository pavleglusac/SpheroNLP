

<template>
    <div>
      <canvas ref="customCanvas"></canvas>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  export default {
    mounted() {
      
  
    },
    methods: {
      drawCustomShape(data) {
  
        const canvas = this.$refs.customCanvas;
        const ctx = canvas.getContext('2d');
        const resa = 7
        const radius = 5
        const height = 45;
        const blue = {insideColor: "#14A4BE", outlineColor: "#25C7DC"}
        const violet = {insideColor: "#463199", outlineColor: "#5F61B3"}
        const violetInverse = {insideColor: "#5F61B3", outlineColor: "#463199"}
        const black = {insideColor: "#050505", outlineColor: "#293337"}
        const green = {insideColor: '#32F9FF',  outlineColor:'#43BEAC'}
        const darkBlue = {insideColor: '#0C5EA8',  outlineColor:'#0085C6'}
        const pink = {insideColor: '#AA325F',  outlineColor:'#D54077'}
        const darkPink = {insideColor: '#5C2042',  outlineColor:'#95376C'}
        
        
        class Params {
        constructor(xStart, yStart, width, content, linesNum = -1) {
            this.ctx = ctx;
            this.x = xStart;
            this.y = yStart;
            this.width = width;
            this.height = height;
            this.radius = radius;
            this.resa = resa;
            this.content = content;
            this.linesNum = linesNum;
        }
      } 
  
      class CodeBlock {
          constructor(params) {
            this.p = params;
            this.lastX = 0;
          }

          drawBody(){
           
          }

          writeContent(){
           
          }

          calculateWidth() {
            let a = 0;
            for (let i = 1; i < this.p.content; i++) {
              a += ctx.measureText(this.p.content[i]).width;
            }
            return a + this.getFixedContent();
          }

          finish(){
            this.p.ctx.closePath();
            this.p.ctx.stroke();
            this.p.ctx.fill();
          }

          drawVerticalLineWithArches(n)
          {
            let offset = (n + 1) * this.p.height;
            this.p.ctx.arcTo(this.p.x - this.p.resa * 3, this.p.y + this.p.height, this.p.x - this.p.resa * 3, this.p.y + this.p.height - this.p.radius, this.p.radius);
            this.p.ctx.lineTo(this.p.x  - this.p.resa * 3, this.p.y + this.p.radius - offset);  
            this.p.ctx.arcTo(this.p.x - this.p.resa * 3, this.p.y - offset, this.p.x - this.p.resa * 3 + this.p.radius, this.p.y - offset, this.p.radius);
          }

          prepare()
          {
            this.p.ctx.strokeStyle = this.p.color.insideColor;
            this.p.ctx.fillStyle = this.p.color.outlineColor;
            this.p.ctx.lineWidth = this.p.lineWidth;
            this.p.ctx.beginPath();
          }

          drawVerticalLine()
          {
            this.p.ctx.lineTo(this.p.x, this.p.y);
          }

          drawBottomLine()
          {
            this.p.ctx.lineTo(this.p.x  + 10 * this.p.resa, this.p.y + this.p.height);
            this.p.ctx.lineTo(this.p.x + 9 * this.p.resa, this.p.y + this.p.height + this.p.resa);
            this.p.ctx.lineTo(this.p.x + 7 * this.p.resa, this.p.y + this.p.height + this.p.resa);
            this.p.ctx.lineTo(this.p.x + 6 * this.p.resa, this.p.y + this.p.height);
            this.p.ctx.lineTo(this.p.x + 3 * this.p.resa, this.p.y + this.p.height);
          }

          drawSemicircle()
          {
            this.p.ctx.arc(this.p.x + this.p.width,  this.p.y + (this.p.height/2), this.p.height/2, -Math.PI / 2, Math.PI / 2, false); // Arc for a semicircle;
          }

          drawUpperLine()
          {
            this.p.ctx.lineTo(this.p.x + 3 * this.p.resa, this.p.y);
            this.p.ctx.lineTo(this.p.x + 4 * this.p.resa, this.p.y + this.p.resa);
            this.p.ctx.lineTo(this.p.x + 6 * this.p.resa, this.p.y + this.p.resa);
            this.p.ctx.lineTo(this.p.x + 7 * this.p.resa, this.p.y);
          }
          

          drawInsideHexagon(ctx, insideColor, x, y, height, keyword) {
            ctx.font = '17px Arial';
            const textWidth = ctx.measureText(keyword).width;
            //let width = height * 0.45; // Set a default width based on the original ratio
            let width = textWidth - this.p.resa/2; // Ensure the width is at least the text width + a margin

            y = y + height / 7;
            height = height * 0.45;

            ctx.beginPath();
            ctx.moveTo(x, y);
            ctx.lineTo(x + width, y);
            ctx.lineTo(x + width * 1.6, y + height * 0.75);
            ctx.lineTo(x + width, y + height * 1.5);
            ctx.lineTo(x, y + height * 1.5);
            ctx.lineTo(x - width * 0.6, y + height * 0.75);
            ctx.lineTo(x, y);
            ctx.closePath();
            ctx.fillStyle = insideColor;
            ctx.fill();

            ctx.fillStyle = 'white';
            const textX = x - this.p.resa / 4;
            const textY = y + height;
            ctx.fillText(keyword, textX, textY);
        }



        drawInsideRec(ctx, insideColor, x, y, height, keyword, ratio = 0.7) {
          ctx.font = '17px Arial';
          const textWidth = ctx.measureText(keyword).width;
          let width = textWidth + this.p.resa * 4;

          y = y + height / 7;
          height = height * ratio;

          let radius = height / 2;

          ctx.beginPath();
          ctx.moveTo(x + radius, y);
          ctx.lineTo(x + width - radius, y);
          ctx.arcTo(x + width, y, x + width, y + radius, radius);
          ctx.lineTo(x + width, y + height - radius);
          ctx.arcTo(x + width, y + height, x + width - radius, y + height, radius);
          ctx.lineTo(x + radius, y + height);
          ctx.arcTo(x, y + height, x, y + height - radius, radius);
          ctx.lineTo(x, y + radius);
          ctx.arcTo(x, y, x + radius, y, radius);
          ctx.closePath();

          ctx.fillStyle = insideColor;
          ctx.fill();
          ctx.fillStyle = 'white';
          const textX = x + this.p.resa*2;
          const textY = y + height / 1.47;
          ctx.fillText(keyword, textX, textY);
          this.lastX = textX + width; 
      }


        drawInsideOctagon(ctx, insideColor, x, y, height) {
          ctx.beginPath();
          y = y + height / 7;
          height = height * 0.4
          let width = height;
          ctx.moveTo(x, y);
          ctx.lineTo(x + width, y);
          ctx.lineTo(x + width * 1.6, y + height * 0.6);
          ctx.lineTo(x + width * 1.6, y + height * 1.2);
          ctx.lineTo(x + width, y + height * 1.8);
          ctx.lineTo(x, y + height * 1.8);
          ctx.lineTo(x - width * 0.6, y + height * 1.2);
          ctx.lineTo(x - width * 0.6, y + height * 0.6);
          ctx.lineTo(x, y);
          ctx.closePath();
          ctx.fillStyle = insideColor;  
          ctx.fill();
        }


      drawInsideSquare(ctx, insideColor, x, y, height, keyword, ratio = 0.4) {
        ctx.font = '17px Arial';
        const textWidth = ctx.measureText(keyword).width;
        let width = textWidth + this.p.resa * 2;

        y = y + height / 7;
        height = height * ratio;

        ctx.beginPath();
        ctx.moveTo(x, y);
        ctx.lineTo(x + width, y);
        ctx.lineTo(x + width, y + height * 1.8);
        ctx.lineTo(x, y + height * 1.8);
        ctx.lineTo(x, y);
        ctx.closePath();
        ctx.fillStyle = insideColor;
        ctx.fill();
        ctx.fillStyle = 'white';
        const textX = x + this.p.resa;
        const textY = y + height / 0.85;
        ctx.fillText(keyword, textX, textY);
        this.lastX = textX + width; 

       }
      }



      class ComplexComponent extends CodeBlock {
        drawBody()
        {
          this.prepare();
          ctx.moveTo(this.p.x + this.p.radius, this.p.y);
          this.drawUpperLine();
          this.drawSemicircle();
          this.drawBottomLine();
          
          let offset = (this.p.linesNum + 1) * this.p.height
          this.p.x = this.p.x + this.p.resa * 3 ;
          this.p.y = this.p.y + offset;
          this.drawVerticalLine(); 
          this.drawUpperLine();     
          this.drawSemicircle();  
          this.drawMovedBottomLine();
          this.drawVerticalLineWithArches(this.p.linesNum);
          this.finish();
        }


        drawMovedBottomLine()
          {
            this.p.ctx.lineTo(this.p.x  + 4 * this.p.resa, this.p.y + this.p.height);
            this.p.ctx.lineTo(this.p.x + 3 * this.p.resa, this.p.y + this.p.height + this.p.resa);
            this.p.ctx.lineTo(this.p.x + 1 * this.p.resa, this.p.y + this.p.height + this.p.resa);
            this.p.ctx.lineTo(this.p.x + 0 * this.p.resa, this.p.y + this.p.height);
            this.p.ctx.lineTo(this.p.x + 0 * this.p.resa, this.p.y + this.p.height);
          }
      }

      class SimpleComponent extends CodeBlock {
        drawBody()
        {
          this.prepare();
          ctx.moveTo(this.p.x + this.p.radius, this.p.y);                                // ovo je prva tacka, nakon luka
          this.drawUpperLine();
          this.drawSemicircle();
          this.p.x -= this.p.resa * 3;
          this.drawBottomLine();
          this.p.x += this.p.resa * 6;
          this.drawVerticalLineWithArches(this.p.linesNum);
          this.finish();
        }

      }


      class CompareComponent extends CodeBlock {
        drawBody () {
          this.p.color = violetInverse;
          // compare treba da bude malo uvucen u odnosu na ostale komponente
          this.p.x += resa * 4;

          this.prepare();
          ctx.beginPath();
          this.p.y = this.p.y + this.p.height / 7;
          this.p.height = this.p.height * 0.45
          ctx.moveTo(this.p.x, this.p.y);
          ctx.lineTo(this.p.x + this.p.width, this.p.y);
          ctx.lineTo(this.p.x + this.p.width + this.p.height * 0.75, this.p.y + this.p.height * 0.75);
          ctx.lineTo(this.p.x + this.p.width, this.p.y + this.p.height * 1.5);
          ctx.lineTo(this.p.x, this.p.y + this.p.height * 1.5);
          ctx.lineTo(this.p.x - this.p.height * 0.75 , this.p.y + this.p.height * 0.75);
          ctx.lineTo(this.p.x, this.p.y);
          this.finish();
        }

        writeContent() {
          this.p.ctx.stroke();
          this.p.ctx.fill();

          this.p.ctx.fillStyle = 'white';
          this.p.ctx.font = '17px Arial';

          this.drawInsideRec(this.p.ctx, this.p.color.insideColor, this.p.x + this.p.resa * 1, this.p.y, this.p.height, this.p.content[0], 1.25);
          this.drawInsideSquare(this.p.ctx, this.p.color.insideColor, this.lastX + this.p.resa * 1, this.p.y, this.p.height, this.p.content[1], 0.65);
          this.drawInsideRec(this.p.ctx, this.p.color.insideColor, this.lastX + this.p.resa * 2, this.p.y, this.p.height, this.p.content[2], 1.25);
        
        }
      }

      class TextComponent extends SimpleComponent {

        constructor(params) {
          super(params);
          this.p.color = blue;
          }

        writeContent()
        {
          this.p.ctx.stroke();
          this.p.ctx.fill();
          this.p.ctx.fillStyle = 'white';
          this.p.ctx.font = '17px Arial';
          this.p.ctx.fillText(this.p.content, this.p.x - 2 * this.p.resa, this.p.y + this.p.height /1.6);
        }
      }

      class RollComponent extends SimpleComponent {
        constructor(params) {
          super(params);
          this.p.color = blue;
          }


        writeContent()
        {
          this.p.ctx.stroke();
          this.p.ctx.fill();

          this.p.ctx.fillStyle = 'white';
          this.p.ctx.font = '17px Arial';

          this.p.ctx.fillText("roll", this.p.x - this.p.resa, this.p.y + this.p.height /1.6);
          this.drawInsideRec(this.p.ctx, this.p.color.insideColor, this.p.x + this.p.resa * 4, this.p.y, this.p.height, this.p.content[1] + '°');

          this.p.ctx.fillText("at", this.lastX, this.p.y + this.p.height /1.6);
          this.drawInsideRec(this.p.ctx, this.p.color.insideColor, this.lastX + this.p.resa * 4, this.p.y, this.p.height, this.p.content[2]);

          this.p.ctx.fillText("speed for", this.lastX, this.p.y + this.p.height /1.6);
          this.drawInsideRec(this.p.ctx, this.p.color.insideColor, this.lastX + this.p.resa * 12, this.p.y, this.p.height, this.p.content[3] + 's' );
        }
      }

      class DelayComponent extends SimpleComponent {

        constructor(params) {
          super(params);
          this.p.color = blue;
          }


        writeContent()
        {
          this.p.ctx.stroke();
          this.p.ctx.fill();
          this.p.ctx.fillStyle = 'white';
          this.p.ctx.font = '17px Arial';
          this.p.ctx.fillText("delay for", this.p.x - this.p.resa, this.p.y + this.p.height /1.6);
          this.drawInsideRec(this.p.ctx, this.p.color.insideColor, this.p.x - 5 * this.p.resa + 100, this.p.y, this.p.height, this.p.content[1] + 's');
        }
      }

      class LedComponent extends SimpleComponent {

        constructor(params) {
          super(params);
          this.p.color = green;
          }

        writeContent()
        {
          this.p.ctx.fillStyle = 'white';
          this.p.ctx.font = '17px Arial';
          let c = "(" + this.p.content[1] + ", " + this.p.content[2] + ", " + this.p.content[3] + ")";
          this.p.ctx.fillText("main LED", this.p.x - this.p.resa * 2, this.p.y + this.p.height /1.6);
          this.drawInsideOctagon(this.p.ctx, c, this.p.x + 85, this.p.y, this.p.height);
        }
      }

      class SetComponent extends TextComponent {
        constructor(params) {
          super(params);
          this.p.color = pink;
          }

        writeContent()
        {
          this.p.ctx.stroke();
          this.p.ctx.fill();

          this.p.ctx.fillStyle = 'white';
          this.p.ctx.font = '17px Arial';

          this.p.ctx.fillText("set", this.p.x - this.p.resa, this.p.y + this.p.height /1.6);
          this.drawInsideSquare(this.p.ctx, this.p.color.insideColor, this.p.x + this.p.resa * 4, this.p.y, this.p.height, this.p.content[1]);

          this.p.ctx.fillText("to", this.lastX + this.p.resa * 1, this.p.y + this.p.height /1.6);
          //this.drawInsideRec(this.p.ctx, this.p.color.insideColor, this.lastX + this.p.resa * 5, this.p.y, this.p.height, this.p.content[2]);
          if (this.p.content[2].length > 1)
          {
            let newData = this.p.content[2];
            let p = new Params(this.p.x, this.p.y, 300, [newData[2], newData[3]]);
            let rand = new RandomExpression(p);
            rand.drawBody();
            rand.writeContent();
          }          
          else {
            this.drawInsideRec(this.p.ctx, this.p.color.insideColor, this.lastX + this.p.resa * 5, this.p.y, this.p.height, this.p.content[2]);
          }
        }
      }


      class SoundComponent extends TextComponent  {
        constructor(params) {
          super(params);
          this.p.color = darkPink;
          }

          writeContent()
        {
          this.p.ctx.stroke();
          this.p.ctx.fill();

          this.p.ctx.fillStyle = 'white';
          this.p.ctx.font = '17px Arial';

          this.p.ctx.fillText("play", this.p.x - this.p.resa, this.p.y + this.p.height /1.6);
          this.drawInsideSquare(this.p.ctx, this.p.color.insideColor, this.p.x + this.p.resa * 5, this.p.y, this.p.height, this.p.content[0]);

          this.p.ctx.fillText("sound and", this.p.x + this.p.resa * 20, this.p.y + this.p.height /1.6);
          this.drawInsideHexagon(this.p.ctx, this.p.color.insideColor, this.p.x + this.p.resa * 35, this.p.y, this.p.height, this.p.content[1]);

         }
      }

      class HeaderComponent extends SimpleComponent {

        constructor(params) {
          super(params);
          this.p.color = blue;
          }

        writeContent()
        {
          this.p.ctx.stroke();
          this.p.ctx.fill();
          this.p.ctx.fillStyle = 'white';
          this.p.ctx.font = '17px Arial';
          this.p.ctx.fillText("heading", this.p.x - this.p.resa, this.p.y + this.p.height /1.6);
          this.drawInsideRec(this.p.ctx, this.p.color.insideColor, this.p.x - 5 * this.p.resa + 100, this.p.y, this.p.height, this.p.content[1] + '°');
        }
      }

      class StartComponent extends TextComponent {
        constructor(params) {
          super(params);
          this.p.color = black;
          this.p.content = "on start program";
          }

        drawUpperLine()
        {
        }
      }

      class EndComponent extends TextComponent {
        constructor(params) {
          super(params);
          this.p.color = violet;
          this.p.content = "exit program";
        }

        drawBottomLine()
        {

        }
      }

      class RandomExpression extends TextComponent {
        constructor(params) {
          super(params);
          this.p.color = darkBlue;
          this.p.height *= 0.8;
          this.p.y += this.p.height / 10
          this.p.x += this.p.resa * 20;
        }
        drawUpperLine() {}
        drawBottomLine() {}
        drawVerticalLineWithArches() {
          this.p.ctx.arc(this.p.x - 2 * this.p.resa, this.p.y + (this.p.height/2), this.p.height/2, Math.PI / 2, 3 * Math.PI / 2, false);
        }

        writeContent()
        {
          this.p.ctx.stroke();
          this.p.ctx.fill();

          this.p.ctx.fillStyle = 'white';
          this.p.ctx.font = '17px Arial';

          this.p.ctx.fillText("random", this.p.x - this.p.resa * 2, this.p.y + this.p.height /1.6);
          this.drawInsideSquare(this.p.ctx, this.p.color.insideColor, this.p.x + this.p.resa * 7, this.p.y, this.p.height, "int");

          this.p.ctx.fillText("from", this.lastX + resa * 1, this.p.y + this.p.height /1.6);
          this.drawInsideRec(this.p.ctx, this.p.color.insideColor, this.lastX + this.p.resa * 7, this.p.y, this.p.height, this.p.content[0]);

          this.p.ctx.fillText("to", this.lastX + this.p.resa * 0, this.p.y + this.p.height /1.6);
          this.drawInsideRec(this.p.ctx, this.p.color.insideColor, this.lastX + this.p.resa * 4, this.p.y, this.p.height, this.p.content[1]);
        }
      }

      

      class LoopUntilTrue extends ComplexComponent
      {
        constructor(params) {
          super(params);
          this.p.color = violet;
          this.p.content = "loop until";
          }

        writeContent() {
          let offset = (this.p.linesNum + 1) * this.p.height;
          this.p.ctx.stroke();
          this.p.ctx.fill();
          this.p.ctx.fillStyle = 'white';
          this.p.ctx.font = '17px Arial';
          this.p.y = this.p.y - offset;
          this.p.ctx.fillText(this.p.content, this.p.x - this.p.resa * 2, this.p.y + this.p.height /1.6);
          this.drawInsideHexagon(this.p.ctx, this.p.color.insideColor, this.p.x - this.p.resa * 3 + 100, this.p.y, this.p.height, 'true');
          ctx.fillStyle = 'white';
          ctx.font = '30px Arial';
          ctx.fillText(String.fromCharCode(0x02923), this.p.x  + 130, this.p.y + this.p.height * (this.p.linesNum + 2) - 15 );
        }
      }

      class LoopTimes extends ComplexComponent {
        constructor(params) {
          super(params);
          this.p.color = violet;
          }

          writeContent() {
          let offset = (this.p.linesNum + 1) * this.p.height;
          this.p.ctx.stroke();
          this.p.ctx.fill();
          this.p.ctx.fillStyle = 'white';
          this.p.ctx.font = '17px Arial';
          this.p.y = this.p.y - offset;
          this.p.ctx.fillText("loop", this.p.x - this.p.resa * 2, this.p.y + this.p.height /1.6);
          this.drawInsideRec(this.p.ctx, this.p.color.insideColor, this.p.x + this.p.resa * 4, this.p.y, this.p.height, this.p.content[1]);
          this.p.ctx.fillText("times", this.p.x + this.p.resa * 12, this.p.y + this.p.height /1.6);
          ctx.fillStyle = 'white';
          ctx.font = '30px Arial';
          ctx.fillText(String.fromCharCode(0x02923), this.p.x  + 140, this.p.y + this.p.height * (this.p.linesNum + 2) - 15 );
        }
      }

      class LoopForever extends ComplexComponent
      {

        constructor(params) {
          super(params);
          this.p.color = violet;
          this.p.content = "loop forever";
          }

        writeContent() {
          let offset = (this.p.linesNum + 1) * this.p.height;
          this.p.ctx.fillStyle = 'white';
          this.p.ctx.font = '17px Arial';
          this.p.y = this.p.y - offset
          this.p.ctx.fillText(this.p.content, this.p.x - this.p.resa * 2, this.p.y + this.p.height /1.6);
          this.p.ctx.fillStyle = 'white';
          this.p.ctx.font = '30px Arial';
          this.p.ctx.fillText(String.fromCharCode(0x02923), this.p.x  + 140, this.p.y + this.p.height * (this.p.linesNum + 2) - 15 );
        }
      }

      class IfComponent extends ComplexComponent
      {
        constructor(params) {
          super(params);
          this.p.color = violet;
          }

        writeContent() {
          let offset = (this.p.linesNum + 1) * this.p.height;
          this.p.ctx.font = '17px Arial';
          this.p.y = this.p.y - offset
          this.p.ctx.fillStyle = 'white';
          this.p.ctx.fillText("if", this.p.x - this.p.resa * 2, this.p.y + this.p.height /1.6);
          //this.drawInsideHexagon(this.p.ctx, this.p.color.insideColor, this.p.x - this.p.resa * 3 + 50, this.p.y, this.p.height, 'true');
          this.p.ctx.fillText("then", this.p.x + 240, this.p.y + this.p.height /1.6);
          // ovdje treba staviti da se napravi compare

          // sad je vrijeme da se pravi compare komponenta
          if (this.p.content[1].length > 1)
          {
            let newData = this.p.content[1]; 
            let p = new Params(this.p.x, this.p.y, 180, [newData[2], newData[3], newData[4]]);
            let rand = new CompareComponent(p);
            rand.drawBody();
            rand.writeContent();
          }          
          /*else {
            this.drawInsideRec(this.p.ctx, this.p.color.insideColor, this.lastX + this.p.resa * 5, this.p.y, this.p.height, this.p.content[2]);
          }*/


        }
      }

      class IfElseComponent extends ComplexComponent
      {
        constructor(params) {
          super(params);
          this.p.color = violet;
          }

          drawBody()
        {
          this.prepare();
          ctx.moveTo(this.p.x + this.p.radius, this.p.y);
          this.drawUpperLine();
          this.drawSemicircle();
          this.drawBottomLine();
          
          let offset = (this.p.linesNum + 1) * this.p.height
          this.p.x = this.p.x + this.p.resa * 3 ;
          this.p.y = this.p.y + offset;
          this.drawVerticalLine(); 
          this.drawUpperLine();     
          this.drawSemicircle();
          this.p.x = this.p.x - this.p.resa * 3 ;
  
          this.drawBottomLine();
          offset = (this.p.linesNum + 1) * this.p.height  // ne treba *2 jer smo *1 vec sabrali
          this.p.x = this.p.x + this.p.resa * 3 ;
          this.p.y = this.p.y + offset;
          this.drawVerticalLine(); 
          this.drawUpperLine();     
          this.drawSemicircle();  

          this.drawMovedBottomLine();
          this.drawVerticalLineWithArches(this.p.linesNum * 2 + 1);
          this.finish();
        }

        writeContent() {
          let offset = (this.p.linesNum + 1 + this.p.linesNum + 1) * this.p.height;
          this.p.ctx.font = '17px Arial';
          this.p.y = this.p.y - offset
          this.p.ctx.fillStyle = 'white';
          this.p.ctx.fillText("if", this.p.x - this.p.resa * 2, this.p.y + this.p.height /1.6);
          this.drawInsideHexagon(this.p.ctx, this.p.color.insideColor, this.p.x - this.p.resa * 3 + 50, this.p.y, this.p.height, 'true');
          this.p.ctx.fillText("then", this.p.x + 240, this.p.y + this.p.height /1.6);
          this.p.ctx.fillText("else", this.p.x - this.p.resa * 2, this.p.y + this.p.height * (this.p.linesNum + 1) + this.p.height /1.6);

          if (this.p.content[1].length > 1)
          {
            let newData = this.p.content[1]; 
            let p = new Params(this.p.x, this.p.y, 180, [newData[2], newData[3], newData[4]]);
            let rand = new CompareComponent(p);
            rand.drawBody();
            rand.writeContent();
          }       
        }
      }
  
  
        canvas.width = 1500; 
        canvas.height = 1500; 


        let startX = 0;
        let startY = 25;
  
      class Offsets {

      translate(y, position, offset) {
        for (let i = position; i<y.length; i++)
        {
          y[i] += offset
        }
        return y;
      }

      addIfElse(data, y) {
        for (let i = 0; i< data.length; i++) {
          if (data[i][0]==="if-else")
          // treba lancano da pomjerim sve komponente koje idu nakon i+prva duzina
          {
            let len = data[i].length;
            let scope = data[i][len-2]; // ovo je predzadnji element
            y = this.translate(y, i + 1 + scope, 1);
          }
        }
        return y;
      }

      createinitialY(data) {
        let y = [];
        for (let j = 0; j <= data.length; j++) {
            y.push(j);
        }    
        return y;
      }

      getYOffsets(data) {
        let y = this.createinitialY(data);
        // svaki put kad vidim da se x vratilo za 1, moram da povecam y za 1
        for (let i = 1; i < data.length; i++) {
          let diff = data[i - 1][1] - data[i][1];
          if (diff > 0) {
            y = this.translate(y, i, diff)
          } 
        }
        y = this.addIfElse(data, y);
        return y;
      }
      }
  
      data.unshift(['start', 1]);
      data.push(['end', 1]);
      
      let bs = new Offsets();
      let yOff = bs.getYOffsets(data);

      let commandDict = {"roll": RollComponent, "led": LedComponent, "loopTimes": LoopTimes, "declare": SetComponent, "if": IfComponent, 
      "compare": CompareComponent, 'if-else': IfElseComponent, "random": RandomExpression, "assign": SetComponent, "start": StartComponent,
        "end": EndComponent}
      let commandWidth = {"roll": 330, "led": 150, "loopTimes": 170, "declare": 170, "if": 360, "compare": 180, 
      "if-else": 300, "random": 290, "assign": 170, "start": 120, "end":150}

        
      for (let i = 0; i < data.length; i++) {
        let commandName = data[i][0]; 
        let ps = data[i].slice(1);
        let p = new Params(data[i][1] * 3 * resa, yOff[i] * height, commandWidth[commandName], ps);
        let c = new commandDict[commandName](p);
        if (c instanceof ComplexComponent){
          p.linesNum = data[i][ps.length ];
        }
        if (c instanceof SetComponent && data[i][3].length > 3) c.p.width = 470;
        c.drawBody();
        c.writeContent();
       }
      },
    },
  };
  </script>