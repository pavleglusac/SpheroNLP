

<template>
  <div>
    <canvas ref="customCanvas"></canvas>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  mounted() {
    this.drawCustomShape();

  },
  methods: {
    drawCustomShape() {

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

      let firstX = 50;
      let firstY = 50;

      // osnovno
      /*let p1 = new Params(firstX, firstY, 130);
      let p2 = new Params(firstX, firstY + 1 * height, 200);
      let p3 = new Params(firstX, firstY + 2 * height, 150);
      let p4 = new Params(firstX, firstY + 3 * height, 170, ['MWin', "===", 1])*/
      let p5 = new Params(firstX + 500, firstY + 4 * height, 150, '', 2);

      /*let o1 = new StartComponent(p1);
      o1.drawBody();
      o1.writeContent();
      let o2 = new TextComponent(p2);
      o2.drawBody();
      o2.writeContent();
      let o3 = new TextComponent(p3);
      o3.drawBody();
      o3.writeContent();
      let o4 = new CompareComponent(p4);
      o4.drawBody();
      o4.writeContent();
      let o5 = new IfElseComponent(p5);
      o5.drawBody();
      o5.writeContent();

*/
      // Pavlov primjer
     /* let secondX = 500;
      let secondY = 100;
      let pStart = new Params(secondX, secondY, 130);
      let oStart = new StartComponent(pStart);
      oStart.drawBody();
      oStart.writeContent();

      let pLoop = new Params(secondX, secondY + 1 * height, 150, '', 2);
      let oLoop = new LoopUntilTrue(pLoop);
      oLoop.drawBody();
      oLoop.writeContent();

      let pRoll = new Params(secondX + 3 * resa, secondY + 2 * height, 320, [0, 24, 1])
      let oRoll = new RollComponent(pRoll);
      oRoll.drawBody();
      oRoll.writeContent();

      let pDelay = new Params(secondX + 3 * resa, secondY + 3 * height, 120, [5]);
      let oDelay = new DelayComponent(pDelay);
      oDelay.drawBody();
      oDelay.writeContent();

      let pLed = new Params(secondX, secondY + 5 * height, 130, [55, 100, 30]);
      let oLed = new LedComponent(pLed);
      oLed.drawBody();
      oLed.writeContent();

      let pEnd = new Params(secondX, secondY +  6 * height, 130);
      let oEnd = new EndComponent(pEnd);
      oEnd.drawBody();
      oEnd.writeContent();

      let pExp = new Params(secondX, secondY +  7 * height, 330, ['int', 0, 2]);
      let oExp = new RandomExpression(pExp);
      oExp.drawBody();
      oExp.writeContent();

      let pSet = new Params(secondX, secondY +  8 * height, 230, ['brzina', 20]);
      let oSet = new SetComponent(pSet);
      oSet.drawBody();
      oSet.writeContent();

      let pSound = new Params(secondX, secondY +  9 * height, 330, ['win classic', 'wait']);
      let oSound = new SoundComponent(pSound);
      oSound.drawBody();
      oSound.writeContent();
      */
    /*
      //treca skupina
      let thirdX = 1000;
      let thirdY = 50;

      let pStart3 = new Params(thirdX, thirdY + 0 * height, 130);
      let oStart3 = new StartComponent(pStart3);
      oStart3.drawBody();
      oStart3.writeContent();

      let pLoopForever = new Params(thirdX, thirdY + 1 * height, 150, "", 7);
      let oLoopForever = new LoopForever(pLoopForever);
      oLoopForever.drawBody();
      oLoopForever.writeContent();

      let pHeader = new Params(thirdX + 3 * resa, thirdY + 2 * height, 120, [0]);
      let oHeader = new HeaderComponent(pHeader);
      oHeader.drawBody();
      oHeader.writeContent();

      let pLoopTimes = new Params(thirdX + 3 * resa, thirdY + 3 * height, 150, [5], 4);
      let oLoopTimes = new LoopTimes(pLoopTimes);
      oLoopTimes.drawBody();
      oLoopTimes.writeContent();

      let pAim = new Params(thirdX + 6 * resa, thirdY + 4 * height, 70, 'reset aim');
      let oAim = new TextComponent(pAim);
      oAim.drawBody();
      oAim.writeContent();

      let pIf = new Params(thirdX + 6 * resa, thirdY + 5 * height, 150, ['true'], 1);
      let oIf = new IfComponent(pIf);
      oIf.drawBody();
      oIf.writeContent();

      let pRoll32 = new Params(thirdX + 9 * resa, thirdY + 6 * height, 320, [ 0, 0, '0']);
      let oRoll32 = new RollComponent(pRoll32);
      oRoll32.drawBody();
      oRoll32.writeContent();*/


      class BiloSta {

        translate(y, position, offset) {
          for (let i = position; i<y.length; i++)
          {
            y[i] += offset
          }
          return y;
        }


        getOffsets(data) {
          let y = [];
          for (let j = 0; j <= data.length; j++) {
              y.push(j);
          }    

          for (let i = 0; i < data.length; i++) {

            if (data[i][0].includes("loop")) {
              let scope = data[i][data[i].length - 1]; 
              y = this.translate(y, i + 1 + scope, 1);
            }
/*            else if (data[i][0].includes("compare") || data[i][0].includes("random")) {
              y = this.translate(y, i, -1);
            }*/
            else if (data[i][0].includes("if"))
            {
              let scope = data[i][data[i].length - 1]; 
              y = this.translate(y, i + 1 + scope, 1);

              if (data[i][0]===("if-else")) {
              let scope1 = data[i][data[i].length - 1]; 
              let scope2 = data[i][data[i].length - 2]; 
              y = this.translate(y, i + 2 + scope1 + scope2, 1); 
              }
            }
           
          console.log(y); 
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

        getOffsets2(data) {
          let y = [];
          for (let j = 0; j <= data.length; j++) {
              y.push(j);
          }    
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

      
      

///////////////////////////////// sad krece pravo
      let startX = 10;
      let startY = 25;
      /*let data = [
      ['led', 1, 255, 255, 255],
      ['loopTimes', 1, 5, 6],
      ['declare', 2, 'B', 5],
      ['if-else', 2, ['compare', 2, 'B', '>', 10], 1, 1],
      
      ['roll', 3, 90, 50, 5],
      ['roll', 3, 10, 50, 5],
      ['roll', 1, 10, 50, 5]
    ];*/

    /*let data = [
      ['led', 1, 255, 255, 255],
      ['loopTimes', 1, 5, 4],
      ['declare', 2, 'B', ['random', 2, 0, 2]],
      ['if', 2, ['compare', 3, 'B', '>', 10], 1],
      ['roll', 3, 90, 50, 5]
    ]*/

    /*let data = [
    ['declare', 1,'B', ['random', 1, 0, 2]],
    ['if', 1, ['compare', 2, 'B', '>', 10],4],
    ['roll', 2, 90, 50, 5],
    ['loopTimes', 2, 5, 1],
    ['led', 3, 255, 255, 255]
    ]*/

    /*let data = [
      ['start', 1],
      ['declare', 1, 'B', ['random', 1, 0, 2]],
      ['if', 1, ['compare', 2, 'B', '>', 10], 6],
      ['roll', 2, 90, 50, 5],
      ['loopTimes', 2, 5, 3],
      ['if', 3, ['compare', 4, 'B', '<', 15],1],
      ['assign', 4, 'B', 10],
      ['roll', 1, 90, 50, 5],
      ['end', 1]
      
    ]*/

    let data = [
    ['declare', 1, 'B', ['random', 1, 0, 2]],
    ['if', 1, ['compare', 2, 'B', '>', 10], 6],
    ['roll', 2, 90, 50, 5],
    ['loopTimes', 2, 5, 3],
    ['if', 3, ['compare', 4, 'B', '<', 15], 1],
    ['assign', 4, 'B', ['random', 4, 0, 2]],
    ['roll', 1, 90, 50, 5]

    ]
    data.unshift(['start', 1]);
    data.push(['end', 1]);
    console.log(data);


    let bs = new BiloSta();
    let yOff = bs.getOffsets2(data);


      /*let s = new Params(startX, startY, 120);
      let a = new StartComponent(s);
      a.drawBody();
      a.writeContent();*/

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
        if (c instanceof SetComponent) {
          if (data[i][3].length > 3)
          {
            c.p.width = 470;
          }
        }
        c.drawBody();
        c.writeContent();
       }

    
    },
  },
};
</script>