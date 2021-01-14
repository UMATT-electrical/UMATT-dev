struct Message {
   unsigned long word;
   unsigned char length;
};//Message

struct Message msgMkr(unsigned long data, unsigned char size){
    struct Message msg;
    msg.word = data;
    msg.length = size;
    return msg;
}//msgMkr

void writeSPI(unsigned char CS, struct Message data){
    digitalWrite(CS, LOW);
    for (int i=0; i<data.length; i++){
        digitalWrite(MOSI,getBit(i,data.word))
        digitalWrite(CLK,HIGH);
        //add sleep function for 0.005 seconds
        digitalWrite(CLK,LOW);
        //add sleep function for 0.005 seconds
    }
    digitalWrite(MOSI, LOW);
    digitalWrite(CS, HIGH);
    //add sleep function for 0.005 seconds
}//writeSPI

unsigned char getBit(unsigned char idx, unsigned char data){
    return (data & (1 << idx)) >> idx;
}//getBit

unsigned char readSPI(unsigned char CS){
    unsigned char data;
    digitalWrite(CS, LOW);
    for (int i=0; i<8; i++){
         digitalWrite(CLK,HIGH);
         //add sleep function for 0.005 seconds
        data = data<<1 + digitalRead(MISO);
        digitalWrite(CLK,LOW);
        //add sleep function for 0.005 seconds
    }
    digitalWrite(CS, HIGH);
    return data;
}//readSPI
