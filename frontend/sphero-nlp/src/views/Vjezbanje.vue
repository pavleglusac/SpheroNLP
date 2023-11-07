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
      const canvas = this.$refs.customCanvas;
      const ctx = canvas.getContext('2d');

      canvas.width = 1500; 
      canvas.height = 1500; 

      let resa = 7
      let radius = 5

      let firstX = 50;
      let firstY = 50;
      let yHeight = 50;

      this.drawStart(ctx, firstX, firstY, 130, yHeight, radius, resa, '#293337', '#050505', 'on start program')
      this.roundedRect(ctx, firstX, firstY + 1 * yHeight, 200, yHeight, radius, resa, '#25C7DC', '#14A4BE', 'ovdje ce ici tekst');
      this.roundedRect(ctx, firstX, firstY + 2 * yHeight, 150, yHeight, radius, resa, '#5F61B3', '#463199', 'drugi tekst');
      this.roundedRect(ctx, firstX, firstY + 3 * yHeight, 250, yHeight, radius, resa, '#25C7DC', '#14A4BE', 'jos duza treca vrsta dugog teksta');
      this.roundedRect(ctx, firstX, firstY + 4 * yHeight, 150, yHeight, radius, resa, '#5F61B3', '#463199', 'drugi tekst');
      this.roundedRect(ctx, firstX, firstY + 5 * yHeight, 200, yHeight, radius, resa, '#25C7DC', '#14A4BE', 'treca drugi tekst drugi tekst');


      let secondX = 500;
      let secondY = 250;
      this.drawStart(ctx, secondX, secondY + 0 * yHeight, 130, yHeight, radius, resa, '#293337', '#050505', 'on start program')
      this.drawLoopUntilTrue(ctx, secondX, secondY + 1 * yHeight, 150, yHeight, radius, resa, '#5F61B3', '#463199', 'loop until', 2);
      this.drawBasicRectangle(ctx, secondX + 3 * resa, secondY + 2 * yHeight, 320, yHeight, radius, resa, '#25C7DC', '#14A4BE', ['roll', 0, 'at', 24, 'speed for', '1']);
      this.drawDelayFor(ctx, secondX + 3 * resa, secondY + 3 * yHeight, 120, yHeight, radius, resa, '#5F61B3', '#463199', 'delay for', 5);
      //this.roundedRect(ctx, secondX, secondY + 5 * yHeight, 200, yHeight, radius, resa, '#25C7DC', '#14A4BE', 'treca drugi tekst drugi tekst');

      let thirdX = 1000;
      let thirdY = 50;
      this.drawStart(ctx, thirdX, thirdY + 0 * yHeight, 130, yHeight, radius, resa, '#293337', '#050505', 'on start program')
      this.drawLoopForever(ctx, thirdX, thirdY + 1 * yHeight, 150, yHeight, radius, resa, '#5F61B3', '#463199', 'loop forever', 7);
      this.headingRect(ctx, thirdX + 3 * resa, thirdY + 2 * yHeight, 120, yHeight, radius, resa, '#25C7DC', '#14A4BE', ['heading', 0]);
      this.drawLoopUntilTrue(ctx, thirdX + 3 * resa, thirdY + 3 * yHeight, 150, yHeight, radius, resa, '#5F61B3', '#463199', 'loop until', 4);
      this.roundedRect(ctx, thirdX + 6 * resa, thirdY + 4 * yHeight, 70, yHeight, radius, resa, '#25C7DC', '#14A4BE', 'reset aim');
      this.drawIfTrue(ctx, thirdX + 6 * resa, thirdY + 5 * yHeight, 150, yHeight, radius, resa, '#5F61B3', '#463199', ['if', 'true', 'then'], 1);
      this.drawBasicRectangle(ctx, thirdX + 9 * resa, thirdY + 6 * yHeight, 320, yHeight, radius, resa, '#25C7DC', '#14A4BE', ['roll', 0, 'at', 0, 'speed for', '0  ']);

      let forthX = 500;
      let forthY = 50;
      this.mainLED(ctx, forthX + 3 * resa, forthY, 130, yHeight, radius, resa, '#43BEAC', '#32F9FF', ['main LED', 0]);


    },

    mainLED(ctx, x, y, width, height, radius, resa, color, insideColor, command) {
      ctx.strokeStyle = insideColor;
      ctx.fillStyle = color;
      ctx.lineWidth = 1;

      ctx.beginPath();
      ctx.moveTo(x + radius, y);                                // ovo je prva tacka, nakon luka

      ctx.lineTo(x + 3 * resa, y);
      ctx.lineTo(x + 4 * resa, y + resa);
      ctx.lineTo(x + 6 * resa, y + resa);
      ctx.lineTo(x + 7 * resa, y);        // ovo sve je bila gornja pipa
      ctx.arc(x + width,  y + (height/2), height/2, -Math.PI / 2, Math.PI / 2, false); // Arc for a semicircle
      
      //ctx.lineTo(x + radius, y + height);                       // donja linija
      ctx.lineTo(x  + 7 * resa, y + height);
      ctx.lineTo(x + 6 * resa, y + height + resa);
      ctx.lineTo(x + 4 * resa, y + height + resa);
      ctx.lineTo(x + 3 * resa, y + height);

      ctx.arcTo(x, y + height, x, y + height - radius, radius); // donji lijevi luk
      ctx.lineTo(x, y + radius);                                // lijeva linija
      ctx.arcTo(x, y, x + radius, y, radius);                   // gornji lijevi luk
      ctx.closePath();

      ctx.stroke();
      ctx.fill();

      ctx.fillStyle = 'white';
      ctx.font = '17px Arial';

      ctx.fillText(command[0], x + resa, y + height /1.6);
      //this.drawInsideRec(ctx, insideColor, x + 80, y, height, command[1] + '°');
      this.drawInsideOctagon(ctx, insideColor, x + 110, y, height);
    },


    drawIfTrue(ctx, x, y, width, height, radius, resa, color, insideColor, command, linesNum) {
      ctx.strokeStyle = insideColor;
      ctx.fillStyle = color;
      ctx.lineWidth = 1;

      ctx.beginPath();
      ctx.moveTo(x + radius, y);                                // ovo je prva tacka, nakon luka

      ctx.lineTo(x + 3 * resa, y);
      ctx.lineTo(x + 4 * resa, y + resa);
      ctx.lineTo(x + 6 * resa, y + resa);
      ctx.lineTo(x + 7 * resa, y);        // ovo sve je bila gornja pipa
      ctx.arc(x + width,  y + (height/2), height/2, -Math.PI / 2, Math.PI / 2, false); // Arc for a semicircle
      
      ctx.lineTo(x  + 10 * resa, y + height);
      ctx.lineTo(x + 9 * resa, y + height + resa);
      ctx.lineTo(x + 7 * resa, y + height + resa);
      ctx.lineTo(x + 6 * resa, y + height);
      ctx.lineTo(x + 3 * resa, y + height);

      //ctx.arcTo(x + 3 * resa - radius, y + height, x + 3 * resa - radius, y + height + radius, radius);

      let offset = (linesNum + 1) * height
      ctx.lineTo(x + 3 * resa, y + offset);          // ovdje se prvi put y spustio

      x = x + resa * 3 ;
      y = y + offset;
      ctx.lineTo(x + resa * 3, y);
      ctx.lineTo(x + resa * 4, y + resa);
      ctx.lineTo(x + 6 * resa, y + resa);
      ctx.lineTo(x + 7 * resa, y);        // ovo sve je bila gornja pipa
      ctx.arc(x + width * 1.2,  y + (height/2), height/2, -Math.PI / 2, Math.PI / 2, false); // Arc for a semicircle
      
      //ctx.lineTo(x + radius, y + height);                       // donja linija
      ctx.lineTo(x  + 4 * resa, y + height);
      ctx.lineTo(x + 3 * resa, y + height + resa);
      ctx.lineTo(x + 1 * resa, y + height + resa);
      ctx.lineTo(x + 0 * resa, y + height);


      ctx.lineTo(x - resa * 2, y + height);   // zadnji dio donje linije

      // Arc before the left line
      ctx.arcTo(x - resa * 3, y + height, x - resa * 3, y + height - radius, radius);
      ctx.lineTo(x - resa * 3, y + radius - offset);    // left line
      // Arc after the left line
      ctx.arcTo(x - resa * 3, y - offset, x - resa * 3 + radius, y - offset, radius);
      ctx.closePath();

      ctx.stroke();
      ctx.fill();
      ctx.fillStyle = 'white';
      ctx.font = '17px Arial';
      y = y - offset
      ctx.fillText(command[0], x - resa * 2, y + height /1.6);
      this.drawInsideHexagon(ctx, insideColor, x - resa * 3 + 50, y, height, 'true');
      ctx.fillText(command[2], x + 72, y + height /1.6);


      //ctx.fillStyle = 'white';
      //ctx.font = '30px Arial';
      //ctx.fillText(String.fromCharCode(0x02923), x  + 160, y + height * (linesNum + 2) - 15 );

    },




    headingRect(ctx, x, y, width, height, radius, resa, color, insideColor, command) {
      ctx.strokeStyle = insideColor;
      ctx.fillStyle = color;
      ctx.lineWidth = 1;

      ctx.beginPath();
      ctx.moveTo(x + radius, y);                                // ovo je prva tacka, nakon luka

      ctx.lineTo(x + 3 * resa, y);
      ctx.lineTo(x + 4 * resa, y + resa);
      ctx.lineTo(x + 6 * resa, y + resa);
      ctx.lineTo(x + 7 * resa, y);        // ovo sve je bila gornja pipa
      ctx.arc(x + width,  y + (height/2), height/2, -Math.PI / 2, Math.PI / 2, false); // Arc for a semicircle
      
      //ctx.lineTo(x + radius, y + height);                       // donja linija
      ctx.lineTo(x  + 7 * resa, y + height);
      ctx.lineTo(x + 6 * resa, y + height + resa);
      ctx.lineTo(x + 4 * resa, y + height + resa);
      ctx.lineTo(x + 3 * resa, y + height);

      ctx.arcTo(x, y + height, x, y + height - radius, radius); // donji lijevi luk
      ctx.lineTo(x, y + radius);                                // lijeva linija
      ctx.arcTo(x, y, x + radius, y, radius);                   // gornji lijevi luk
      ctx.closePath();

      ctx.stroke();
      ctx.fill();

      ctx.fillStyle = 'white';
      ctx.font = '17px Arial';

      ctx.fillText(command[0], x + resa, y + height /1.6);
      this.drawInsideRec(ctx, insideColor, x + 80, y, height, command[1] + '°');
    },


    drawLoopForever(ctx, x, y, width, height, radius, resa, color, insideColor, command, linesNum) {
      ctx.strokeStyle = insideColor;
      ctx.fillStyle = color;
      ctx.lineWidth = 1;

      ctx.beginPath();
      ctx.moveTo(x + radius, y);                                // ovo je prva tacka, nakon luka

      ctx.lineTo(x + 3 * resa, y);
      ctx.lineTo(x + 4 * resa, y + resa);
      ctx.lineTo(x + 6 * resa, y + resa);
      ctx.lineTo(x + 7 * resa, y);        // ovo sve je bila gornja pipa
      ctx.arc(x + width,  y + (height/2), height/2, -Math.PI / 2, Math.PI / 2, false); // Arc for a semicircle
      
      ctx.lineTo(x  + 10 * resa, y + height);
      ctx.lineTo(x + 9 * resa, y + height + resa);
      ctx.lineTo(x + 7 * resa, y + height + resa);
      ctx.lineTo(x + 6 * resa, y + height);
      ctx.lineTo(x + 3 * resa, y + height);

      //ctx.arcTo(x + 3 * resa - radius, y + height, x + 3 * resa - radius, y + height + radius, radius);

      let offset = (linesNum + 1) * height
      ctx.lineTo(x + 3 * resa, y + offset);          // ovdje se prvi put y spustio


      x = x + resa * 3 ;
      y = y + offset;
      ctx.lineTo(x + resa * 3, y);
      ctx.lineTo(x + resa * 4, y + resa);
      ctx.lineTo(x + 6 * resa, y + resa);
      ctx.lineTo(x + 7 * resa, y);        // ovo sve je bila gornja pipa
      ctx.arc(x + width * 1.2,  y + (height/2), height/2, -Math.PI / 2, Math.PI / 2, false); // Arc for a semicircle

      
      
      //ctx.lineTo(x + radius, y + height);                       // donja linija
      ctx.lineTo(x  + 4 * resa, y + height);
      ctx.lineTo(x + 3 * resa, y + height + resa);
      ctx.lineTo(x + 1 * resa, y + height + resa);
      ctx.lineTo(x + 0 * resa, y + height);


      ctx.lineTo(x - resa * 2, y + height);   // zadnji dio donje linije

      // Arc before the left line
      ctx.arcTo(x - resa * 3, y + height, x - resa * 3, y + height - radius, radius);
      ctx.lineTo(x - resa * 3, y + radius - offset);    // left line
      // Arc after the left line
      ctx.arcTo(x - resa * 3, y - offset, x - resa * 3 + radius, y - offset, radius);
      ctx.closePath();

      ctx.stroke();
      ctx.fill();
      ctx.fillStyle = 'white';
      ctx.font = '17px Arial';
      y = y - offset
      ctx.fillText(command, x - resa * 2, y + height /1.6);

      ctx.fillStyle = 'white';
      ctx.font = '30px Arial';
      ctx.fillText(String.fromCharCode(0x02923), x  + 160, y + height * (linesNum + 2) - 15 );
    },


    drawLoopUntilTrue(ctx, x, y, width, height, radius, resa, color, insideColor, command, linesNum) {
      ctx.strokeStyle = insideColor;
      ctx.fillStyle = color;
      ctx.lineWidth = 1;

      ctx.beginPath();
      ctx.moveTo(x + radius, y);                                // ovo je prva tacka, nakon luka

      ctx.lineTo(x + 3 * resa, y);
      ctx.lineTo(x + 4 * resa, y + resa);
      ctx.lineTo(x + 6 * resa, y + resa);
      ctx.lineTo(x + 7 * resa, y);        // ovo sve je bila gornja pipa
      ctx.arc(x + width,  y + (height/2), height/2, -Math.PI / 2, Math.PI / 2, false); // Arc for a semicircle
      
      ctx.lineTo(x  + 10 * resa, y + height);
      ctx.lineTo(x + 9 * resa, y + height + resa);
      ctx.lineTo(x + 7 * resa, y + height + resa);
      ctx.lineTo(x + 6 * resa, y + height);
      ctx.lineTo(x + 3 * resa, y + height);

      //ctx.arcTo(x + 3 * resa - radius, y + height, x + 3 * resa - radius, y + height + radius, radius);

      let offset = (linesNum + 1) * height
      ctx.lineTo(x + 3 * resa, y + offset);          // ovdje se prvi put y spustio


      x = x + resa * 3 ;
      y = y + offset;
      ctx.lineTo(x + resa * 3, y);
      ctx.lineTo(x + resa * 4, y + resa);
      ctx.lineTo(x + 6 * resa, y + resa);
      ctx.lineTo(x + 7 * resa, y);        // ovo sve je bila gornja pipa
      ctx.arc(x + width * 1.2,  y + (height/2), height/2, -Math.PI / 2, Math.PI / 2, false); // Arc for a semicircle

      
      
      //ctx.lineTo(x + radius, y + height);                       // donja linija
      ctx.lineTo(x  + 4 * resa, y + height);
      ctx.lineTo(x + 3 * resa, y + height + resa);
      ctx.lineTo(x + 1 * resa, y + height + resa);
      ctx.lineTo(x + 0 * resa, y + height);


      ctx.lineTo(x - resa * 2, y + height);   // zadnji dio donje linije

      // Arc before the left line
      ctx.arcTo(x - resa * 3, y + height, x - resa * 3, y + height - radius, radius);
      ctx.lineTo(x - resa * 3, y + radius - offset);    // left line
      // Arc after the left line
      ctx.arcTo(x - resa * 3, y - offset, x - resa * 3 + radius, y - offset, radius);
      ctx.closePath();

      ctx.stroke();
      ctx.fill();
      ctx.fillStyle = 'white';
      ctx.font = '17px Arial';
      y = y - offset
      ctx.fillText(command, x - resa * 2, y + height /1.6);
      this.drawInsideHexagon(ctx, insideColor, x - resa * 3 + 100, y, height, 'true');

      ctx.fillStyle = 'white';

      ctx.font = '30px Arial';
      ctx.fillText(String.fromCharCode(0x02923), x  + 160, y + height * (linesNum + 2) - 15 );
    },




    drawStart(ctx, x, y, width, height, radius, resa, color, insideColor, command) {
      ctx.strokeStyle = insideColor;
      ctx.fillStyle = color;
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(x + radius, y);                                
      ctx.arc(x + width,  y + (height/2), height/2, -Math.PI / 2, Math.PI / 2, false); // Arc for a semicircle
      
      //ctx.lineTo(x + radius, y + height);                       // donja linija
      ctx.lineTo(x  + 7 * resa, y + height);
      ctx.lineTo(x + 6 * resa, y + height + resa);
      ctx.lineTo(x + 4 * resa, y + height + resa);
      ctx.lineTo(x + 3 * resa, y + height);

      ctx.arcTo(x, y + height, x, y + height - radius, radius); // donji lijevi luk
      ctx.lineTo(x, y + radius);                                // lijeva linija
      ctx.arcTo(x, y, x + radius, y, radius);                   // gornji lijevi luk

      ctx.closePath();
      ctx.stroke();
      ctx.fill();
      ctx.fillStyle = 'white';
      ctx.font = '17px Arial';
      ctx.fillText(command, x + resa, y + height /1.6);

    },



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
    },

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
    },

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
    },



    drawBasicRectangle(ctx, x, y, width, height, radius, resa, color, insideColor, command) {
      ctx.strokeStyle = insideColor;
      ctx.fillStyle = color;
      ctx.lineWidth = 1;

      ctx.beginPath();
      ctx.moveTo(x + radius, y);                                // ovo je prva tacka, nakon luka

      ctx.lineTo(x + 3 * resa, y);
      ctx.lineTo(x + 4 * resa, y + resa);
      ctx.lineTo(x + 6 * resa, y + resa);
      ctx.lineTo(x + 7 * resa, y);        // ovo sve je bila gornja pipa
      ctx.arc(x + width,  y + (height/2), height/2, -Math.PI / 2, Math.PI / 2, false); // Arc for a semicircle
      
      //ctx.lineTo(x + radius, y + height);                       // donja linija
      ctx.lineTo(x  + 7 * resa, y + height);
      ctx.lineTo(x + 6 * resa, y + height + resa);
      ctx.lineTo(x + 4 * resa, y + height + resa);
      ctx.lineTo(x + 3 * resa, y + height);

      ctx.arcTo(x, y + height, x, y + height - radius, radius); // donji lijevi luk
      ctx.lineTo(x, y + radius);                                // lijeva linija
      ctx.arcTo(x, y, x + radius, y, radius);                   // gornji lijevi luk
      ctx.closePath();

      ctx.stroke();
      ctx.fill();

      ctx.fillStyle = 'white';
      ctx.font = '17px Arial';

      ctx.fillText(command[0], x + resa, y + height /1.6);
      this.drawInsideRec(ctx, insideColor, x + 40, y, height, command[1] + '°');

      ctx.fillText(command[2], x + resa + 100, y + height /1.6);
      this.drawInsideRec(ctx, insideColor, x + 130, y, height, command[3]);

      ctx.fillText(command[4], x + resa + 180, y + height /1.6);
      this.drawInsideRec(ctx, insideColor, x + 270, y, height, command[5] + 's' );

    },


    roundedRect(ctx, x, y, width, height, radius, resa, color, insideColor, command) {
      ctx.strokeStyle = insideColor;
      ctx.fillStyle = color;
      ctx.lineWidth = 1;

      ctx.beginPath();
      ctx.moveTo(x + radius, y);                                // ovo je prva tacka, nakon luka

      ctx.lineTo(x + 3 * resa, y);
      ctx.lineTo(x + 4 * resa, y + resa);
      ctx.lineTo(x + 6 * resa, y + resa);
      ctx.lineTo(x + 7 * resa, y);        // ovo sve je bila gornja pipa
      ctx.arc(x + width,  y + (height/2), height/2, -Math.PI / 2, Math.PI / 2, false); // Arc for a semicircle
      
      //ctx.lineTo(x + radius, y + height);                       // donja linija
      ctx.lineTo(x  + 7 * resa, y + height);
      ctx.lineTo(x + 6 * resa, y + height + resa);
      ctx.lineTo(x + 4 * resa, y + height + resa);
      ctx.lineTo(x + 3 * resa, y + height);

      ctx.arcTo(x, y + height, x, y + height - radius, radius); // donji lijevi luk
      ctx.lineTo(x, y + radius);                                // lijeva linija
      ctx.arcTo(x, y, x + radius, y, radius);                   // gornji lijevi luk
      ctx.closePath();

      ctx.stroke();
      ctx.fill();

      ctx.fillStyle = 'white';
      ctx.font = '17px Arial';
      ctx.fillText(command, x + resa, y + height /1.6);


      //this.drawInsideRec(ctx, insideColor, x + 100, y, height, '');
      
    },

    drawDelayFor(ctx, x, y, width, height, radius, resa, color, insideColor, command, number) {
      ctx.strokeStyle = insideColor;
      ctx.fillStyle = color;
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(x + radius, y);                                // ovo je prva tacka, nakon luka

      ctx.lineTo(x + 3 * resa, y);
      ctx.lineTo(x + 4 * resa, y + resa);
      ctx.lineTo(x + 6 * resa, y + resa);
      ctx.lineTo(x + 7 * resa, y);        // ovo sve je bila gornja pipa
      ctx.arc(x + width,  y + (height/2), height/2, -Math.PI / 2, Math.PI / 2, false); // Arc for a semicircle
      
      //ctx.lineTo(x + radius, y + height);                       // donja linija
      ctx.lineTo(x  + 7 * resa, y + height);
      ctx.lineTo(x + 6 * resa, y + height + resa);
      ctx.lineTo(x + 4 * resa, y + height + resa);
      ctx.lineTo(x + 3 * resa, y + height);

      ctx.arcTo(x, y + height, x, y + height - radius, radius); // donji lijevi luk
      ctx.lineTo(x, y + radius);                                // lijeva linija
      ctx.arcTo(x, y, x + radius, y, radius);                   // gornji lijevi luk
      ctx.closePath();

      ctx.stroke();
      ctx.fill();

      ctx.fillStyle = 'white';
      ctx.font = '17px Arial';
      ctx.fillText(command, x + resa, y + height /1.6);


      this.drawInsideRec(ctx, insideColor, x - 3 * resa + 100, y, height, number + 's');
      
    },
  },
};
</script>
