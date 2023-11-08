<template>
  <div>
    <canvas ref="customCanvas"></canvas>
  </div>
</template>

<script>
export default {
  mounted() {
    this.drawCustomShape();
  },
  methods: {
    drawCustomShape() {

      class Params {
        constructor(ctx, xStart, yStart, width, height, radius, resa, insideColor, outlineColor, content, linesNum = -1) {
            this.ctx = ctx;
            this.x = xStart;
            this.y = yStart;
            this.width = width;
            this.height = height;
            this.radius = radius;
            this.resa = resa;
            this.insideColor = insideColor;
            this.color = outlineColor;
            this.content = content;
            this.linesNum = linesNum;
        }
      } 

      class CodeBlock {
          constructor(params) {
            this.p = params;
          }

          drawBody(){
            console.log("iscrtaj se");
          }

          writeContent(){
            console.log("Pisanjee");
          }
          
          finish(){
            this.p.ctx.closePath();
            this.p.ctx.stroke();
            this.p.ctx.fill();
          }

          drawVerticalLineWithArches()
          {
            let offset = (this.p.linesNum + 1) * this.p.height;
            this.p.ctx.arcTo(this.p.x - this.p.resa * 3, this.p.y + this.p.height, this.p.x - this.p.resa * 3, this.p.y + this.p.height - this.p.radius, this.p.radius);
            this.p.ctx.lineTo(this.p.x  - this.p.resa * 3, this.p.y + this.p.radius - offset);  
            this.p.ctx.arcTo(this.p.x - this.p.resa * 3, this.p.y - offset, this.p.x - this.p.resa * 3 + this.p.radius, this.p.y - offset, this.p.radius);
          }

          prepare()
          {
            this.p.ctx.strokeStyle = this.p.insideColor;
            this.p.ctx.fillStyle = this.p.color;
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


          // TODO ovdje je ostalo zakucano par vrijednosti
          drawInsideHexagon(ctx, insideColor, x, y, height, keyword) {
            ctx.beginPath();
            y = y + height / 7;
            height = height * 0.45
            let width = height;
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
            ctx.font = '17px Arial';
            const textX = x - 3;
            const textY = y + height;
            ctx.fillText(keyword, textX, textY);
          }


          drawInsideRec(ctx, insideColor, x, y, height, keyword) {
            ctx.beginPath();   
            let width = 50;
            y = y + height / 7;
            height = height * 0.7
            let radius = height / 2;
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
            ctx.font = '17px Arial';
            const textX = x + 13;
            const textY = y + 24;
            ctx.fillText(keyword, textX, textY); 
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
          this.drawVerticalLineWithArches();
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
          this.drawVerticalLineWithArches();
          this.finish();
        }
      }

      class TextComponent extends SimpleComponent {
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
        writeContent()
        {
          this.p.ctx.stroke();
          this.p.ctx.fill();

          this.p.ctx.fillStyle = 'white';
          this.p.ctx.font = '17px Arial';

          this.p.ctx.fillText(this.p.content[0], this.p.x - this.p.resa, this.p.y + this.p.height /1.6);
          this.drawInsideRec(this.p.ctx, this.p.insideColor, this.p.x + this.p.resa * 4, this.p.y, this.p.height, this.p.content[1] + '°');

          this.p.ctx.fillText(this.p.content[2], this.p.x + this.p.resa * 13, this.p.y + this.p.height /1.6);
          this.drawInsideRec(this.p.ctx, this.p.insideColor, this.p.x + this.p.resa * 17, this.p.y, this.p.height, this.p.content[3]);

          this.p.ctx.fillText(this.p.content[4], this.p.x + this.p.resa + this.p.resa * 24, this.p.y + this.p.height /1.6);
          this.drawInsideRec(this.p.ctx, this.p.insideColor, this.p.x + this.p.resa * 36, this.p.y, this.p.height, this.p.content[5] + 's' );
        }
      }

      class DelayComponent extends SimpleComponent {
        writeContent()
        {
          this.p.ctx.stroke();
          this.p.ctx.fill();
          this.p.ctx.fillStyle = 'white';
          this.p.ctx.font = '17px Arial';
          this.p.ctx.fillText(this.p.content[0], this.p.x - this.p.resa, this.p.y + this.p.height /1.6);
          this.drawInsideRec(this.p.ctx, this.p.insideColor, this.p.x - 5 * this.p.resa + 100, this.p.y, this.p.height, this.p.content[1] + 's');
        }
      }

      class LedComponent extends SimpleComponent {
        writeContent()
        {
          this.p.ctx.fillStyle = 'white';
          this.p.ctx.font = '17px Arial';
          this.p.ctx.fillText(this.p.content[0], this.p.x - this.p.resa * 2, this.p.y + this.p.height /1.6);
          this.drawInsideOctagon(this.p.ctx, this.p.insideColor, this.p.x + 85, this.p.y, this.p.height);
        }
      }

      class HeaderComponent extends SimpleComponent {
        writeContent()
        {
          this.p.ctx.stroke();
          this.p.ctx.fill();
          this.p.ctx.fillStyle = 'white';
          this.p.ctx.font = '17px Arial';
          this.p.ctx.fillText(this.p.content[0], this.p.x - this.p.resa, this.p.y + this.p.height /1.6);
          this.drawInsideRec(this.p.ctx, this.p.insideColor, this.p.x - 5 * this.p.resa + 100, this.p.y, this.p.height, this.p.content[1] + '°');
        }
      }

      class StartComponent extends TextComponent {
        drawUpperLine()
        {
        }
      }

      class LoopUntilTrue extends ComplexComponent
      {
        writeContent() {
          let offset = (this.p.linesNum + 1) * this.p.height;
          this.p.ctx.stroke();
          this.p.ctx.fill();
          this.p.ctx.fillStyle = 'white';
          this.p.ctx.font = '17px Arial';
          this.p.y = this.p.y - offset;
          this.p.ctx.fillText(this.p.content, this.p.x - this.p.resa * 2, this.p.y + this.p.height /1.6);
          this.drawInsideHexagon(this.p.ctx, this.p.insideColor, this.p.x - this.p.resa * 3 + 100, this.p.y, this.p.height, 'true');
          ctx.fillStyle = 'white';
          ctx.font = '30px Arial';
          ctx.fillText(String.fromCharCode(0x02923), this.p.x  + 130, this.p.y + this.p.height * (this.p.linesNum + 2) - 15 );
        }
      }

      class LoopForever extends ComplexComponent
      {
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
        writeContent() {
          let offset = (this.p.linesNum + 1) * this.p.height;
          this.p.ctx.font = '17px Arial';
          this.p.y = this.p.y - offset
          this.p.ctx.fillStyle = 'white';
          this.p.ctx.fillText(this.p.content[0], this.p.x - this.p.resa * 2, this.p.y + this.p.height /1.6);
          this.drawInsideHexagon(this.p.ctx, this.p.insideColor, this.p.x - this.p.resa * 3 + 50, this.p.y, this.p.height, 'true');
          this.p.ctx.fillText(this.p.content[2], this.p.x + 72, this.p.y + this.p.height /1.6);
        }
      }


      const canvas = this.$refs.customCanvas;
      const ctx = canvas.getContext('2d');

      canvas.width = 1500; 
      canvas.height = 1500; 

      let resa = 7
      let radius = 5
      let firstX = 50;
      let firstY = 50;
      let yHeight = 50;


      // osnovno
      let p1 = new Params(ctx, firstX, firstY, 130, yHeight, radius, resa, '#050505', '#293337', 'on start program');
      let p2 = new Params(ctx, firstX, firstY + 1 * yHeight, 200, yHeight, radius, resa, '#14A4BE', '#25C7DC', 'ovdje ce ici tekst');
      let p3 = new Params(ctx, firstX, firstY + 2 * yHeight, 150, yHeight, radius, resa, '#463199', '#5F61B3', 'drugi tekst');
      let p4 = new Params(ctx, firstX, firstY + 3 * yHeight, 250, yHeight, radius, resa, '#14A4BE', '#25C7DC', 'jos duza treca vrsta dugog teksta')
      let p5 = new Params(ctx, firstX, firstY + 4 * yHeight, 150, yHeight, radius, resa, '#463199', '#5F61B3', 'drugi tekst');

      let o1 = new StartComponent(p1);
      o1.drawBody();
      o1.writeContent();
      let o2 = new TextComponent(p2);
      o2.drawBody();
      o2.writeContent();
      let o3 = new TextComponent(p3);
      o3.drawBody();
      o3.writeContent();
      let o4 = new TextComponent(p4);
      o4.drawBody();
      o4.writeContent();
      let o5 = new TextComponent(p5);
      o5.drawBody();
      o5.writeContent();


      // Pavlov primjer
    
      let secondX = 500;
      let secondY = 250;
      let pStart = new Params(ctx, secondX, secondY, 130, yHeight, radius, resa, '#050505', '#293337', 'on start program');
      let oStart = new StartComponent(pStart);
      oStart.drawBody();
      oStart.writeContent();

      let pLoop = new Params(ctx, secondX, secondY + 1 * yHeight, 150, yHeight, radius, resa, '#463199', '#5F61B3', 'loop until', 2);
      let oLoop = new LoopUntilTrue(pLoop);
      oLoop.drawBody();
      oLoop.writeContent();

      let pRoll = new Params(ctx, secondX + 3 * resa, secondY + 2 * yHeight, 320, yHeight, radius, resa, '#14A4BE', '#25C7DC', ['roll', 0, 'at', 24, 'speed for', '1'])
      let oRoll = new RollComponent(pRoll);
      oRoll.drawBody();
      oRoll.writeContent();

      let pDelay = new Params(ctx, secondX + 3 * resa, secondY + 3 * yHeight, 120, yHeight, radius, resa, '#463199', '#5F61B3', ['delay for', 5]);
      let oDelay = new DelayComponent(pDelay);
      oDelay.drawBody();
      oDelay.writeContent();

      let pLed = new Params(ctx, secondX, secondY + 5 * yHeight, 130, yHeight, radius, resa, '#32F9FF', '#43BEAC', ['main LED', 0]);
      let oLed = new LedComponent(pLed);
      oLed.drawBody();
      oLed.writeContent();
    

      //treca skupina

      let thirdX = 1000;
      let thirdY = 50;

      let pStart3 = new Params(ctx, thirdX, thirdY + 0 * yHeight, 130, yHeight, radius, resa,  '#050505', '#293337', 'on start program');
      let oStart3 = new StartComponent(pStart3);
      oStart3.drawBody();
      oStart3.writeContent();

      let pLoopForever = new Params(ctx, thirdX, thirdY + 1 * yHeight, 150, yHeight, radius, resa, '#463199', '#5F61B3', 'loop forever', 7);
      let oLoopForever = new LoopForever(pLoopForever);
      oLoopForever.drawBody();
      oLoopForever.writeContent();

      let pHeader = new Params(ctx, thirdX + 3 * resa, thirdY + 2 * yHeight, 120, yHeight, radius, resa, '#14A4BE', '#25C7DC', ['heading', 0]);
      let oHeader = new HeaderComponent(pHeader);
      oHeader.drawBody();
      oHeader.writeContent();

      let pLoopUntilTrue3 = new Params(ctx, thirdX + 3 * resa, thirdY + 3 * yHeight, 150, yHeight, radius, resa, '#463199', '#5F61B3', 'loop until', 4);
      let oLoopUntilTrue3 = new LoopUntilTrue(pLoopUntilTrue3);
      oLoopUntilTrue3.drawBody();
      oLoopUntilTrue3.writeContent();

      let pAim = new Params(ctx, thirdX + 6 * resa, thirdY + 4 * yHeight, 70, yHeight, radius, resa, '#14A4BE', '#25C7DC', 'reset aim');
      let oAim = new TextComponent(pAim);
      oAim.drawBody();
      oAim.writeContent();

      let pIf = new Params(ctx, thirdX + 6 * resa, thirdY + 5 * yHeight, 150, yHeight, radius, resa, '#463199', '#5F61B3', ['if', 'true', 'then'], 1);
      let oIf = new IfComponent(pIf);
      oIf.drawBody();
      oIf.writeContent();

      let pRoll32 = new Params(ctx, thirdX + 9 * resa, thirdY + 6 * yHeight, 320, yHeight, radius, resa, '#14A4BE', '#25C7DC', ['roll', 0, 'at', 0, 'speed for', '0  ']);
      let oRoll32 = new RollComponent(pRoll32);
      oRoll32.drawBody();
      oRoll32.writeContent();
    },
  },
};
</script>